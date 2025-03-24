def a1():
    print("hola mundo!")

def a2():
    nombre=input("ingrese su nombre: ")
    print(f"hola {nombre}")

def a3():
    nombre = input("Ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese s lugar de residencia")
    print(f"Hola soy {apellido} {nombre} tengo {edad} anios y vivo en {residencia}")

def a4():
    radio = input("Ingrese el radio del circulo: ")
    print(f"El area de un circulo con radio {radio} es de {3.14*(float(radio)**2)} y su perimetro es de {2*3.14*float(radio)}")

def a5():
    tiempo = input("Ingrese el tiempo en segundos: ")
    print(f"El tiempo ingresado equivale a {float(tiempo)/3600} horas ")

def a6(): 
    numero = input("Ingrese un numero: ")
    for i in range(1,10,1):
        print(f"{numero} x {i} = {i*int(numero)} ")

def a7(): 
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    print(f"{numero1} + {numero2} = {numero1+numero2}")
    print(f"{numero1} - {numero2} = {numero1-numero2}")
    print(f"{numero1} * {numero2} = {numero1*numero2}")
    print(f"{numero1} / {numero2} = {numero1/numero2}")

def a8():
    altura=int(input("Ingrese su altura en centimetros: "))
    peso=float(input("Ingres su peso en kilos: "))
    print(f"Su IMC es de {peso/((altura/100)**2)}")

def a9():
    tempCelcius=float(input("Ingrese la temperatura en celcius: "))
    print(f"La temperatura ingresada ({tempCelcius}) equivale a {(9/5*tempCelcius)+32} grados Fahrenheit")

def a10():
