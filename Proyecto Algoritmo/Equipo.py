
class Equipo():
    def __init__(self, id, code, name, group):
        self.id = id 
        self.code = code
        self.name = name
        self.group = group

    def mostrar(self): #Funcion para mostrar miembros del equipo
        print(f'''
              Nombre del país: {self.name}
              Codigo: {self.code}
              Grupo: {self.group}''')
        