import os
import json

"""
Ruta donde se encuentra el archivo JSON.
"""
RUTA_ARCHIVO = "data/agenda.json"

def cargarDatos():
    """
    Cargar los datos desde el archivo JSON.
    Si no existen o hay un error, devuelve una lista vacía.
    """
    if not os.path.exists(RUTA_ARCHIVO):
        return {"usuarios":[], "contactos":[]}
    
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return {"usuarios":[], "contactos":[]}
    
def guardarDatos(datos):
    """ 
    Guarda el diccionario en el archivos JSON.
    """
    try:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            """
            ident=4 para que el JSON se vea más legible
            """
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        