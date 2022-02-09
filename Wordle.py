from string import ascii_lowercase
import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
def mostrarPalabras():
    palabrasOrdenadas = {k: v for k, v in sorted(palabrasPuntuacion.items(), key=lambda item: item[1], reverse=True)}
    mostrarNPalabras(palabrasOrdenadas,15)
def eliminarPalabras(palabrasEliminar):
    for palabra in palabrasEliminar:
        if palabra in palabrasPuntuacion.keys():
            del palabrasPuntuacion[palabra]
def recalcular():
    calcularGris()
    calcularAmarillo()
    calcularVerde()
def calcularGris():
    palabrasEliminar = []
    for palabra in palabrasPuntuacion.keys():
        for letra in gris:
            if letra in palabra:
                palabrasEliminar.append(palabra)
    eliminarPalabras(palabrasEliminar)
def calcularAmarillo():
    palabrasEliminar = []
    for palabra in palabrasPuntuacion.keys():
        for letra, pos in amarillo:
            if (letra in palabra and palabra[pos] == letra) or letra not in palabra:
                palabrasEliminar.append(palabra)
    eliminarPalabras(palabrasEliminar)
def calcularVerde():
    palabrasEliminar = []
    for palabra in palabrasPuntuacion.keys():
        for letra, pos in verde:
            if letra not in palabra or palabra[pos] != letra:
                palabrasEliminar.append(palabra)
    eliminarPalabras(palabrasEliminar)
def primeraOpcion():
    palabrasOrdenadas = {k: v for k, v in sorted(palabrasPuntuacion.items(), key=lambda item: item[1], reverse=True)}
    palabrasBorrar = []
    ultimoValor = 0
    for p in palabrasOrdenadas.keys():
        if truncate(palabrasOrdenadas[p],10) == ultimoValor:
            palabrasBorrar.append(p)
        else:
            ultimoValor = truncate(palabrasOrdenadas[p],10)
    for pb in palabrasBorrar:
        del palabrasOrdenadas[pb]
    mostrarNPalabras(palabrasOrdenadas,10)

def mostrarNPalabras(lista,numero):
    cont = 0
    for p in lista.keys():
        print(p + " --> " + str(lista[p]))
        cont += 1
        if cont >= numero:
            break

f = open("Diccionario")
cadena = f.read()
f.close()
cadena = cadena.replace("\\xf1", "ñ")
cadena = cadena.replace('"', "")
separador = ","
diccionario = cadena.split(separador)


#Inicializamos letras
letrasPuntuacion = {'a':0}

#Vemos porcentaje de letras
for p in diccionario:
    for l in p:
        letrasPuntuacion[l] = letrasPuntuacion.get(l, 0) + 1
for l in letrasPuntuacion.keys():
    letrasPuntuacion[l] = letrasPuntuacion.get(l, 0) / len(diccionario)


#Asignamos puntuación a las palabras
palabrasPuntuacion = {'ababa':0}

for p in diccionario:
    punt = 0
    letrasUsadas = []
    for i in range(len(p)):
        l = p[i]
        if (l not in letrasUsadas):
            punt += letrasPuntuacion[l]
        letrasUsadas.append(l)
    palabrasPuntuacion[p]= palabrasPuntuacion.get(p, 0) + punt / len(p)

primeraOpcion()

while(True):
    #A partir de aqui tenemos resultados
    gris = []
    amarillo = []
    verde = []

    print("Palabra introducida:")
    palabraIntroducida = input()

    print("De que color es cada letra: gris(g), amarilla(a), verde(v)")
    posicion = 0
    for l in palabraIntroducida:
        color = ""
        while color not in ['g','a','v']:
            print("Color de " + l + ": ", end="")
            color = input()
        if (color=='g'):
            gris.append(l)
        elif (color=='a'):
            amarillo.append([l,posicion])
        elif (color == 'v'):
            verde.append([l, posicion])
        posicion+=1

    recalcular()
    mostrarPalabras()





