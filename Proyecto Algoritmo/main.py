from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Restaurante import Restaurante
from Producto import Producto
from Cliente import Cliente
from Boleto import Boleto
from Venta_Restaurante import Venta_Restaurante
import uuid
import requests
import json


#Funcion de obtencion de la informacion proviniente del API y transformar la informacion en objetos
def api(lista_Equipos, lista_Estadios, lista_Partidos): 

    #Obtiene la info del API para Equipos
    URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    response = requests.get(URL)
    response = response.json()
    for x in response:  #Transforma la info del API para Equipos en objetos 
        nuevo_equipo = Equipo(x['id'], x['code'], x['name'], x['group']) #OBJETO
        lista_Equipos.append(nuevo_equipo)
                                                        
    #Obtiene la info del API para Estadios 
    URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    response = requests.get(URL)
    response = response.json()
    for x in response:  #Transforma la info del API para Estadios en objetos
        lista_Restaurantes =[]
        for y in x['restaurants']:
            lista_Productos = []
            for z in y['products']: 
                nuevo_producto = Producto(z['name'], z['quantity'], z['price'], z['stock'], z['adicional'])
                lista_Productos.append(nuevo_producto)
            nuevo_restaurante = Restaurante(y['name'], lista_Productos)
            lista_Restaurantes.append(nuevo_restaurante)
        nuevo_estadio = Estadio(x['id'], x['name'], x['city'], x['capacity'], lista_Restaurantes) #OBJETO
        lista_Estadios.append(nuevo_estadio)

    #Obtiene la info del API para Partidos
    URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
    response = requests.get(URL)
    response = response.json()
    for x in response: #Transforma la info del API para Partidos en objetos
        for y in lista_Equipos:
            if y.id == x['home']['id']:
                equipo_local = y
            elif y.id == x['away']['id']:
                equipo_visintates = y
        for z in lista_Estadios:
            if z.id == x['stadium_id']:
                estadio = z
        nuevo_partido = Partido(x['id'], x['number'], equipo_local, equipo_visintates, x['date'], x['group'], estadio) #OBJETO
        lista_Partidos.append(nuevo_partido)


#Funcion que extrae los elementos de la lista de objetos tipo Equipos
def extraer_paises(lista_Equipos):
    paises = set()
    for x in lista_Equipos:
        paises.add(x.name)
    return sorted(paises)


#Funcion que extrae los elementos de la lista de objetos tipo Estadios
def extraer_estadios(lista_Estadios):
    estadios = set()
    for x in lista_Estadios:
        estadios.add(x.name)
    return sorted(estadios)


#Funcion que extrae los elementos de la lista de objetos tipo Partidos
def extraer_fecha(lista_Partidos):
    #print(lista_Partidos)
    fechas = set()
    for x in lista_Partidos:
        fechas.add(x.date)
    return sorted(fechas)
    

#Funcion para partidos y estadios, muestra el submenú
def partidos_estadios(lista_Partidos, lista_Estadios, lista_Equipos): 
    print('\n 1. Buscar todos los partidos de un país \n 2. Buscar todos los partidos que se jugarán en un estadio específico\n 3. Buscar todos los partidos que se jugarán en una fecha determinada\n ')
    option = input('\nSeleccione una opcion: ')
    while not option.isnumeric() or not int(option) in range(1, 7):
        option = input('Seleccione una opcion valida: ')
        
    if option == '1':
        print('\nPaises disponibles en la EuroCopa 2024')
        paises = extraer_paises(lista_Equipos)
        for i, pais in enumerate(paises):
            print(f'{i+1}. {pais}')
        pais_buscado = input('\nIngrese el nombre del país de los partidos que quiere ver: ').lower()
        # while not pais_buscado.isalpha() or not pais_buscado in paises:
        #     print('ERROR\nEse pais no se encuentra en la lista de paises')
        #     pais_buscado = input('Ingrese un pais valido: ').lower()

        for x in lista_Partidos:
            if x.home.name.lower() == pais_buscado or x.away.name.lower() == pais_buscado:
                x.mostrar()

    elif option == '2':
        print('\nEstadios disponibles en la EuroCopa 2024')
        estadios = extraer_estadios(lista_Estadios)
        for i, estadio in enumerate(estadios):
            print(f'{i+1}. {estadio}')
        estadio_buscado = input('\nIngrese el nombre del estadio de los partidos que quiere ver: ').lower()
        # while not estadio_buscado in estadios:
        #     print('ERROR\nEse estadio no se encuentra en la lista de estadios')
        #     estadio_buscado = input('Ingrese un estadio valido: ').lower()

        for x in lista_Estadios:
            if x.name.lower() == estadio_buscado:
                for y in lista_Partidos:
                    if y.stadium_id.id == x.id:
                        y.mostrar()

    elif option == '3':
        print('\nFechas de los partidos disponibles en la EuroCopa 2024')
        fechas = extraer_fecha(lista_Partidos)
        for i, fecha in enumerate(fechas):
            print(f'{i+1}. {fecha}')
        fecha_buscada = input('\nIngrese una fecha de los partidos que quiere ver, como el siguiente formato: año-mes-dia: ')
        # while not fecha_buscada in fecha:
        #     print('ERROR\nEse estadio no se encuentra en la lista de estadios')
        #     fecha_buscada = input('Ingrese un estadio valido: ').lower()
        #partido_encontrados = []
        for x in lista_Partidos:
            if x.date == fecha_buscada:
                x.mostrar()
                #partido_encontrados.append(x)


