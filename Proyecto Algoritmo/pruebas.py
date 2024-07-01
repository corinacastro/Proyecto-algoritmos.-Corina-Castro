

# x = [374,424]

# fila = -(-x[0] // 10) 
# columna = 10

# #fila1 = -(-fila // 1)

# print(fila)
# #print(fila1)

# #asiento = round((fila1 - fila)*10,2)
# #print(asiento)

# y =[
#     [0,1,2,3,4,5,6,7],
#     [8,9,10,11,12,13,14,15]
# ]

import uuid
def numero_random():
# Genera un UUIDv4 aleatorio
    uuid_aleatorio = uuid.uuid4()
    # Convierte el UUID en una cadena
    uuid_str = str(uuid_aleatorio)
    # Formatea la cadena UUID (eliminar guiones y convertir a minúsculas)
    uuid_formateado = uuid_str.replace("-","").lower()
    num_random = uuid_formateado
    return num_random

y=numero_random()
print(y)

































# matriz = [[0 for _ in range(10)] for _ in range(10)]

# # Imprimir encabezado de columnas
# print("  ", end='')
# for j in range(10):
#     print(j, end=' ' if j < 9 else '\n')  # Agregar salto de línea al último número de cada columna

# # Imprimir matriz con filas identificadas por el abecedario
# for i, fila in enumerate(matriz):
#     print(chr(65 + i), end=' ')  # Imprimir letra correspondiente a la fila
#     for j, elemento in enumerate(fila):
#         if elemento == 0:
#             print("|O|", end=' ')
#         elif elemento == 1:
#             print("|X|", end=' ')
#         if (j + 1) % 10 == 0:
#             print(" ", end='  ')  # Agregar espacio en blanco al final de cada fila
#             print(flush=True)  # Forzar la impresión de los datos antes de que se complete la línea
#     print()




# matriz = [[0 for _ in range(10)] for _ in range(10)]
# # en los das llamo a los numeros de la caacdad de cada estado 

# for i, fila in enumerate(matriz):
#     for j, elemento in enumerate(fila):
#         if elemento == 0:
#             print("|O|", end=' ')
#         elif elemento == 1:
#             print("|X|", end=' ')
#         if (j + 1) % 10 == 0:
#             print()
#     print()

