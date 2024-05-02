import os

def obtener_nombre_elemento(carpeta, indice):
    # Listar todos los archivos y carpetas en la carpeta especificada
    elementos = os.listdir(carpeta)
    # Ordenar los elementos alfabéticamente
    elementos.sort()
    
    # Comprobar si el índice está dentro del rango válido
    if 0 <= indice < len(elementos):
        return elementos[indice]
    else:
        return "Índice fuera de rango"

# Ruta de la carpeta que quieres explorar
ruta_carpeta = 'ruta/a/tu/carpeta'

# Índice del elemento que quieres obtener
indice_elemento = 3  # Cambia este número al índice que necesitas

#-------------------------------------------------------------
print("Inicio")
# Llamar a la función y mostrar el resultado
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 0)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 0)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 1)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 1)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------
print("1000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 500)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 500)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 501)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 501)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------
print("2000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 1000)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 999)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 1000)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 1000)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------
print("3000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 1500)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 1499)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 1501)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 1500)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------

print("4000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 2000)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 1999)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 2001)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 2000)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------

print("5000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 2500)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 2499)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 2501)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 2500)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------

print("6000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 3000)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 2999)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 3001)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 3000)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------

print("7000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 3500)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 3499)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 3501)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 3500)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------

print("8000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 4000)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 3999)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 4001)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 4000)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------

print("9000")
nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 4500)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 4499)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/1', 4501)
print(nombre_elemento_1)

nombre_elemento_1 = obtener_nombre_elemento('INFORME_2/FOTOS/8362/0', 4500)
print(nombre_elemento_1)
print(' ')

#-------------------------------------------------------------

