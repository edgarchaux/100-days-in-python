#Listas y tuplas
#Teoría
#Listas
'''Variables que pueden contener más de un valor de diferente o igual tipo a la vez. Se crean igual que una variable
Ejemplo:
colores=['rojo','amarillo','verde','azul','morado']
De igual forma para imprimirlas se usa print(). Por ejemplo:
print(colores)
Para imprimir elementos:
print(colores[0]), para imprimir el elemento 0 de la lista colores
También se pueden imprimir elementos con formato así:
print(f"El segundo elemento de la lista es:{colores[2]}")
Para acceder a un carácter de un elemento:
print(colores[1][3]), esto imprime la r del color amarillo
para imprimir una lista en sentido inverso:
print(colores[-1]), imprime el último elemento de la lista, es decir, morado
para sustituir elementos de la lista:
colores[1]='dorado', cambia el color amarillo por dorado
Para añadir nuevos elementos:
colores.append('fucsia') añade el elemento fucsia al final de la lista
Para añadir nuevo elemento en una posición específica
colores.inser(2,'celeste'), inserta un nuevo elemento en la posición 2
Para eliminar elementos:
colores.clear(), elimina todos los elementos de la lista
Para eliminar elementos de la lista por su número de posición:
colores.pop(2), elimina el elemento de la posición 2
Para eliminar elementos por su valor:
colores.remove("rojo"), elimina todos los elementos de valor rojo
Método copy(): copia el contenido de una lista en otra:
Colores2=colores.copy(), copia el contenido de la lista colores a la lista colores2
Método count(): es para saber el número de veces que se repite un elemento:
print(colores.count("azul")), muesta el número de veces que se repite el valor azul en la lista colores
Método index(): busca la posición de la primera ocurrencia de un elemento
print(colores.index("verde"))
Método reverse(): invierte las posiciones de una lista
colores.reverse()
Método sort(): Ordena alfabéticamente los elementos de una lista en forma ascendente
colores.sort()
si se quiere cambiar de forma ascendente:
colores.sort(reverse= True)
También ordena los números, por ejemplo:
numeros=[12,92,23,64,25]
numeros.sort()
Método extend(): para unir dos listas, por ejemplo:
colores.extend(colores2)
print (colores)
Nota: si se extiende con un valor string y no una lista, cada letra del string se ubicará en cada posición
Tuplas
Son elementos inmutables una vez se declaran. Se diferencian de las listas sintácticamente por los paréntesis. Por ejemplo:
colorest=("rojo","azul","verde", "morado")
Para llamar a un elemento de una tupla se usan los corchetes
print(colorest[0])
Las tuplas no tienen todos los métodos de las listas
Método len()
Dice la cantidad de elementos que tiene una lista o una tupla, por ejemplo:
print(len(colores))
print(len(colorest))'''
#Práctica