import json
import os
import re

from modules.core import cargarDatos
from modules.utils import limpiarPantalla, pausar
from modules.messages import mostrarTitulo, mostrarError, mostrarExito

"""Archivo de salida para el reporte"""
rutaReporte = "reporte_auditoria.json"

"""Conjunto de valores permitidos"""
rolesPermitidos = {"administrador", "usuario"}
tiposContactosPermitidos = {"personal", "trabajo"}


def validarTelefono(telefono):
    """Valida que el número de teléfono tenga un formato correcto."""
    if not telefono:
        return False

    telefonoLimpio = str(telefono).replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("+", "")
    return telefonoLimpio.isdigit()


def validarEmail(email):
    """Valida que el correo electrónico tenga un formato correcto."""
    if not email:
        return False

    patronEmail = r'^[^@]+@[^@]+\.[^@]+$'
    return bool(re.match(patronEmail, str(email).strip()))


def auditarDatos():
    """Realiza la auditoría de los datos de contactos y usuarios."""
    limpiarPantalla()
    mostrarTitulo("Auditoría de Consistencia de Datos")
    print("Iniciando auditoría de datos...")

    datos = cargarDatos()
    usuarios = datos.get("usuarios", [])
    contactos = datos.get("contactos", [])

    usuariosConErrores = []
    contactosConErrores = []
    emailsUsuarios = {}
    idsContactos = {}

    camposObligatoriosUsuarios = {"id", "nombres", "apellidos", "telefono", "email", "direccion", "password", "rol"}
    for idx, u in enumerate(usuarios):
        erroresUsuario = []
        userId = u.get("id")
        userEmail = u.get("email")

        for campo in camposObligatoriosUsuarios:
            valor = u.get(campo)
            if valor is None or str(valor).strip() == "":
                erroresUsuario.append(f"Campo obligatorio '{campo}' es obligatorio y no puede estar vacío.")

        if "email" in u and u["email"]:
            emailStrip = str(u["email"]).strip()
            if not validarEmail(emailStrip):
                erroresUsuario.append(f"El correo electrónico '{emailStrip}' no tiene un formato válido.")
            if emailStrip.lower() not in emailsUsuarios:
                emailsUsuarios[emailStrip.lower()] = []
            emailsUsuarios[emailStrip.lower()].append(userId or f"sinIdIndex{idx}")

        if "rol" in u and u["rol"]:
            rolClean = str(u["rol"]).strip().lower()
            if rolClean not in rolesPermitidos:
                erroresUsuario.append(f"El rol '{u['rol']}' no es válido. Valores permitidos: {list(rolesPermitidos)}.")

        if erroresUsuario:
            usuariosConErrores.append({
                "id": userId if userId else f"sinIdIndex{idx}",
                "email": userEmail if userEmail else "sinEmail",
                "errores": erroresUsuario
            })

    emailsDuplicados = {email for email, ids in emailsUsuarios.items() if len(ids) > 1}
    for emailDuplicado in emailsDuplicados:
        for idx, u in enumerate(usuarios):
            userEmail = u.get("email")
            if userEmail and str(userEmail).strip().lower() == emailDuplicado:
                userId = u.get("id") or f"sinIdIndex{idx}"
                encontrado = False
                for u_err in usuariosConErrores:
                    if u_err["id"] == userId:
                        u_err["errores"].append(f"El correo electrónico '{emailDuplicado}' está duplicado.")
                        encontrado = True
                        break
                if not encontrado:
                    usuariosConErrores.append({
                        "id": userId,
                        "email": userEmail,
                        "errores": [f"El correo electrónico '{emailDuplicado}' está duplicado."]
                    })

    camposObligatoriosContactos = {"id", "nombres", "apellidos", "telefono", "email"}
    for idx, c in enumerate(contactos):
        erroresContacto = []
        contactoId = c.get("id")

        for campo in camposObligatoriosContactos:
            valor = c.get(campo)
            if valor is None or str(valor).strip() == "":
                erroresContacto.append(f"Campo obligatorio '{campo}' es obligatorio y no puede estar vacío.")

        tipoValor = c.get("tipo") or c.get("tipoContacto")
        if tipoValor is None or str(tipoValor).strip() == "":
            erroresContacto.append("El campo 'tipo' es obligatorio y no puede estar vacío.")
        else:
            tipoClean = str(tipoValor).strip().lower()
            if tipoClean not in tiposContactosPermitidos:
                erroresContacto.append(f"El tipo de contacto '{tipoValor}' no es válido. Valores permitidos: {list(tiposContactosPermitidos)}.")

        if "telefono" in c and c["telefono"]:
            if not validarTelefono(c["telefono"]):
                erroresContacto.append(f"El número de teléfono '{c['telefono']}' no tiene un formato válido.")

        if "email" in c and c["email"]:
            emailStrip = str(c["email"]).strip()
            if not validarEmail(emailStrip):
                erroresContacto.append(f"El correo electrónico '{emailStrip}' no tiene un formato válido.")

        if contactoId is not None and str(contactoId).strip() != "":
            idStr = str(contactoId).strip()
            if idStr not in idsContactos:
                idsContactos[idStr] = []
            idsContactos[idStr].append(idx)

        if erroresContacto:
            contactosConErrores.append({
                "id": contactoId if contactoId else f"sinIdIndex{idx}",
                "errores": erroresContacto
            })

    idsDuplicados = {cid for cid, idxs in idsContactos.items() if len(idxs) > 1}
    for idDuplicado in idsDuplicados:
        for idx, c in enumerate(contactos):
            contactoId = c.get("id")
            if contactoId is not None and str(contactoId).strip() == idDuplicado:
                encontrado = False
                for c_err in contactosConErrores:
                    if c_err["id"] == contactoId:
                        c_err["errores"].append(f"El ID de contacto '{idDuplicado}' está duplicado.")
                        encontrado = True
                        break
                if not encontrado:
                    contactosConErrores.append({
                        "id": contactoId,
                        "errores": [f"El ID de contacto '{idDuplicado}' está duplicado."]
                    })

    totalUsuarios = len(usuarios)
    totalContactos = len(contactos)
    totalUsuariosConErrores = len(usuariosConErrores)
    totalContactosConErrores = len(contactosConErrores)
    totalEmailsDuplicados = len(emailsDuplicados)
    totalIdsDuplicados = len(idsDuplicados)

    tieneErrores = (totalUsuariosConErrores > 0 or totalContactosConErrores > 0)
    mensajeGlobal = (
        "Se encontraron inconsistencias en la auditoría de datos."
        if tieneErrores else
        "No se encontraron inconsistencias en la auditoría de datos. Todos los registros son consistentes."
    )

    reporte = {
        "mensaje_global": mensajeGlobal,
        "usuarios_con_errores": usuariosConErrores,
        "contactos_con_errores": contactosConErrores,
        "resumen": {
            "total_usuarios": totalUsuarios,
            "total_contactos": totalContactos,
            "usuarios_con_errores": totalUsuariosConErrores,
            "contactos_con_errores": totalContactosConErrores,
            "usuarios_con_email_duplicado": totalEmailsDuplicados,
            "contactos_con_id_duplicado": totalIdsDuplicados
        }
    }

    try:
        with open(rutaReporte, "w", encoding="utf-8") as archivoReporte:
            json.dump(reporte, archivoReporte, ensure_ascii=False, indent=4)
        print(f"Auditoría completada. El reporte se ha guardado en '{rutaReporte}'.")
    except Exception as e:
        mostrarError(f"Ocurrió un error al guardar el reporte de auditoría: {str(e)}")
        pausar()
        return

    print("=" * 50)
    print("RESUMEN DE AUDITORÍA".center(50))
    print("=" * 50)
    print(f"Total de usuarios evaluados:  {totalUsuarios}")
    print(f"Total de contactos evaluados: {totalContactos}")
    print("-" * 50)

    if tieneErrores:
        mostrarError(f"Usuarios con errores detectados: {totalUsuariosConErrores}")
        mostrarError(f"Contactos con errores detectados: {totalContactosConErrores}")
        if totalEmailsDuplicados > 0:
            print(f" -> Correos de usuario duplicados: {totalEmailsDuplicados}")
        if totalIdsDuplicados > 0:
            print(f" -> IDs de contacto duplicados:    {totalIdsDuplicados}")
        print("\nPara ver la lista detallada de errores, consulte el archivo:")
        print(f" -> {os.path.abspath(rutaReporte)}")
    else:
        mostrarExito("¡Auditoría completada sin inconsistencias detectadas!")
        print("\nSe generó un reporte limpio en:")
        print(f" -> {os.path.abspath(rutaReporte)}")

    print("=" * 50)
    pausar()