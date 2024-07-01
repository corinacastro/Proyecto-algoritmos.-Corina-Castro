
class Venta_Restaurante():
    def __init__(self, estadio, restaurante, id_cliente_restaurante, comida):
        self.estadio = estadio
        self.restaurante = restaurante
        self.id_cliente_restaurante = id_cliente_restaurante
        self.comida = comida

    def mostrar(self): #Funcion para mostrar boletos
        print(f'''
            El estadio donde se encuentra el restaurante: {self.estadio}
            Nombre del restaurante: {self.restaurante}
            Cedula del cliente del restaurante: {self.id_cliente_restaurante}
            Comida comprada: {self.comida}''')