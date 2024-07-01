
class Restaurante():
    def __init__(self, name, products):
        self.name = name 
        self.products = products

    def mostrar(self): #Funcion para mostrar miembros del equipo
        print(f'''
              Nombre del restaurante: {self.name}
              Productos: {self.products}''')
        
    def factura(self, cedula, precio_subtotal, adicional_producto):
        #Algoritmo para establecer si la cedula es un numero perfecto
        es_perfecto = ''
        suma_divisores = 0
        for i in range(1, int(cedula)):
            if int(cedula) % i == 0:
                suma_divisores += i
        if suma_divisores == int(cedula):
            es_perfecto = True
            descuento = 0.15 * float(precio_subtotal)
        else:
            es_perfecto = False
            descuento = 0
        iva = round(0.16 * float(precio_subtotal),2)
        print(f'''
              ***** FACTURA *****
            Nombre del producto: 
            Tipo de producto: {adicional_producto}
            Precio de los productos: {precio_subtotal}$
            Descuento:{descuento}
            IVA (%16): {iva}
            Precio Total: {float(precio_subtotal)-descuento+iva}$
            ''')

