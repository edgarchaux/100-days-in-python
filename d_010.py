#Funciones lambda
#Parte teórica
'''
Son funciones cortas con sintaxis reducida, solo tiene una expresión
Por ejemplo:
def multiplicacion(num1, num2):
    return num1*num2
en funcion lambda sería:
lambda num1, num2: num1*num2
Para llamar a las funciones lambda:
se almacenan en variables, por ejemplo:
multiplicacion=lambda num1, num2: num1*num2
resultado1=multiplicacion(10,7)
print(resultado1)
Otra forma de llamarlas es:
(lambda num1, num2: print(num1*num2))(7,5)
Lambda no se puede hacer si se requiere más de una expresión
'''
#Parte práctica
'''
1.  Crear con una función lambda una calculadora de áreas de círculo cuyo único parámetro sea el radio'''
radio=int(input("Introduzca el radio del círculo en cm\n"))
pi=3.14
area=round((lambda radio: pi*radio**2)(radio),2)
print(f"El área del círculo es: {area} cms")
'''
2.  Crear una funcipon lambda para saludar por tu nombre'''
nombre=input(str("¿Cómo te llamas?\n"))
saludo=(lambda nombre:'bienvenido|a, '+nombre)(nombre)
print(saludo)
'''
3.  Mediante una función lambda imprimir: El color se encuentra en la posición 1 de la lista'''
colores=["rojo", "azul","verde","amarillo"]
color=str(input("¿Qué color quieres buscar?\n"))
busqueda=(lambda color: colores.index(color))(color)
print(f"El color {color} se encuentra en la posición {busqueda} de la lista")