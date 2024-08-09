#Strings avanzados
#Parte teórica
'''
concatenar
sintaxis'''
f="función"
s="suave"
p="programación"
print(" ".join([p,f,f,p]))
print(f+s)
print (f,s)
#Método join con listas
colores=["amarillo","azul","rojo","verde"]
separador="*"
concatena=separador.join(colores)
print(concatena)
#Operador %: formatea los strings
print("%s %s"%(p,f))
#Método format
print("{} {}".format(p,s))
#Multiplicar strings
print(p*3)
print((p+" ")*3)
#iterar strings
pf="100daysinpython"
for letra in pf:
    print(letra)
for letra in range(len(letra)):
    print(pf[letra])
#Diccionario con posiciones de un string
lista_pf=dict(enumerate(pf))
print(lista_pf)
#Parte práctica
'''
1.  Utilizar el método join para concatenar la frase'''
frase=["Estoy","aprendiendo","python","con","el","curso","de","100","días","de","programación","fácil"]
print(" ".join(frase))
'''
2.  Iterar la lista de colores y presentarla en la consola con el método format con la primera letra en mayúscula'''
guion="-"
punto="."
for i in range(len(colores)):
    print(f"{guion}{colores[i].capitalize()}{punto}\n")
'''
3.  concatenar usando % formato'''
num_1=10
num_2=34.50
result=num_1*num_2
print("La multiplicación de %i * %f da como resultado: %f."%(num_1,num_2,result))