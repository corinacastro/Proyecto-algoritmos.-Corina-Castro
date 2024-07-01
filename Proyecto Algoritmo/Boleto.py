
class Boleto():
    def __init__(self, id_cliente, partido, tipo_entrada, asiento, codigo_unico):
        self.id_cliente = id_cliente
        self.partido = partido
        self.tipo_entrada = tipo_entrada
        self.asiento = asiento
        self.codigo_unico = codigo_unico

    def mostrar(self): #Funcion para mostrar boletos
        print(f'''
              Cedula del cliente: {self.id_cliente}
              Partido que selecciono el cliente: {self.partido}
              Tipo de entrada: {self.tipo_entrada}
              Asiento que selecciono el cliente: {self.asiento}''')
    
    

