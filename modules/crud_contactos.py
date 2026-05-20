from modules.core import cargarDatos, guardarDatos
from modules.utils import limpiarPantalla, pausar
from modules.messages import mostrarTitulo, mostrarError, mostrarExito

def crearContacto():
    """
    Pide al usuario los datos del contacto, valido qu el ID no exista y lo guarda en el archivo JSON.
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
    validar que el ID del contacto no exista en la lista de contactos
    """
    for contacto in contactos:
        if contacto["id"] == idContacto:
            mostrarError("El ID del contacto ya existe. Intente con otro ID.")
            pausar()
            return
    
    nombres= input("Ingrese el nombre del contacto: ").strip()
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
        Imprime una tabla con los contactos, mostrando solo el ID, nombres, apellidos, teléfono y email.
        """
        print(f"{'ID':<10} | {'Nombre Completo':<30} | {'Teléfono':<15} | {'Email':<25} | {'Tipo':<15}")
        print("-" * 105)

        for c in contactos:
            nombreCompleto = f"{c['nombres']} {c['apellidos']}"
            # Se usa :<10 para alinear el texto a la izquierda en esos espacios (formateo de strings)
            print(f"{c['id']:<10} | {nombreCompleto[:30]:<30} | {c['telefono'][:15]:<15} | {c['email'][:25]:<25} | {c['tipo'][:15]:<15}")

    print("\n" + "-" * 105)
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
        elif opcion in ["3", "4", "5"]:
            print("\n(En construcción - Fase 4)")
            pausar()
        elif opcion == "6":
            break
        else:
            mostrarError("Opción no válida. Intente de nuevo.")
            pausar()
