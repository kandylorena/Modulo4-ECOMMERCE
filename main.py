from clases.catalogo import Catalogo
from clases.usuarios import *
from clases.producto import Producto

class Tienda:
    def __init__(self):
        self.catalogo = Catalogo()
        self.cargar_datos()
    
    def cargar_datos(self):
        self.catalogo.agregar_producto(Producto)