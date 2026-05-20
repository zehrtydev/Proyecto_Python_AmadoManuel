En la empresa ACME Solutions, los empleados suelen almacenar sus contactos personales y laborales en hojas de cálculo desordenadas, notas en el celular y correos sueltos, dificultando encontrar rápidamente un número, un correo o la información de una persona específica cuando se necesita. Para solucionar este problema, se solicita el desarrollo de un Gestor de Lista de Contactos que permita a los usuarios registrar, consultar, buscar, actualizar y eliminar contactos de manera centralizada y persistente.

Login
El sistema debe iniciar siempre mostrando una interfaz de inicio de sesión, donde el usuario ingresa:

Usuario: e-mail corporativo.
Contraseña
Solo si las credenciales son correctas, el usuario podrá acceder al menú principal del sistema.

Nota: Al igual que en otros sistemas de la empresa, el primer usuario debe venir precargado en el archivo de datos:
Nombre: Admin
Apellidos: Administrador
Teléfono: 555 000111
e-mail: admin@acmesolutions.com
Dirección: Cl 185 # 26 – 85
Rol: administrador
Contraseña: admin123 (o la que se defina en el archivo JSON inicial)

Registro de usuarios del sistema
Los usuarios del sistema son los empleados que administran la lista de contactos (pueden ser administrativos, asesores comerciales, etc.).

A continuación se presentan los datos para registrar un usuario adentro del sistema:

Número de identificación
Nombres
Apellidos
Número de teléfono
e-mail (corporativo) → será el nombre de usuario
Dirección
Rol (por ejemplo: admin / operario)
Contraseña
Solo un usuario autenticado podrá registrar nuevos usuarios, donde dicha opción se restringe para ser solamente habilitada para el rol admin.

Gestión de contactos
Los contactos son las personas externas o internas con las que la empresa se comunica, los cuales pueden ser clientes, proveedores, aliados, etc.

Los datos mínimos de un contacto son los siguientes:

Número de identificación (o ID interno)
Nombres
Apellidos
Teléfono principal
e-mail
Dirección
Tipo de contacto (cliente, proveedor, aliado, personal, etc.)
Notas (campo de texto libre para observaciones)

El sistema deberá permitir:

Registrar contactos
Ingresar todos los datos anteriores.
Validar que no se duplique el identificador del contacto.
Listar contactos
Mostrar en forma de tabla en consola:
ID, nombre completo, teléfono, e-mail, tipo de contacto.
Buscar contactos
Permitir buscar por:
Número de identificación
Nombre o apellidos (búsqueda parcial)
Tipo de contacto
Mostrar los resultados en una tabla con sus datos principales.
Actualizar contactos
Buscar al contacto por su ID.
Permitir modificar cualquiera de sus campos (teléfono, e-mail, dirección, tipo, notas, etc.).
Guardar los cambios en el archivo de datos.
Eliminar contactos
Permitir eliminar un contacto por su ID.
Confirmar antes de borrar definitivamente.

Persistencia de datos
Toda la información debe almacenarse en un archivo JSON, que contendrá al menos los siguientes datos:

{
  "usuarios": [
    {
      "id": "0000",
      "nombres": "Admin",
      "apellidos": "Administrador",
      "telefono": "555 000111",
      "email": "admin@acmesolutions.com",
      "direccion": "Cl 185 # 26 – 85",
      "password": "admin123",
      "rol": "admin"
    }
  ],
  "contactos": []
}
Cada vez que se:

Registre, actualice o elimine un usuario
Registre, actualice o elimine un contacto

El archivo JSON deberá actualizarse para mantener persistencia de la información.

La entrega de este proyecto se realizará de manera individual, donde se debe anexar un enlace a un repositorio en GitHub publico llamado “Proyecto_Python_ApellidoNombre” (Proyecto_Python_Apellido1Nombre1Apellido2Nombre2 donde aplique) que contenga el código de la aplicación construida en Python. En este mismo repositorio, debe contener los siguientes archivos:

Archivo principal de ejecución basado en Python (archivo app.py).
Archivos modularizados que den funcionalidad al programa principal de Python (carpeta modules con archivos core.py, utils.py, messages.py, crud_usuarios.py y crud_contactos.py).
Archivo JSON que almacene la información del programa en sí (carpeta data con archivo agenda.json).
