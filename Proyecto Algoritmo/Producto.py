
class Producto():
    def __init__(self, name, quantity, price, stock, adicional):
        self.name = name 
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional

    def mostrar(self): #Funcion para mostrar miembros del equipo
        print(f'''
              Nombre del producto: {self.name}
              Cantidad del producto: {self.quantity}
              Precio del producto: {self.price}
              Inventario: {self.stock}
              Adicional: {self.adicional}''')
