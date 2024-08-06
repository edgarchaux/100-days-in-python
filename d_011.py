#POO
#Parte teórica
'''Poo se refiere a un paradigma que representa objetos reales o imaginarios
cuyas particularidades se llaman atributos, así:
Taza_1
color="blanco"
mensaje=none
material="porcelana"
limpia=True
Taza_2
clases
sistemas de generadores de objetos
sintaxis
class Taza():
    color="blanco"
    mensaje=none
    material="porcelana"
    limpia=True"
Instancias del objeto
cuando se generan a partir de las clases
¿Cómo instanciar un objeto:
taza_1=Taza()
taza_2=Taza()
para ver la dirección de memoria
print(taza_1)
print(taza_2)
¿Cómo se acceden a los atributos de un objeto?
print(taza_1.color)
reasignar valores a objetos
taza_2.color="blanco y azul"
Métodos
funciones que pertenecen a una clase
¿Cómo se declara un método de una clase?
class Vehiculo():
pais_origen="Alemania"
    def __init__(self, color, longitud, ruedas)
        self.color=color
        self.longitud=longitud
        self.ruedas=ruedas
    def arrancar (self):
        print("El vehículo ha arrancado")
    def detener (self):
        print("El vehículo se ha detenido")
    def mostrar_info(self):
        print(f"El auto es de color{self.color} con una longitud de {self.longitud} y {self.ruedas} ruedas")
        print(f"El país de origen es {self.pais_origen}")
vehiculo_1=vehiculo("rojo", 4, 4)
vehiculo_1.arrancar(self)
vehicylo_1.detener(self)
vehiculo_2=Vehiculo("verde", 8.25,8)
¿Qué es self?
Es el objeto que será instanciado de la clase, representa el propio nombre de la clase
Se debe colocar en cada método
print(vehiculo_1.pais_origen)
Atributos de clase vs atributos de instancia
los atributos de instancia son los que tienen en los parámetros, es decir que cada objeto tendrá un valor diferente
los atributos de clase son los que son comunes en todos los objetos de la misma clase
En el ejemplo vehiculo, pais_origen es atributo de clase y color es atributo de instanciación
vehiculo_1.mostrar_info()
Estructuras vacías
sintaxis
class vehiculo():
    pass
'''
#Parte práctica