import os

def limpiarPantalla():
    """
    Limpia la pantalla del sistema dependiendo del sistema operativo.
    """
    if os.name == "nt":  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/Mac
        os.system('clear')
    
def pausar():
    """
    Hace una pausa hasta que el usuario presione Enter.
    """
    input("Presiona Enter para continuar...")
    