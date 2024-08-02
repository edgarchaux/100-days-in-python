#Los diccionarios y sets
#Parte teóorica
'''
Diccionarios:
Los diccionarios son parecidos a las tuplas o a las listas,
con la diferencia que tienen un código que los identifica.
Sintaxis:
microsoft_office={
    "word":"Microsoft word en el mundo del sistema es un slogan de un youtuber",
    "excel":"Microsoft excel es un programa de hojas de cálculo",
    "power": "Significa poder en inglés"}
las claves son: "word", "excel" y "power"
el asignador es el signo de dos puntos
el valor es el texto largo
el separador es el signo de ,
Para llamar a un diccionario entero se usa su nombre. Ejemplo:
print(microsoft_office)
para llamar a un valor del diccionario:
print(microsoft_office["word"])
las claves de los diccionarios pueden ser int, por ejemplo:
diccionario={
    1: "valor 1",
    2: "valor 2",
    3: "valor 3",
    }
print(diccionario[3])
Para añadir nuevos elementos al diccionario:
microsoft_office["ourlook"]="Nunca supe para que servía
print(microsoft_office["outlook"])
diccionarios vacios
Se usan para que el usuario vaya llenando datos
sintaxis
vacio={}
print(vacio)
ejemplo de utilidad de diccionario vacio:
inventario={
    1: "Espada",
    2: "Escudo",
    3: "mascota",
}
inventario = {}
print(inventario)
al principio el diccionario tenía 3 elementos,
pero al npc lo mataron y perdió todos los elementos que había conseguido
Editar elementos existentes:
microsoft_office["word"]="sirve para mucho"
print(microsoft_office["word"])
Bucles iteradores de diccionarios de claves:
imprime todas las claves del diccionario
sintaxis
for programa in microsoft_office:
    print(f"[programa]")
poner la primera letra en mayúscula de manera automática
sintaxis
for program in microsoft_office
    print(f"program.capitalize()")
'''