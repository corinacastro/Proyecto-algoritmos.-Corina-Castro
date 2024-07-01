
class Cliente():
    def __init__(self, name, id, edad, boleto, tipo_entrada, codigo_unico):
        self.name = name
        self.id = id
        self.edad = edad 
        self.boleto = boleto
        self.tipo_entrada = tipo_entrada 
        self.codigo_unico = codigo_unico
        self.gasto = 0

    def mostrar(self): #Funcion para mostrar datos del cliente
        print(f'''
              Nombre: {self.name}
              Cedula: {self.id}
              Edad: {self.edad}
              Ticket del partido: {self.boleto}
              Tipo de entrada: {self.tipo_entrada}''')
        