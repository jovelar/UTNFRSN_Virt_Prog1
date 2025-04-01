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


actividad4()