#Funciones
#Teoría
'''Las funciones ayudan a reciclar código.
Su sintaxis empieza con la palabra def
Por ejemplo:
def saludar():
    nombre=input("Introduzca su nombre, por favor\n")
    print(f"¡Muy buenas, {nombre}!")
Para que se ejecute una función se debe llamar, por ejemplo:
saludar()
Argumentos posicionales
las funciones a veces tienen parámetros que se ponen dentro de los paréntesis de la definición
los parámetros son variables para introducir en las funciones
def saludar(nombre):
    print(f"¡Muy buenas, {nombre}!")
Nótese que se eliminó la opción para que el usuario introduzca el nombre.
Ahora el usuario deberá colocar el argumento cuando llame la función
saludo(Alberto)
saludo(ines)
Se pueden colocar tantos parámetros como sean necesarios, por ejemplo:
def(nombre, edad):
    print(f"Muy buenas {nombre}")
    print(f"Usted tiene {edad} años")
Argumentos de clave
La ventaja que tienen es que se pueden cambiar el orden en la declaración
saludar(nombre="Quique", edad=30)
return
Devuelve un resultado para utilizarlo dentro de la función
def suma(numero1,numero2):
    print(numero1+numero2)
suma(10,50)
muestra el resultado en la consola, pero si se necesita el resultado para hacer algo, no se puede
scope
significa que no se pueden usar variables definidas dentro de una función fuera de la misma
def suma(numero1,numero2):
    return numero1 + numero 2
resultado=suma(10,50)
de esta forma se guarda el valor del resultado de la función suma()
'''
#practica
'''
1.  añadir un color al principio de la lista con el uso de una función'''
colores=["rojo","verde","amarillo"]
def color(color):
    colores.insert(0,color)
color(str(input("Escriba un color para añadirlo a la lista: \n")))
print(colores)
'''
2.  Encontrar un error si lo hay
def saludar()
    nombre=input("Introduzca su nombre, por favor\n")
    print(f"Muy buenas {nombre}")
faltan los dos puntos'''
#Proyecto
'''Hacer una calculadora con funciones
debe tener suma, resta, multiplicación, división, módulo y exponente'''
print("Calculadora")
def calcular(num1,num2,operacion):
    if operacion==1:
        return num1+ num2
    elif operacion==2:
        return num1-num2
    elif operacion==3:
        return num1*num2
    elif operacion==4:
        return num1/num2
    elif operacion==5:
        return num1%num2
    elif operacion==6:
        return num1**num2
    else:
        return "operación inhabilitada"
operadores=["Suma","Resta", "Multiplicación", "División", "Módulo", "Exponente"]
indice=["1","2","3","4","5","6"]

exit=int(input("Desea realizar alguna operación?\n 1. Sí 2. No\n"))
operacion=0
num1=0
num2=0
while exit==1:
    for i in range(0,5):
        print(f"{indice[i]}-    {operadores[i]}")
    operador=int(input("Digite el número de la operación que desea realizar\n"))
    print(f"Ha elegido la opción {operadores[operador-1]}")
    num1=float(input(f"Ingrese el primer número de {operadores[operador-1]}\n"))
    num2=float(input(f"Ingrese el segundo número de {operadores[operador-1]}\n"))
    res=calcular(num1,num2,operador)
    print (f"El resultado de {operadores[operador-1]} es {res}")
    exit=int(input("Desea realizar alguna otra operación?\n 1. Sí 2. No\n"))
print("Que tenga un buen día")
while True:
    def calculadora_auto(num1,num2):
        resultados=[float(num1+num2),float(num1-num2),float(num1*num2),float(num1/num2) ,float(num1%num2),float(num1**num2)]
        operacion_resultados=["suma: ","resta: ","multiplicación: ", "división: ", "módulo: ","exponente: "]
        for i in range (0,5):
            respuesta=print(f"{operacion_resultados[i]}{round(resultados[i],2)}")
        return(respuesta)
    num1=float(input("Ingrese el primer número de las operaciones\n"))
    num2=float(input("Ingrese el segundo número de las operaciones\n"))
    calculadora_auto(num1,num2)