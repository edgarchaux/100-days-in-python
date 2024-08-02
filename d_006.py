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
'''