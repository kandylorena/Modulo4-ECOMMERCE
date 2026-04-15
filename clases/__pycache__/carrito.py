from producto import Producto

class Carrito:
    def __init__(self):
        self.items = {}

    def __str__(self):
        return f"{self.items}"

    def agregar(self, producto, cantidad):
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] =cantidad

    def ver_carrito(self):
        total = 0
        for p,c in self.items.items():
            subtotal = p.precio * c
            total += subtotal
            print(f"{p.nombre} - cantidad {c} - subtotal{subtotal}")
        print(f"total de la compra: {total}")



    def total(self):
        pass

    def vaciar(self, producto):
        self.items.clear()

#para probar
p1 = Producto(1, "computador","tecnologia", 100)
p2 = Producto(2, "computador","tecnologia", 100)
p3 = Producto(3, "computador","tecnologia", 100)
p4 = Producto(4, "computador","tecnologia", 100)
carrito = Carrito()
carrito.agregar(p1, 2)
carrito.agregar(p1, 2)
carrito.agregar(p2, 2)
carrito.agregar(p3, 2)
carrito.agregar(p4, 2)
carrito.ver_carrito()
carrito.vaciar(p2)
