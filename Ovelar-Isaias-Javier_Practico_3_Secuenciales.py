
from statistics import mode,median,mean
from datetime import datetime
import random

def actividad1():
    edad = int(input("Ingrese su edad: "))
    if edad>=18:
        print("Usted es mayor de edad!")


def actividad2():
    nota = int(input("Ingrese su nota: "))
    if nota >=6:
        print("Aprobado!")
    else:
        print("Desaprobado!")

def actividad3():
    numero = int(input("Ingrese un numero par: "))
    if numero % 2==0:
        print("el numero ingresado es par")
    else:
        print("Por favor, ingrese un numero par")

def actividad4():
    edad = int(input("Ingrese su edad: "))
    if edad <12:
        print("Nino")
    elif edad>=12 and edad<18:
        print("Adolescente")
    elif edad>=18 and edad<30:
        print("Adulto joven")
    else:
        print("Adulto")


def actividad5():
    password = input("Ingrese una contrasena de entre 8 y 14 caracteres: ")
    if len(password)>=8 and len(password)<=14:
        print("Ha ingresado una contrasena correcta")
    else:
        print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")

def actividad6():
    numeros_aleatorios = [random.randint(1,100)for i in range(50)]

    #calculando la media
    media=mean(numeros_aleatorios)

    #Calculando la mediana, .median() realiza la division entre los numeros del medio en caso de que el arreglo sea par
    #por ello el metodo no es util en este caso y debemos determinar el punto medio de arreglo de otra manera
    pos_medio=0
    if len(numeros_aleatorios)%2 ==0:
        pos_medio=(len(numeros_aleatorios)//2)-1
    else:
        #Division entera
        pos_medio=len(numeros_aleatorios)//2
    
    #La lista deberia estar ordenada primero
    numeros_aleatorios.sort()
    mediana=numeros_aleatorios[int(pos_medio)]

    #Calculando la moda
    moda=mode(numeros_aleatorios)

    #Monstrando informacion para corroborar la funcion

    print("lista ordenada:")
    ordenada=numeros_aleatorios
    ordenada.sort()
    print(ordenada)

    print(f"Media:{media}, mediana: {mediana}, moda: {moda}")

    if media > mediana and mediana > moda:
        print("Sesgo positivo")
    elif media < mediana and mediana < moda:
        print("Sesgo negativo")
    elif media == mediana and mediana == moda:
        print("Sin Sesgo")

def actividad7():
    palabra = input("Ingrese una palabra: ")
    vocales = ('A','a','E','e','I','i','O','o','U','u') #Tupla que contiene vocales
    if palabra.endswith(vocales):
        palabra=palabra + '!'
    print(palabra)


#Solucion mas al estilo 'C', es decir, iterando con un while en un string
def buscaVocal(letra):
    palabra = "AaEeIiOoUu"
    encontrado=False
    posicion=0

    while posicion<len(palabra) and encontrado==False:
        if palabra[posicion]==letra:
            encontrado=True
        posicion += 1
    return encontrado


def actividad7_IT():
    palabra = input("Ingrese una palabra: ")
    termina_en_vocal=buscaVocal(palabra[len(palabra)-1])
    if termina_en_vocal == True:
        palabra=palabra + '!'
    print(palabra)

def actividad8():
    nombre = input("Ingrese su Nombre: ")
    valido = False

    #Mientras no se ingrese una opcion valida, no se podra salir del bucle
    while valido ==False:
        opcion=""
        print("Ingrese una opcion: ")
        print("1- Mostrar su nombre en Mayusculas ")
        print("2- Mostrar su nombre en minusculas ")
        print("3- Mostar su nombre solo con la primera letra mayuscula ")
        opcion=input()
        if opcion!='1' and opcion!='2' and opcion!='3':
            print("Opcion invalida, solo 1 2 o 3")
        else:
            valido=True
            if opcion=='1':
                print(nombre.upper())
            elif opcion=='2':
                print(nombre.lower())
            elif opcion=='3':
                print(nombre.capitalize())

def actividad9():
    magnitud = float(input("Ingrese la magnitud del Sismo: "))
    if magnitud >=7:
        print("Extremo")
    if 7 > magnitud >=6:
        print("Muy fuerte")
    if 6> magnitud >=5:
        print("Fuerte")
    if 5 > magnitud >=4:
        print("Moderado")
    if 4 > magnitud >=3:
        print("Leve")
    if magnitud <3:
        print("Muy leve")


def actividad10():
    hemisferio=""
    hemisvalido=False
    while hemisvalido is False:
        print("1- Sur \n 2-Norte")
        hemisferio=input("Ingrese en cual hemisferio ud se encuentra ")
        if hemisferio!='1' and hemisferio.lower()!="sur" and hemisferio!='2' and hemisferio.lower()!="norte":
            print("Opcion invalida")
        else:
            hemisvalido=True
            if hemisferio=='1' or hemisferio=="sur":
                hemisferio='1'
            else:
                hemisferio='2'
    
    stringFecha=""
    fechaValida=False
    while fechaValida is False:
        stringfecha = input("Ingrese una fecha en el formato DD-MM-AA") #https://docs.python.org/es/3.13/library/datetime.html
        try:                                                            #https://docs.python.org/es/3.13/tutorial/errors.html
            stringfecha=datetime(stringFecha,"%%d-%m-%y")
            fechaValida=True
        except ValueError:
            print("Fecha invalida!")
            fechaValida=False
    
    print(stringFecha)

actividad10()
    