#Funcion para obtener una cifra de numeros y letras al azar
#para el codigo unico de cada boleto
def numero_random():
# Genera un UUIDv4 aleatorio
    uuid_aleatorio = uuid.uuid4()
    # Convierte el UUID en una cadena
    uuid_str = str(uuid_aleatorio)
    # Formatea la cadena UUID (eliminar guiones y convertir a minúsculas)
    uuid_formateado = uuid_str.replace("-","").lower()
    num_random = uuid_formateado
    return num_random


# Funcion para vender entradas
#parametros> lista_Partidos, lista_Clientes, lista_Boletos
def ventas_entradas(lista_Partidos, lista_Clientes, lista_Boletos):  
        nombre = input('\nIngrese su nombre y apellido: ')
        cedula = input('\nIngrese su cedula: ')
        #validacion de la cedula
        while not cedula.isnumeric() or not len(cedula) >= len('600000') or not len(cedula) <= len('70000000') or cedula[0] == '0':
            cedula = input('Ingrese un numero de cedula valido: ')
        edad = input('\nIngrese su edad: ')
        #validacion de la edad
        while not edad.isnumeric():
            edad = input('Ingrese una edad valida: ')
        for y, x in enumerate(lista_Partidos):
            print(f'\n {y+1}.'), x.mostrar()
        partido = input('\nSeleccione el partido que desea comprar: ')
        #validacion de la seleccion del partido
        while not partido.isnumeric() or not int(partido) in range(1, len(lista_Partidos)+1):
            partido = input('Seleccione un partido valido: ')
        estadio_por_partido = lista_Partidos[int(partido) - 1]
        print('\n 1. General --> 35$\n 2. VIP --> 75$ con posibilidad de adquirir productos en los restaurantes')
        entrada = input('Seleccione el tipo de entrada que desea comprar: ')
        #validacion de la seleccion de la entrada
        while not entrada.isnumeric() or not int(entrada) in range(1, 3):
            entrada = input('Seleccione un tipo de entrada valido: ')  
        if entrada == '1':
            entrada = 'General'
            precio = 35
            estadio_por_partido.mostrar_estadio(entrada)
            capacidad = estadio_por_partido.stadium_id.capacity[0]
            print(capacidad)
        elif entrada == '2':
            entrada = 'VIP'
            precio = 75
            estadio_por_partido.mostrar_estadio(entrada)
            capacidad = estadio_por_partido.stadium_id.capacity[1]
        print('''
\n           Los puestos disponibles estan mostrados de la siguiente forma: |O|
            Los puestos ocupados estan mostrados de la siguiente forma: |X|
            Debe seleccionar un asiento disponible, ubicando su fila y su columna\n''')
        fila = input('Ingrese la fila del asiento que desea: ')
            #validacion de la seleccion de la fila
        while not fila.isnumeric() or not int(fila) in range(0,capacidad//10): 
            fila = input('Ingrese una fila valida: ')
        columna = input('Ingrese la columna del asiento que desea: ')
            #validacion de la seleccion de la columna
        while not columna.isnumeric() or not int(columna) in range(0,10): 
            columna = input('Ingrese una columna valida: ')
        #validacion de la disponibilidad del asiento
        while estadio_por_partido.check_asiento(entrada, fila, columna):
            print('\n El asiento ya esta ocupado')
            print('\n 1. Desea ver el mapa del estadio nuevamente\n 2. Salir\n')
            option = input('Ingrese la opcion que desea: ')
            #Validacion de la seleccion 
            while not option.isnumeric() or not int(option) in range(1,3):
                option = input('Ingrese una opcion valida: ')
            if option == '1':
                estadio_por_partido.mostrar_estadio(entrada) #Muestra el estadio establecido en partido
                fila = input('Ingrese la fila del asiento que desea: ')
                #validacion de la seleccion de la fila 
                while not fila.isnumeric() or not int(fila) in range(0,capacidad//10): 
                    fila = input('Ingrese una fila valida: ')
                columna = input('Ingrese la columna del asiento que desea: ')
                #validacion de la seleccion de la columna
                while not columna.isnumeric() or not int(columna) in range(0,10):  
                    columna = input('Ingrese una columna valida: ')
            elif option == '2':
                print("GRACIAS POR SU VISITA, HASTA LUEGO!")
                break
        #Designacion del codigo unico para cada entrada
        #se llama a la funcion
        codigo_unico = numero_random()
        estadio_por_partido.factura(nombre, entrada, precio, cedula, fila, columna, codigo_unico)
        compra = input('¿Desea seguir con la compra?:\n1. Si\n2. No \n ')
        #Validacion de la seleccion
        while not compra.isnumeric() or not int(compra) in range(1, 3):
            compra = input('Seleccione una opcion valida: ')  
        contador_clientes = 0
        if compra == '1':
            #Se añaden los nuevos clientes y los nuevos boletos a sus listas correspondientes
            nuevo_boleto = Boleto(cedula, estadio_por_partido, entrada,f'{fila}-{columna}', codigo_unico)
            nuevo_cliente = Cliente(nombre, cedula, edad, nuevo_boleto, entrada, codigo_unico)
            estadio_por_partido.update_asiento(entrada, fila, columna)
            lista_Clientes.append(nuevo_cliente)
            lista_Boletos.append(nuevo_boleto)
            contador_clientes += 1 
            print('\n**********COMPRA REALIZADA CON EXITO**********')
        elif compra =='2':
            print('Gracias por visitar nuestra pagina')
            pass


#Funcion para asistencia
#Funcion que comprueba que coincidan el codigo unico del usuario con algun boleto para poder entrar
#Entonces se cuenta cuanta gente entra
def asistencia(lista_Clientes):
    codigo = input('\nIngrese tu codigo unico: ')
    aux = False
    contador_clientes = 0
    for cliente in lista_Clientes:
        if cliente.codigo_unico == codigo: 
            print('\n VERIFICADO\n PUEDE ENTRAR AL ESTADIO ')
            contador_clientes += 1
            aux = True
    if aux == False:
        print('El codigo ingresado no es valido, no puede asistir')


#Funcion para buscar productos segun el tipo de producto
def busquedad_productos(cliente, lista_Venta_Restaurantes):
    #buscar en los objeto la info de restaurantes (es como una cadena de objetos)
    restaurantes = cliente.boleto.partido.stadium_id.restaurants
    #Se muestra la lista de restaurantes enumerada
    for x, restaurante in enumerate(restaurantes):
        print(f'{x+1}. {restaurante.name}')
    restaurante = input('Ingrese el restaurante en el que desea buscar: ')
    #Validacion de seleccion de restaurante
    while not restaurante.isnumeric() or not int(restaurante) in range(1, len(restaurantes)+1):
        restaurante = input('Seleccione una opcion valida: ') 
    print('\n 1. Buscar productos por nombre\n 2. Buscar productos por tipo\n 3. Buscar productos por rango de precio\n')
    option = input('\nSeleccione una opcion: ')
    #Validacion de seleccion
    while not option.isnumeric() or not int(option) in range(1, 4):
        option = input('Seleccione una opcion valida: ')

    if option == '1':
        #Se establece por el indice(que selecciono el usuario) el producto del restaurante
        productos = restaurantes[int(restaurante)-1].products
        for x, name in enumerate(productos):
            print(f'{x+1}. {name.name}')
        nombre = input('Ingrese el numero del producto del que desea ver la informacion: ')
        #Validacion de seleccion del nombre del producto
        while not nombre.isnumeric() or not int(nombre) in range(1, len(productos)+1):
            nombre = input('Seleccione una opcion valida: ')
            #mostrar el producto con el indice que selecciono el ususario
        productos[int(nombre)-1].mostrar()

    elif option == '2':
        tipo = input('''Los tipos de productos son:\n 1. plate\n 2. package\n 3. non-alcoholic\n 4. alcoholic
Ingrese el tipo del que desea ver la informacion: ''')
        #Validacion de seleccion del tipo de producto
        while not tipo.isnumeric() or not int(tipo) in range(1, 5):
            tipo = input('Seleccione una opcion valida: ')

        if tipo == '1':
            tipo = 'plate'
            #Se establece por el indice(que selecciono el usuario) el producto del restaurante
            productos = restaurantes[int(restaurante)-1].products
            for x, type in enumerate(productos):
                if type.adicional == tipo:
                    #muestra los productos de tipo PLATE
                    type.mostrar()
        elif tipo == '2':
            tipo = 'package'
            #Se establece por el indice(que selecciono el usuario) el producto del restaurante
            productos = restaurantes[int(restaurante)-1].products
            for x, type in enumerate(productos):
                if type.adicional == tipo:
                    #muestra los productos de tipo PACKAGE
                    type.mostrar()
        elif tipo == '3':
            tipo = 'non-alcoholic'
            #Se establece por el indice(que selecciono el usuario) el producto del restaurante
            productos = restaurantes[int(restaurante)-1].products
            for x, type in enumerate(productos):
                if type.adicional == tipo:
                    #muestra los productos de tipo NON-ALCOHOLIC
                    type.mostrar()
        elif tipo == '4':
            tipo = 'alcoholic'
            #Se establece por el indice(que selecciono el usuario) el producto del restaurante
            productos = restaurantes[int(restaurante)-1].products
            for x, type in enumerate(productos):
                if type.adicional == tipo:
                    #muestra los productos de tipo ALCOHOLIC
                    type.mostrar()   
    elif option == '3':
        print('\nIngrese el rango de precio')
        min = input('Ingresa el precio minimo que desea buscar (numero entero): ')
        #Validacion del numero minimo 
        while not min.isnumeric():
            min = input('Valor invalido, ingresa el precio minimo que desea buscar (numero entero): ')
        max = input('Ingresa el precio maximo que desea buscar (numero entero): ')
        #Validacion del numero maximo
        while not max.isnumeric():
            max = input('Valor invalido, ingresa el precio maximo que desea buscar (numero entero): ')
        #Validacion de la condicion de ambos numeros
        while not int(min)<int(max):
            print('EL PRECIO MINIMO DEBE SER MENOR AL PRECIO MAXIMO')
            min = input('Ingresa el precio minimo que desea buscar (numero entero): ')
            max = input('Ingresa el precio maximo que desea buscar (numero entero): ')
        #while para?
        #Se establece por el indice(que selecciono el usuario) el producto del restaurante
        productos = restaurantes[int(restaurante)-1].products
        for x, price in enumerate(productos):
            if float(price.price) >= int(min) and float(price.price) <= int(max):
                #muestra los productos dentro del rango de precio establecido
                price.mostrar()
    return True


#Funcion para comprar productos 
def compra_restaurante(cliente, lista_Venta_Restaurantes):
    #buscar en los objeto la info de restaurantes (es como una cadena de objetos)
    restaurantes = cliente.boleto.partido.stadium_id.restaurants
    #Se muestra la lista de restaurantes enumerada
    for x, restaurante in enumerate(restaurantes):
        print(f'{x+1}. {restaurante.name}')
    restaurante = input('Ingrese el resturante en el que desea comprar: ')
    #Validacion de seleccion de restaurante
    while not restaurante.isnumeric() or not int(restaurante) in range(1, len(restaurantes)+1):
        restaurante = input('Seleccione una opcion valida: ') 
    #Se establece por el indice(que selecciono el usuario) el producto del restaurante 
    productos = restaurantes[int(restaurante)-1].products
    for x, producto in enumerate(productos):
        print(f'{x+1}. {producto.name} --> precio: {producto.price}')
    producto = input('Ingrese el producto que desea comprar: ')
    #Validacion de seleccion de producto
    while not producto.isnumeric() or not int(producto) in range(1, len(productos)+1):
        producto = input('Seleccione una opcion valida: ')
    #Se establece el producto seleccionado por su indice
    producto = productos[int(producto)-1]
    #Restriccion de que nadie menor a 18 años compre: alcoholic
    if int(cliente.edad) < 18 and producto.adicional == 'alcoholic':
        print('No puede comprar productos alcoholicos por ser menor de edad')
    else:
        cantidad = input('\n Que cantidad desea comprar del producto seleccionado: ')
        #Validacion de cantidad
        while not cantidad.isnumeric(): #or not int(cantidad) in range(1, len(productos)+1): #AYUDAAAAAAAA
            cantidad = input('No hay suficientes, diga otra cantidad menor: ') 
        adicional_producto = producto.adicional
        precio_producto = producto.price
        precio_subtotal = float(precio_producto) * int(cantidad)
        #Se saca la factura del producto seleccionado
        restaurantes[int(restaurante)-1].factura(cliente.id, precio_subtotal, adicional_producto)
        compra = input('\n ¿Desea proseguir con la compra?:\n1. Si\n2. No \n ')
        #Validacion de compra
        while not compra.isnumeric() or not int(compra) in range(1, 3):
            compra = input('Seleccione una opcion valida: ')
        if compra == '1':
            nueva_venta_resturante = Venta_Restaurante(cliente.boleto.partido.stadium_id, restaurantes[int(restaurante)-1], cliente.id ,producto)  #(estadio, nombre_restaurante, id_cliente_restaurante, comida) atributos de la clase venta de restaurante
            #Se suman las ventas del restaurante
            lista_Venta_Restaurantes.append(nueva_venta_resturante)
            print('\n**********COMPRA REALIZADA CON EXTO**********')
        elif compra =='2':
            print('Gracias por visitar nuestra pagina')
            pass
        return True


#Funcion de restaurante, para buscar productos o para comprarlos
def restaurante(lista_Clientes, lista_Venta_Restaurantes): 
    print('\n 1. Buscar productos en Restaurantes \n 2. Compra de productos en restaurantes\n')
    option = input('\nSeleccione una opcion: ')
    #vallidacion de seleccion
    while not option.isnumeric() or not int(option) in range(1, 3):
        option = input('Seleccione una opcion valida: ')
#Se valida si eres cliente
    if option == '1':
        asd = False 
        cedula = input('\nIngrese su cedula: ')
        while not cedula.isnumeric() or not len(cedula) >= len('600000') or not len(cedula) <= len('70000000') or cedula[0] == '0':
                cedula = input('Ingrese un numero de cedula valido: ')
        for x in lista_Clientes:
            if x.id == cedula:
                asd = busquedad_productos(x, lista_Venta_Restaurantes) #lo que significa cada parametro en la funcion (cliente, lista_Venta_Restaurantes)
        if asd == False:
            print('No se encontro el cliente en la lista de clientes VIP')
#Ademas si eres cliiente, tienes que ser VIP
    elif option =='2':
        asd = False
        cedula = input('\nIngrese su cedula: ')
        while not cedula.isnumeric() or not len(cedula) >= len('600000') or not len(cedula) <= len('70000000') or cedula[0] == '0':
                cedula = input('Ingrese un numero de cedula valido: ')
        for x in lista_Clientes:
            if x.id == cedula and x.tipo_entrada == 'VIP':
                asd = compra_restaurante(x, lista_Venta_Restaurantes)
        if asd == False:
            print('No se encontro el cliente en la lista de clientes VIP')


#Funcion de estadistica, muestra el submenú
def estadisticas():
    print('\n 1. Promedio de gasto de un cliente VIP en un partido (ticket + restaurante) \n 2. Tabla con la asistencia a los partidos de mejor a peor\n 3. Partido con mayor asistencia\n 4. Partido con mayor boletos vendidos\n 5. Top 3 productos más vendidos en el restaurante\n 6. Top 3 de clientes (clientes que más compraron boletos)\n 7. Graficos con estadisticas\n')
    option = input('Seleccione una opcion: ')
    while not option.isnumeric() or not int(option) in range(1, 7):
        option = input('Seleccione una opcion valida: ')

    if option == "1":
        print('Promedio de gasto de un cliente VIP en un partido (ticket + restaurante)')

    elif option == "2":
        print('Tabla con la asistencia a los partidos de mejor a peor')
    
    elif option == "3":
        print('Partido con mayor asistencia')

    elif option == "4":
        print('Partido con mayor boletos vendidos')

    elif option == "5":
        print('Top 3 productos más vendidos en el restaurante')

    elif option == "6":
        print('Top 3 de clientes (clientes que más compraron boletos)')

    elif option == "6":
        print('Graficos con estadisticas')

#Muestra el menú
#Realiza todo 
def main():   
    lista_Equipos = []
    lista_Estadios = []
    lista_Partidos = []
    lista_Boletos = []
    lista_Clientes = []
    lista_Venta_Restaurantes = []

    api(lista_Equipos, lista_Estadios, lista_Partidos)
    print('\n***************************************\nBIENVENIDA A LA EUROCOPA ALEMANIA 2024\n***************************************\n')

    while True:
        print('\n 1. Partidos y estadios\n 2. Venta de entradas\n 3. Asistencia a los partidos\n 4. Restaurante\n 5. Estadisticas\n 6. Salir\n')
        option = input('Seleccione una opcion: ')
        while not option.isnumeric() or not int(option) in range(1, 7):
            option = input('Seleccione una opcion valida: ')

        if option == '1':
            partidos_estadios(lista_Partidos, lista_Estadios, lista_Equipos)

        elif option == '2':
            ventas_entradas(lista_Partidos, lista_Clientes, lista_Boletos)

        elif option == '3':
            asistencia(lista_Clientes)

        elif option == '4':
            restaurante(lista_Clientes, lista_Venta_Restaurantes) 

        elif option == '5':
            estadisticas()

        elif option == '6':
            print('Hasta luego!! Gracias por visitar la Euro 2024')
            txt(lista_Partidos,lista_Equipos, lista_Estadios, lista_Boletos, lista_Clientes, lista_Venta_Restaurantes)
            break 


#GUARDAR INFORMACION EN ARCHIVO.TXT
def txt(lista_Partidos,lista_Equipos, lista_Estadios, lista_Boletos, lista_Clientes, lista_Venta_Restaurantes):

    #Cada With open abre un archvo que esta en la carpeta txt. 
    #Transforma los objetos en diccionarios para guardarlos en los txt (EN CADA CLASE)
    with open('txt/Partidos.txt', 'w') as w:
        for x in lista_Partidos: 
            dicc = {'id': x.id,          
                    'number': x.number,
                    'home': x.home.name,
                    'away': x.away.name,
                    'date': x.date,
                    'group': x.group,
                    'stadium_id': x.stadium_id.name,
                    'asiento_general': [], 
                    'asiento_vip': []} 

            json_data = json.dumps(dicc)
                #Escriba la cadena en el archivo con una línea mas
            w.write(json_data + '\n')

    with open('txt/Equipos.txt', 'w') as w:
        for x in lista_Equipos:
            dicc = {'id': x.id,
                    'code': x.code,
                    'name': x.name,
                    'group': x.group}
            json_data = json.dumps(dicc)
                #Escriba la cadena en el archivo con una línea mas
            w.write(json_data + '\n')

    with open('txt/Estadios.txt', 'w') as w:
        for x in lista_Estadios:
            dicc = {'id': x.id,
                    'name':x.name,
                    'city': x.city,
                    'capacity':x.capacity,
                    'restaurants': []}
            json_data = json.dumps(dicc)
                #Escriba la cadena en el archivo con una línea mas
            w.write(json_data + '\n')

main()