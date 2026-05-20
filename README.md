# 📒 Gestor de Contactos — ACME Solutions

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Datos-JSON-orange?style=for-the-badge&logo=json&logoColor=white)
![License](https://img.shields.io/badge/Licencia-Educativa-green?style=for-the-badge)

Sistema de gestión de contactos desarrollado en **Python** para la empresa ACME Solutions. Permite registrar, consultar, buscar, actualizar y eliminar contactos de forma centralizada, con persistencia de datos en formato JSON y control de acceso por roles.

---

## 🚀 Características principales

- 🔐 **Sistema de Login** con control de intentos (máximo 3)
- 👤 **Gestión de usuarios** (solo para administradores)
- 📇 **CRUD completo de contactos** (Crear, Leer, Buscar, Actualizar, Eliminar)
- 💾 **Persistencia de datos** en archivo JSON
- 🖥️ **Interfaz de consola** limpia y estructurada

---

## 📁 Estructura del proyecto

```
Proyecto_Python_AmadoManuel/
│
├── app.py                  # Punto de entrada principal
├── Proyecto.md             # Enunciado del taller
├── data/
│   └── agenda.json         # Base de datos en formato JSON
└── modules/
    ├── core.py             # Carga y guardado del archivo JSON
    ├── utils.py            # Utilidades generales (limpiar pantalla, pausar)
    ├── messages.py         # Mensajes de título, error y éxito
    ├── crud_usuarios.py    # Gestión de usuarios del sistema
    └── crud_contactos.py   # Gestión de contactos
```

---

## ▶️ Cómo ejecutar el proyecto

### Requisitos

- Python 3.x instalado en el sistema
- No requiere librerías externas (solo módulos estándar de Python)

### Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Proyecto_Python_AmadoManuel.git
   cd Proyecto_Python_AmadoManuel
   ```

2. Ejecuta el archivo principal:
   ```bash
   python app.py
   ```

3. Inicia sesión con las credenciales del administrador por defecto:

   | Campo      | Valor                   |
   |------------|-------------------------|
   | E-mail     | admin@acmesolutions.com |
   | Contraseña | admin123                |

---

## 🧭 Menú del sistema

```
==========================================
         ACME SOLUTIONS - BIENVENIDO
==========================================

1. Gestión de contactos
2. Gestión de usuarios     ← solo visible para administradores
3. Salir del sistema
```

### Submenú — Gestión de Contactos

| Opción | Acción |
|--------|--------|
| 1 | Registrar nuevo contacto |
| 2 | Listar todos los contactos |
| 3 | Buscar contacto (por ID, nombre o tipo) |
| 4 | Actualizar contacto |
| 5 | Eliminar contacto |
| 6 | Volver al menú principal |

### Submenú — Gestión de Usuarios *(solo admin)*

| Opción | Acción |
|--------|--------|
| 1 | Registrar nuevo usuario |
| 2 | Listar usuarios |
| 3 | Volver al menú principal |

---

## 💾 Estructura del archivo JSON

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

---

## 🛡️ Roles del sistema

| Rol | Acceso |
|-----|--------|
| `admin` | Gestión de contactos + Gestión de usuarios |
| `usuario` | Solo gestión de contactos |

---

## 📦 Módulos

| Archivo | Responsabilidad |
|---------|----------------|
| `app.py` | Login, menú principal y punto de entrada |
| `core.py` | `cargarDatos()` y `guardarDatos()` sobre `agenda.json` |
| `utils.py` | `limpiarPantalla()` y `pausar()` |
| `messages.py` | `mostrarTitulo()`, `mostrarError()`, `mostrarExito()` |
| `crud_usuarios.py` | Crear y listar usuarios del sistema |
| `crud_contactos.py` | CRUD completo de contactos |

---

## 👨‍💻 Autor

**Amado Manuel**  
Proyecto académico
