from modules.core import cargarDatos
from modules.utils import limpiarPantalla, pausar
from modules.messages import mostrarTitulo, mostrarError, mostrarExito
from modules.crud_contacts import menuContactos
from modules.crud_users import menuUsuarios
from modules.audit import auditarDatos

def login():
    """
    Maneja el proceso de inicio de sesión del usuario.
    Retorna el diccionario del usuario si el inicio de sesión es exitoso, o None si falla.
    """
    limpiarPantalla()
    mostrarTitulo("ACME SOLUTIONS - INICIO DE SESIÓN")

    email = input("Ingrese su correo electrónico: ").strip()
    password = input("Ingrese su contraseña: ").strip()

    datos = cargarDatos()
    usuarios = datos.get("usuarios", [])

    for usuario in usuarios:
        if usuario["email"] == email and usuario["password"] == password:
            return usuario
        
    return None

def menuPrincipal(usuarioActual):
    """
    Muestra el menú principal después de un inicio de sesión exitoso y maneja las opciones seleccionadas por el usuario.
    """
    while True:
        limpiarPantalla()
        mostrarTitulo(f"ACME SOLUTIONS - BIENVENIDO {usuarioActual['nombres'].upper()}")
        
        print("1. Gestión de contactos")
        
        # Muestra solo las opciones de gestión si el usuario actual es un administrador.
        if usuarioActual["rol"] == "administrador":
            print("2. Gestión de usuarios")
            print("3. Auditoría de datos")
            print("4. Salir del sistema")
        else:
            print("2. Salir del sistema")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menuContactos()
        elif opcion == "2" and usuarioActual["rol"] == "administrador":
            menuUsuarios(usuarioActual)
        elif opcion == "3" and usuarioActual["rol"] == "administrador":
            auditarDatos()
        elif (opcion == "2" and usuarioActual["rol"] != "administrador") or (opcion == "4" and usuarioActual["rol"] == "administrador"):
            limpiarPantalla()
            mostrarExito("¡Gracias por usar el Gestor de Contactos ACME!")
            break
        else:
            mostrarError("Opción no válida. Intente de nuevo.")
            pausar()
    
def main():
    """
    Punto de entrada principal del programa. Maneja el flujo de inicio de sesión y acceso al menú principal.
    """
    intentos = 3
    usuarioValido = None

    while intentos > 0:
        usuarioValido = login()
        if usuarioValido:
            break
        else:
            intentos -= 1
            mostrarError(f"Credenciales incorrectas. Intentos restantes: {intentos}")
            pausar()
            
    if usuarioValido:
        mostrarExito(f"¡Bienvenido, {usuarioValido['nombres']}!")
        pausar()
        menuPrincipal(usuarioValido)
    else:
        limpiarPantalla()
        mostrarError("Demasiados intentos fallidos. El programa se cerrará.")

if __name__ == "__main__":
    main()