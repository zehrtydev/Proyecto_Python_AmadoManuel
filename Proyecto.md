# 📋 Proyecto: Gestor de Lista de Contactos — ACME Solutions

## 📌 Descripción del problema

En la empresa **ACME Solutions**, los empleados suelen almacenar sus contactos personales y laborales en hojas de cálculo desordenadas, notas en el celular y correos sueltos, dificultando encontrar rápidamente un número, un correo o la información de una persona específica cuando se necesita.

Para solucionar este problema, se solicita el desarrollo de un **Gestor de Lista de Contactos** que permita a los usuarios registrar, consultar, buscar, actualizar y eliminar contactos de manera **centralizada y persistente**.

---

## 🔐 Login

El sistema debe iniciar siempre mostrando una interfaz de **inicio de sesión**, donde el usuario ingresa:

- **Usuario:** e-mail corporativo
- **Contraseña**

Solo si las credenciales son correctas, el usuario podrá acceder al menú principal del sistema.

> **Nota:** Al igual que en otros sistemas de la empresa, el primer usuario debe venir **precargado** en el archivo de datos:
>
> | Campo      | Valor                     |
> |------------|---------------------------|
> | Nombre     | Admin                     |
> | Apellidos  | Administrador             |
> | Teléfono   | 555 000111                |
> | E-mail     | admin@acmesolutions.com   |
> | Dirección  | Cl 185 # 26 – 85         |
> | Rol        | administrador             |
> | Contraseña | admin123                  |

---

## 👤 Registro de usuarios del sistema

Los **usuarios del sistema** son los empleados que administran la lista de contactos (pueden ser administrativos, asesores comerciales, etc.).

### Datos del usuario

| Campo                  | Descripción                              |
|------------------------|------------------------------------------|
| Número de identificación | Identificador único del empleado       |
| Nombres                | Nombres del empleado                     |
| Apellidos              | Apellidos del empleado                   |
| Número de teléfono     | Teléfono de contacto                     |
| E-mail corporativo     | Será el nombre de usuario en el sistema  |
| Dirección              | Dirección de residencia                  |
| Rol                    | `admin` o `usuario`                      |
| Contraseña             | Clave de acceso al sistema               |

> ⚠️ Solo un usuario autenticado podrá registrar nuevos usuarios. Esta opción **está restringida exclusivamente al rol `admin`**.

---

## 📇 Gestión de contactos

Los **contactos** son las personas externas o internas con las que la empresa se comunica: clientes, proveedores, aliados, etc.

### Datos del contacto

| Campo                    | Descripción                                      |
|--------------------------|--------------------------------------------------|
| Número de identificación | ID interno o documento                           |
| Nombres                  | Nombres del contacto                             |
| Apellidos                | Apellidos del contacto                           |
| Teléfono principal       | Número de contacto                               |
| E-mail                   | Correo electrónico                               |
| Dirección                | Dirección del contacto                           |
| Tipo de contacto         | cliente, proveedor, aliado, personal, etc.       |
| Notas                    | Campo de texto libre para observaciones          |

### Operaciones disponibles

#### ➕ Registrar contactos
- Ingresar todos los datos del contacto.
- Validar que no se duplique el identificador del contacto.

#### 📋 Listar contactos
Mostrar en forma de tabla en consola:
`ID | Nombre completo | Teléfono | E-mail | Tipo de contacto`

#### 🔍 Buscar contactos
Permitir buscar por:
- Número de identificación
- Nombre o apellidos *(búsqueda parcial)*
- Tipo de contacto

Mostrar los resultados en una tabla con sus datos principales.

#### ✏️ Actualizar contactos
- Buscar al contacto por su ID.
- Permitir modificar cualquiera de sus campos (teléfono, e-mail, dirección, tipo, notas, etc.).
- Guardar los cambios en el archivo de datos.

#### 🗑️ Eliminar contactos
- Permitir eliminar un contacto por su ID.
- **Confirmar antes de borrar definitivamente.**

---

## 💾 Persistencia de datos

Toda la información debe almacenarse en un **archivo JSON**, con la siguiente estructura mínima:

```json
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
```

El archivo JSON deberá actualizarse cada vez que se:

- ✅ Registre, actualice o elimine un **usuario**
- ✅ Registre, actualice o elimine un **contacto**

---

## 📁 Estructura del proyecto

```
Proyecto_Python_ApellidoNombre/
│
├── app.py                  # Archivo principal de ejecución
├── data/
│   └── agenda.json         # Almacenamiento persistente de datos
└── modules/
    ├── core.py             # Carga y guardado del archivo JSON
    ├── utils.py            # Utilidades (limpiar pantalla, pausar)
    ├── messages.py         # Mensajes de título, error y éxito
    ├── crud_usuarios.py    # CRUD de usuarios del sistema
    └── crud_contactos.py   # CRUD de contactos
```

---

## 📦 Entrega

La entrega se realizará de manera **individual**, mediante un enlace a un repositorio en **GitHub público** con el nombre:

```
Proyecto_Python_ApellidoNombre
```

*(o `Proyecto_Python_Apellido1Nombre1Apellido2Nombre2` donde aplique)*

El repositorio debe contener:

- `app.py` — Archivo principal de ejecución
- `modules/` — Carpeta con los módulos del sistema
- `data/agenda.json` — Archivo JSON con los datos iniciales
