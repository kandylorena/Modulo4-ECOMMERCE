class Producto:
    def __init__(self, id, nombre, categoria,precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"el id del producto es : {self.id} - {self.nombre} - {self.categoria} - {self.precio}"
    
    #ordena para q muestre el dicc ordenado con sus nombres
    def __repr__(self):
        return self.nombre
    
producto1 = Producto(1,"computador","tecnologia",1000)

print(producto1)