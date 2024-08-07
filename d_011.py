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
'''
1.  Hacer la clase vacía llamada Motocicleta
'''
class  Motocicleta():
    #Atributos de clase
    estado="nueva"
    motor=False
    #Métodos
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color=color
        self.matricula=matricula
        self.combustible_litros=combustible_litros
        self.numero_ruedas=numero_ruedas
        self.marca=marca
        self.modelo=modelo
        self.fecha_fabricacion=fecha_fabricacion
        self.velocidad_punta=velocidad_punta
        self.peso=peso
    def arrancar(self):
        if self.motor:
            print("El motor ya estaba en marcha")
        else:
            print("El motor ha arrancado")
            self.estado="usada"
            self.motor=True
    def detener(self):
        if self.motor:
            print("El motor se ha detenido")
            self.motor=False
        else:
            print("El motor ya estaba detenido")
'''
2.  Añadir un atributo de clase especificando que todas las motos son nuevas'''
'''
3.  Crear el método init vacío'''
'''
4.  Añadir parámetros al init'''
'''
5.  Añadir otro atributo de clase motor de tipo booleano de valor predeterminado falso'''
'''
6.  Crear 2 métodos arrancar y detener. Para el método arrancar(): si el motor está detenido, se indica que el motor ha arrancado,
si el motor está en marcha, y se intenta arrancar de nuevo, se indica que el motor ya estaba en marcha
Para el método detener(): si el motor está en marcha, se indica que el motor se ha detenido. Si el motor está detenido, y se intenta detener de nuevo, se indica que el motor ya estaba detenido.
opcionalmente, que el método haga cambiar el estado del motor al llamar a los métodos'''
'''
7.  Instanciar una motocicleta con los siguientes valores:combustible_litros=10 y numero_ruedas=2'''
moto_1=Motocicleta("","",10,2,"","","","","")
'''
8.  Crear otra instancia de motocicleta utilizando los argumentos de clave, en lugar de los posicionales, en depósito colocar vacío'''
moto_2=Motocicleta(matricula="asd-123",color="gris",combustible_litros="vacío", numero_ruedas=2, marca="Suzuki",modelo="2019",fecha_fabricacion="",velocidad_punta="220mi/h",peso="35kls")
'''
9.  Probar los métodos de arranque y detener con una de los dos objetos'''
moto_1.arrancar()
moto_1.detener()
moto_2.arrancar()
moto_2.detener()
'''
10. añadir desde afuera de la clase un nuevo atributo para uno de los dos nuevos objetos llamado precio'''
moto_1.precio=19000
'''
11. Imprimir el valor precio desde afuera de la clase:
"El precio de la motocicleta" x (marca y modelo)es de x precio$"'''
print(f"El precio de la motocicleta {moto_1.marca}{moto_1.modelo}es de {moto_1.precio}")
'''
12. Hacer la misma consulta desde la clase'''