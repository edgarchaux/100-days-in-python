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