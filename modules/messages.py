def mostrarTitulo(titulo):
    """
    Muestra el titulo centrado y decorado.
    """
    print("="*50)
    print(titulo.center(50))
    print("="*50)
    print()

def mostrarError(mensaje):
    """
    Muestra un mensaje de error decorado.
    """
    print(f"\n[ERROR] {mensaje}")
    
def mostrarExito(mensaje):
    """
    Muestra un mensaje de éxito decorado.
    """
    print(f"\n[ÉXITO] {mensaje}")
    