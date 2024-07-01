
class Estadio():
    def __init__(self, id, name, city, capacity, restaurants):
        self.id = id
        self.name = name
        self.city = city 
        self.capacity = capacity
        self.restaurants = restaurants 

    def mostrar(self): #Funcion para mostrar estadios
        print(f'''
              Nombre del estadio: {self.name}
              Ubicacion del estadio: {self.city}
              ID del estadio: {self.id}
              Capacidad del estadio: {self.capacity} asientos
              Restaurantes: ''')
        for restaurant in self.restaurants:
            print(f'''
                            {restaurant.name}''')

        