from modules.core import cargarDatos, guardarDatos
from modules.utils import limpiarPantalla, pausar
from modules.messages import mostrarTitulo, mostrarError, mostrarExito

def crearContacto():
    """
    Pide al usuario los datos del contacto, valida que el ID no exista y lo guarda en el archivo JSON.
    """
    limpiarPantalla()
    mostrarTitulo("Nuevo Contacto")

    datos = cargarDatos()
    contactos = datos.get("contactos", [])

    idContacto = input("Ingrese el ID del contacto: ").strip()

    if not idContacto:
        mostrarError("El ID del contacto no puede estar vacío.")
        pausar()
        return
    
    """
    Validar que el ID del contacto no exista en la lista de contactos.
    """
    for contacto in contactos:
        if contacto["id"] == idContacto:
            mostrarError("El ID del contacto ya existe. Intente con otro ID.")
            pausar()
            return
    
    nombres = input("Ingrese el nombre del contacto: ").strip()
    apellidos = input("Ingrese los apellidos del contacto: ").strip()
    telefono = input("Ingrese el teléfono del contacto: ").strip()
    email = input("Ingrese el correo electrónico del contacto: ").strip()
    direccion = input("Ingrese la dirección del contacto: ").strip()
    tipo = input("Ingrese el tipo de contacto (personal o profesional): ").strip().lower()
    notas = input("Ingrese notas adicionales sobre el contacto: ").strip()

    nuevoContacto = {
        "id": idContacto,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "tipo": tipo,
        "notas": notas
    }

    contactos.append(nuevoContacto)
    datos["contactos"] = contactos
    guardarDatos(datos)

    mostrarExito("Contacto creado exitosamente.")
    pausar()

def listarContactos():
    """
    Muestra una tabla con todos los contactos registrados en el sistema.
    """
    limpiarPantalla()
    mostrarTitulo("Lista de Contactos")

    datos = cargarDatos()
    contactos = datos.get("contactos", [])

    if len(contactos) == 0:
        print("No hay contactos registrados.")
    else:
        """
        Imprime una tabla con los contactos.
        """
        print(f"{'ID':<10} | {'Nombre Completo':<30} | {'Teléfono':<15} | {'Email':<25} | {'Tipo':<15}")
        print("-" * 105)

        for c in contactos:
            nombreCompleto = f"{c['nombres']} {c['apellidos']}"
            print(f"{c['id']:<10} | {nombreCompleto[:30]:<30} | {c['telefono'][:15]:<15} | {c['email'][:25]:<25} | {c['tipo'][:15]:<15}")

    print("\n" + "-" * 105)
    pausar()

def buscarContacto():
    """
    Permite buscar contactos por ID, nombre/apellido o tipo.
    """
    limpiarPantalla()
    mostrarTitulo("Buscar Contacto")

    datos = cargarDatos()
    contactos = datos.get("contactos", [])

    if len(contactos) == 0:
        print("No hay contactos registrados para buscar.")
        pausar()
        return
    
    print("Opciones de búsqueda:")
    print("1. Por ID")
    print("2. Por nombre o apellidos (búsqueda parcial)")
    print("3. Por tipo de contacto")

    opcion = input("\nSeleccione cómo desea buscar: ").strip()
    termino = input("Ingrese el término de búsqueda: ").strip().lower()

    resultados = []

    for c in contactos:
        if opcion == "1":
            if termino in c["id"].lower():
                resultados.append(c)
        elif opcion == "2":
            if termino in c["nombres"].lower() or termino in c["apellidos"].lower():
                resultados.append(c)
        elif opcion == "3":
            if termino in c["tipo"].lower():
                resultados.append(c)

    if len(resultados) == 0:
        mostrarError("No se encontraron contactos que coincidan con la búsqueda.")
    else:
        print("\n--- Resultados de Búsqueda ---")
        print(f"{'ID':<10} | {'Nombre Completo':<30} | {'Teléfono':<15} | {'Email':<25} | {'Tipo':<15}")
        print("-" * 105)
        for c in resultados:
            nombreCompleto = f"{c['nombres']} {c['apellidos']}"
            print(f"{c['id']:<10} | {nombreCompleto[:30]:<30} | {c['telefono'][:15]:<15} | {c['email'][:25]:<25} | {c['tipo'][:15]:<15}")
            
    pausar()

