from catalogo import Catalogo
from producto import Producto
from carrito import Carrito

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def menu(self):
        pass

class Admin(Usuario):
    def menu(self, catalogo):
        while True:
            print("menu admin")
            print("1- Listar catalogo")
            print("2- Crear producto en catalogo")
            print("3- Actualizar producto en catalogo")
            print("4- Eliminar producto en catalogo")
            print("5- Guardar en archivo")

            opcion = input("ingrese su opcion")
            if opcion == "1":
                catalogo.listar_catalogo()
                
            elif opcion == "2":
                id = input("id de producto")
                nombre = input("nombre del producto")
                categoria = input("categoria del producto")
                precio = input("precio del producto")
                catalogo.agregar_producto(Producto(id, nombre, categoria, precio))

            elif opcion == "3":
                pass
            elif opcion == "4":
                id = input("id a borrar")
                catalogo.eliminar_producto(id)
            elif opcion == "5":
                catalogo.guardar_catalogo()
            else:
                print("pon una opcion valida")

usuario_admin = Admin("Kandy")
catalogo = Catalogo()
usuario_admin.menu(catalogo)




class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.carrito = Carrito()

    def menu(self, catalogo):
        while True:
            print("menu cliente")
            print("1- Ver catalogo")
            print("2- Agregar al carrito")
            print("3- Ver carrito ")
            print("4- Comprar")

            opcion = input("ingrese su opcion")
            if opcion == "1":
                catalogo.listar_catalogo()
                
            elif opcion == "2":
                id = input("ingrese el id del producto")
                cantidad = input("cantidad")
                producto = catalogo.buscar_por_id(id)
                self.carrito.agregar(producto, cantidad)

            elif opcion == "3":
                self.carrito.ver_carrito()

            elif opcion == "4":
                self.carrito.pagar()
                self.carrito.vaciar()