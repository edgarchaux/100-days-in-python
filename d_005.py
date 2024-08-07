#Bucles for y while
#Parte teórica
#Bucles
'''Estructuras de flujo que permiten hacer varias repeticiones automáticamente
Flujo de ejecución
va verticalmente desde la línea 1 hasta la última, en los bucles sino se cumple su condición se ignora su código,
sino se cumple su ejecución se repite hasta que se cumpla.
Bucle FOR
Si se cumple la condición, ignora el bucle, sino, se ejecuta
for i in range(5):
    print(f"El valor del bucle es {i}")
Si se añade otro argumento, el primero da el valor inicial
for i in range(3,7):
    print(f"El valor del bucle es {i}")
print("Fin del bucle").
Si se añade un tercer argumento, indica el incremento
for i in range (3,12,3):
    print(f"El valor del bucle es {i}")
print ("Fin del bucle")
Si el tercer argumento es negativo, indica deccrecimiento
for i in range (3,12,-3):
    print(f"El valor del bucle es {i}")
print ("Fin del bucle")
Iterar listas
Para realizar una acción muchas veces
colores=["rojo","azul","verde","amarillo"]
print("---LISTADO DE COLORES---")
for color in colores
    print(f"-{color}-")
El bucle ahorra tiempo y recursos
condicionales dentro de bucles
permiten terminar los bucles antes de ejecutrlo todo, por ejemplo:
for color in colores:
    if color=="azul"":
        print(f"Se ha roto la ejecución del bucle")
        break
    print(f"-color {color}.")
Bucle while
i=1
while i<5:
    print(f"El valor del bucle es: {i}")
    i+=1
Método lower()
Convierte los strings en minúsculas
'''
#Práctica
'''
1. Crear un bucle for que imprima los valores de 7 al 14'''
for i in range(7,15):
    print( f"El valor del bucle es: {i}.")
'''
2.  Crear la misma salida que en el punto 1, pero con un bucle while'''
i=7
while i<15 and i>=7:
    print(f"El valor del bucle es:{i}.")
    i+=1
'''
3.  crear un bucle for que vaya del 0 al -50000, con decrecimientos de 500'''
for i in range(0,-5001,-500):
    print(f"El valor del bucle es: {i}")
i=0
while i>=-5000:
    print(f"El valor del bucle es: {i}")
    i-=500
'''
4.  Iterar en un ciclo for la lista paises'''
paises=["United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam"]
for i in range(0,5,1):
    print(f"->{paises[i]}<-")
'''
5.  Iterar la siguiente lista ignorando el número 356 y 10:'''
numeros=[10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
numeros.sort()
for i in numeros:
    if i==10:
        continue
    elif i==356:
        break
    else:
        print(f"El valor del elemento es: {i}")
#project
'''Hacer un programa para pedidos de pizza para ir añadiendo
Requisitos:
1.  Debe tener el título de la pizzería en el encabezado ->Pizzería PF<-
2.  Guardar en una variable el dinero que el usuario quiere introducir
3.  Crear una lista donde ir añadiendo ingredientes extra
4.  Habrán mínimo 3 tipos de pizza para elegir
5.  Cada pizza tendrá un coste diferente
6.  El usuario podrá elegir sólo una piza
7.  Una vez elegida la pizza se le informará al usuario el total que lleva por el momento
8.  Se le debe pedir al cliente si quiere añadir o no ingredientes extra (estos harán subir el precio final)
9.  Añade al menos 3 ingredientes extra. El usuario podrá elegir uno o varios de estos. No hay límite de ingredientes extra. Sise pasa del dinero se le dirá que no le llega y que vuelva a realizar el pedido
10. Las pizzas e ingredientes tendrán sus precios almacenados en variables
11. Con cada ingrediente extra, se debe ir sumando al total y mostrarselo al usuario con el cambio que le queda.
12. Si el usuario no quiere ingrediente extra, puede pagar directamente sin añadir ninguno.'''
print("->Pizzería PF<-")
cash=float(input("¿Cuánto dinero desea cargar?\n"))
topics=[]
extra_topics=["Queso", "Champiñones", "Pepperoni"]
pizza=["Margarita","Jamón y queso", "Cuatro quesos"]
pizza_costs=[7.85,9.65,9.95]
margarita_cost=7.85
jamon_cost=9.65
queso_cost=9.95
extra_pay=[1.2,2.3,2.1]
pay= 0
extra_cost=[]
extra_car=[]
order=int(input(f"Por favor digite el número de la pizza que desea elegir:\n 1 - Margarita - {margarita_cost}$\n 2 - Jamón y queso - {jamon_cost}$\n 3 - Cuatro quesos - {queso_cost}$\n"))
print(f"Ha elegido la pizza {pizza[order-1]}")
pay_pizza=pizza_costs[order-1]
if (order==1 or order==2 or order ==3)and cash>=pay_pizza:
    pay=pay_pizza
    print(f"Hasta el momento el valor de su compra es de: {round(pay,2)}")
    print(f"Ud cargó {cash} pesos, su pedido es de {round(pay,2)} por tanto le quedan {round(cash-pay)}")
    extra=int(input(f"¿Desea añadir algún ingrediente extra? 1 sí 2 No\n"))
    if extra==1 and cash>=pay:
        while cash>pay and extra==1:
            extra_topic=int(input(f"Ingrese el código del ingrediente que desea:\n 1- Queso - 1.2$ \n 2- Champiñones - 2.3$ \n 3- Pepperoni - 2.1$\n"))
            if cash<(pay+extra_pay[extra_topic-1]):
                print("No le alcanza la plata para el nuevo pedido")
                break
            if extra_topic==1:
                pay+=extra_pay[0]
                extra_cost.append(extra_pay[0])
                extra_car.append(extra_topics[extra_topic-1])
            elif extra_topic==2:
                pay+=extra_pay[1]
                extra_cost.append(extra_pay[1])
                extra_car.append(extra_topics[extra_topic-1])
            elif extra_topic==3:
                pay+=extra_pay[2]
                extra_cost.append(extra_pay[2])
                extra_car.append(extra_topics[extra_topic-1])
            else:
                print("opción iválida")
                break
            print(f"El valor de los adicionales es de:")
            for i in range(0,len(extra_cost)):
                print(f"- {extra_car[i]}    {extra_cost[i]}$-")
            print(f"El valor de su orden es de: {round(pay,2)}, ud cargó {round(cash)}, su cambio es de: {round(cash-pay)} pesos.")
            extra=int(input(f"¿Desea añadir algún otro ingrediente extra? 1 sí 2 No\n"))
    print("De acuerdo, no se añade nada más")
else:
    print("Opción no válida")
print("---Su pedido---")
print(f"El valor de su orden es de: {round(pay,2)}\nud cargó {round(cash,2)}, su cambio es de: {round(cash-pay,2)} pesos.")
print(f"Pizza de {pizza[order-1]}\ncon adicionales de:")
for i in range(0,len(extra_cost)):
    print(f"-{extra_car[i]}     {extra_cost[i]} $-")
print("Disfrute su pedido")