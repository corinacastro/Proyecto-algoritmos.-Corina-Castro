from Estadio import Estadio

class Partido():
    def __init__(self, id, number, home, away, date, group, stadium_id):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium_id = stadium_id
        self.asiento_general = []  
        self.asiento_vip = []  
        self.generar_asiento()


    def mostrar(self):  # Funcion para mostrar partidos
        print(f'''
              Local: {self.home.name}
              Visitante: {self.away.name}
              Fecha: {self.date}
              Grupo: {self.group}
              Numero: {self.number}
              ID del estadio : {self.stadium_id.name}''')

    def generar_asiento(self):
        column_number = 10
        general = self.stadium_id.capacity[0]
        vip = self.stadium_id.capacity[1]
        filas_general = -(-general // 10)
        filas_vip = -(-vip // 10)

        remaining_general = general % 10
        remaining_vip = vip % 10

        # Creacion de una lista dinamica ara self.asiento_general
        self.asiento_general = [[False for _ in range(column_number)]
                                for _ in range(filas_general)]

        # Creacion de una lista dinamica para self.asiento_vip
        self.asiento_vip = [[False for _ in range(column_number)]
                            for _ in range(filas_vip)]

        # Borrar los ultimos asientos de la ultima fila en caso de que no existan (Como NONE)
                    #GENERAL
        for i in range(filas_general):
            for j in range(column_number):
                if i == filas_general - 1 and j >= remaining_general:
                    self.asiento_general[i][j] = None
                    #VIP
        for i in range(filas_vip):
            for j in range(column_number):
                if i == filas_vip - 1 and j >= remaining_vip:
                    self.asiento_vip[i][j] = None

    def update_asiento(self, entrada, fila, columna):
        if entrada == 'General':
            self.asiento_general[int(fila)][int(columna)] = True
        elif entrada == 'VIP':
            self.asiento_vip[int(fila)][int(columna)] = True
    
    def check_asiento(self, entrada, fila, columna):
        if entrada == 'General':
            if self.asiento_general[int(fila)][int(columna)]:  #Asiento ocupado 
                return True
            else:
                return False
        elif entrada == 'VIP':
            if self.asiento_vip[int(fila)][int(columna)]:
                return True
            else:
                return False

    def mostrar_estadio(self, entrada):
        if entrada == 'General':
            self.mostrar_estadio_general(entrada)
        elif entrada == 'VIP':
            self.mostrar_estadio_vip(entrada)

    def mostrar_estadio_general(self, entrada):
        self.mostrar_asientos(entrada, self.asiento_general)

    def mostrar_estadio_vip(self, entrada):
        self.mostrar_asientos(entrada, self.asiento_vip)

    def mostrar_asientos(self, entrada, asientos):
        print(f'''
                            MAPA DEL ESTADIO
                           ***entrada {entrada}***
    ''')
        print('\n    0   1   2   3   4   5   6   7   8   9')
        contador = 0
        for fila in asientos:
            if not contador == 0:
                print()
            if contador < 10:
                print(contador, end='  ')
            else:
                print(contador, end=' ')
            for asiento in fila:
                if asiento is False:
                    print('|O|', end=' ')
                elif asiento is None:
                    print(' ', end=' ')
                else:
                    print('|X|', end=' ')
            contador += 1


    def factura(self, name, tipo_entrada, precio, cedula, fila, columna, codigo_unico):
        #Algoritmo para establecer si la cedula es un numero vampiro
        es_vampiro = ""
        digitos = list(str(cedula))
        num_digitos = len(digitos)

        # Comprobación de los factores
        for i in range(1, int(int(cedula)**0.5)+1):
            if int(cedula) % i == 0:
                factor1 = str(i)
                factor2 = str(int(cedula) // i)
                factores = factor1 + factor2

                # Comprobación de la permutación
                if sorted(digitos) == sorted(factores) and len(factor1) == len(factor2):
                    es_vampiro = True
                    descuento = 0.5 * precio
                else:    
                    es_vampiro = False
                    descuento = 0 * precio
        iva = round(0.16 * precio,2)

        print(f'''
              ***** FACTURA *****
            Nombre del cliente: {name}
            Tipo de entrada: {tipo_entrada}
            Precio de la entrada: {precio}$
            Descuento:{descuento}
            IVA (16%): {iva}
            Total: {precio-descuento+iva}
            Asiento: {fila} - {columna}
            Codigo Unico: {codigo_unico}
            ''')