def actualizarContacto():
    """
    Busca un contacto por ID y permite modificar cualquiera de sus datos.
    """
    limpiarPantalla()
    mostrarTitulo("Actualizar Contacto")

    datos = cargarDatos()
    contactos = datos.get("contactos", [])

    idBuscar = input("Ingrese el ID del contacto a actualizar: ").strip()

    contactoEncontrado = None
    indice = -1

    for i in range(len(contactos)):
        if contactos[i]["id"] == idBuscar:
            contactoEncontrado = contactos[i]
            indice = i
            break
    
    if not contactoEncontrado:
        mostrarError("No se encontró ningún contacto con ese ID.")
        pausar()
        return
    
    print(f"\nActualizando: {contactoEncontrado['nombres']} {contactoEncontrado['apellidos']}")
    print("Nota: Deje el campo en blanco y presione Enter si no desea modificarlo.\n")

    nuevoNombre = input(f"Nombres ({contactoEncontrado['nombres']}): ").strip()
    nuevoApellido = input(f"Apellidos ({contactoEncontrado['apellidos']}): ").strip()
    nuevoTelefono = input(f"Teléfono ({contactoEncontrado['telefono']}): ").strip()
    nuevoEmail = input(f"E-mail ({contactoEncontrado['email']}): ").strip()
    nuevaDireccion = input(f"Dirección ({contactoEncontrado['direccion']}): ").strip()
    nuevoTipo = input(f"Tipo ({contactoEncontrado['tipo']}): ").strip()
    nuevasNotas = input(f"Notas ({contactoEncontrado['notas']}): ").strip()

    if nuevoNombre: contactos[indice]["nombres"] = nuevoNombre
    if nuevoApellido: contactos[indice]["apellidos"] = nuevoApellido
    if nuevoTelefono: contactos[indice]["telefono"] = nuevoTelefono
    if nuevoEmail: contactos[indice]["email"] = nuevoEmail
    if nuevaDireccion: contactos[indice]["direccion"] = nuevaDireccion
    if nuevoTipo: contactos[indice]["tipo"] = nuevoTipo
    if nuevasNotas: contactos[indice]["notas"] = nuevasNotas

    datos["contactos"] = contactos
    guardarDatos(datos)
    mostrarExito("Contacto actualizado correctamente.")
    pausar()

def eliminarContacto():
    """
    Busca un contacto por ID, pide confirmación y lo elimina.
    """
    limpiarPantalla()
    mostrarTitulo("Eliminar Contacto")

    datos = cargarDatos()
    contactos = datos.get("contactos", [])

    idBuscar = input("Ingrese el ID del contacto que desea eliminar: ").strip()
    
    contactoEncontrado = None
    indice = -1

    for i in range(len(contactos)):
        if contactos[i]["id"] == idBuscar:
            contactoEncontrado = contactos[i]
            indice = i
            break

    if not contactoEncontrado:
        mostrarError("No se encontró ningún contacto con ese ID.")
        pausar()
        return
    
    print(f"\nSe eliminará a: {contactoEncontrado['nombres']} {contactoEncontrado['apellidos']}")
    confirmacion = input("¿Está seguro? Escriba 's' para confirmar, 'n' para cancelar: ").strip().lower()

    if confirmacion == "s":
        contactos.pop(indice)
        datos["contactos"] = contactos
        guardarDatos(datos)
        mostrarExito("Contacto eliminado correctamente.")
    else:
        print("\nOperación cancelada.")

    pausar()

def menuContactos():
    """
    Muestra el submenú de gestión de contactos y maneja las opciones seleccionadas por el usuario.
    """
    while True:
        limpiarPantalla()
        mostrarTitulo("Gestión de Contactos")

        print("1. Registrar nuevo contacto")
        print("2. Listar todos los contactos")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            crearContacto()
        elif opcion == "2":
            listarContactos()
        elif opcion == "3":
            buscarContacto()
        elif opcion == "4":
            actualizarContacto()
        elif opcion == "5":
            eliminarContacto()
        elif opcion == "6":
            break
        else:
            mostrarError("Opción no válida. Intente de nuevo.")
            pausar()
