from modules.core import cargarDatos, guardarDatos
from modules.utils import limpiarPantalla, pausar
from modules.messages import mostrarTitulo, mostrarError, mostrarExito

def crearUsuario(usuarioActual):
    """
    Pide los datos de un nuevo usuario, valida que el correo no exista y lo guarda en el JSON.
    Solo puede ser ejecutada por un usuario con rol 'admin'.
    """
    limpiarPantalla()
    mostrarTitulo("Registrar Nuevo Usuario")

    if usuarioActual.get("rol") != "admin":
        mostrarError("Acceso denegado. Solo los administradores pueden crear usuarios.")
        pausar()
        return

    datos = cargarDatos()
    usuarios = datos.get("usuarios", [])

    print("Por favor ingrese los datos del nuevo usuario:")
    idUsuario = input("Número de identificación: ").strip()

    if not idUsuario:
        mostrarError("El número de identificación no puede estar vacío.")
        pausar()
        return

    for u in usuarios:
        if u["id"] == idUsuario:
            mostrarError("Ya existe un usuario con ese número de identificación.")
            pausar()
            return

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    telefono = input("Número de teléfono: ").strip()
    email = input("E-mail corporativo (será su usuario): ").strip()

    if not email:
        mostrarError("El correo electrónico no puede estar vacío.")
        pausar()
        return

    for u in usuarios:
        if u["email"] == email:
            mostrarError("Ya existe un usuario con este correo electrónico.")
            pausar()
            return

    direccion = input("Dirección: ").strip() 
    rol = input("Rol (admin / usuario): ").strip().lower()

    if rol not in ["admin", "usuario"]:
        print("Rol no reconocido, se asignará 'usuario' por defecto.")
        rol = "usuario"

    password = input("Contraseña: ").strip()

    if not password:
        mostrarError("La contraseña no puede estar vacía.")
        pausar()
        return

    nuevoUsuario = {
        "id": idUsuario,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "rol": rol,
        "password": password
    }

    usuarios.append(nuevoUsuario)
    datos["usuarios"] = usuarios 
    guardarDatos(datos)

    mostrarExito("Usuario registrado exitosamente.")
    pausar()

def listarUsuarios():
    """
    Muestra una tabla con todos los usuarios registrados en el sistema.
    """
    limpiarPantalla()
    mostrarTitulo("Lista de Usuarios")

    datos = cargarDatos() 
    usuarios = datos.get("usuarios", [])

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        print(f"{'ID':<12} | {'NOMBRE COMPLETO':<30} | {'E-MAIL (USUARIO)':<30} | {'ROL':<10}")
        print("-" * 92)
        for u in usuarios:
            nombreCompleto = f"{u['nombres']} {u['apellidos']}"
            print(f"{u['id'][:12]:<12} | {nombreCompleto[:30]:<30} | {u['email'][:30]:<30} | {u['rol'][:10]:<10}")

    print("\n" + "-" * 92)
    pausar()

def menuUsuarios(usuarioActual):
    """
    Muestra el submenú de gestión de usuarios y maneja las opciones seleccionadas.
    Solo accesible para usuarios con rol 'admin'.
    """
    while True:
        limpiarPantalla()
        mostrarTitulo("Gestión de Usuarios")

        print("1. Registrar nuevo usuario")
        print("2. Listar usuarios")
        print("3. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crearUsuario(usuarioActual)
        elif opcion == "2":
            listarUsuarios()
        elif opcion == "3":
            break
        else:
            mostrarError("Opción no válida. Intente de nuevo.")
            pausar()
