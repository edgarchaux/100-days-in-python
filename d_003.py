#Tercer día de 100 días en python
#Los condicionales IF, ELIF, ELSE Y MATCH(SWITCH)
#Teoría
#Operadores de decisión
'''
>   mayor que
>   menor que
==  igual que
>=  mayor o igual que
<=  menor o igual que
!= diferente
'''
#If
'''Son estructuras diseñadas para tomar decisiones, donde una variable toma un valor de verdadero o falso.'''
numero=10
if numero>7:
    print('El número es mayor a 7')
elif numero==7:
    print('El número es igual a 7')
else:
    print('El número es menor a 7')
#If anidados
'''Son los condicionales dentro de otros condicionales. Por ejemplo:'''
edad=int(input('¿Cuántos años tiene?\n'))
if(edad>=18):
    print('Puede comprar alcohol. ¿Cuál desea?')
    eleccion=input('1-   ron\n 2-   whisky\n 3- ginebra\n')
    if eleccion==1:
        print('Ha elegido comprar ron')
    elif eleccion==2:
        print('Ha elegido comprar whisky')
    elif eleccion==3:
        print('Ha elegido comprar ginebra')
    else:
        print('Elección inválida')
else:
    print('ud es menor de edad, por favor retírese')
#Operadores lógicos
'''Son operadores de and, or , not. and es para que se cumplan todas las sentencias, or es cuando se cumple alguna de las sentencias y not es cuando no se cumple ninguna
Ejemplo:'''
color='rojo'
forma='circulo'
if(color=='rojo' and forma=='circulo'):
    print(f'Es un {forma}{color}')
else:
    print(f'No es un {forma}{color}')
color='rojo'
forma='circulo'
tamaño='pequeño'
if color=='rojo' and forma=='circulo'and tamaño=='pequeño':
    print(f'Es un {forma}{color}')
else:
    print(f'No es un {forma}{color}')
if color=='rojo' or forma=='cuadrado' or tamaño=='pequeño':
    print ('Se cumple la condición')
else:
    print('No se cumple la condición')
if not color=='azul' and not forma=='cuadrado':
    print('Se cumple la condición')
else:
    print('No se cumple la condición')
#match
error=input('Introduzca un código válido\n')
'''match error:
    case '200':
        print('Todo ok')
    case '300':
        print('Todo no tan ok')
    case '400':
        print('Todo mal')
    case _:
        print ('Error no disponible')'''    
#Práctica
'''1. completar con el operador correcto'''
numero=10
if numero > 7:
    print ('verdadero')
'''2. Completar con el operador correcto'''
numero=5
if numero<7:
    print('Verdadero')
'''3. Completar con el operador correcto'''
numero=7
if numero==7:
    print('Verdadero')
'''4. Completar con el operador correcto'''
color='Verde'
forma='triangular'
if color=='Verde' and forma=='triangular':
    print('Verdadero')
else:
    print('False')
'''5. Completar con el operador correcto'''
color='rojo'
forma='circulo'
tamaño='pequeño'
if color=='rojo' and forma=='circulo' or not tamaño=='grande':
    print('Verdadero')
else:
    print('Falso')
'''6. El bloque else nunca lleva la expresión de comparación, está sujeto a las expresiones del if y elif si lo hay'''
print('Verdadero')
'''7 Qué devuelve'''
numero_1=10
numero_2=10
numero_3=15
if numero_1 == numero_2 and numero_3>numero_1:
    print('Se cumple la condición')
else:
    print('No cumple la condición')
'''Respuesta: Se cumple la condición'''
'''8. Encontrar los errores'''
'''if numero>7:
        print('El número es mayor que 7.')
    else if numero==7
        print('El número es igual a 7.')
else:
    print('El número es menor a 7.')
Respuesta: No existe else if, existe elif
9. Encontrar los errores
numero=5
if numero>7
    print('El número es mayor que 7.')
else
    print('El número es menor o igual a 7.')
Respuesta: después de la sentencia if t else, se debe poner :
10. Encontrar los errores
numero=5
if numero=7:
    print ('El número es mayor que 7.')
else:
    print('El número es menor o igual a 7.')
Respuesta: El operador del if debe cambiarse a >'''
#Project
'''Hacer una calculadora con dos datos numéricos de sumas, restas, multiplicación, módulo y exponentes en la consola de python.'''
'''Requisitos: título, el usuario escogerá primero la opción, informar al usuario la opción seleccionada, si la opción no está en el menú, avisarle
se debe avisar si la opción marcada no está isponible, entrada de datos de tipo float, añadir redondeo a 2 cifras
'''
print('---CALCULADORA MEJORADA\n')
operador=int(input('Hola, elija una opción: \n 1- Suma.\n 2- Resta.\n 3- Multiplicación.\n 4- División.\n 5- Módulo.\n 6- Exponente.\n Teclee un número y pulse ENTER:'))
print(f'Ha elegido la opción"{operador}".')
opcion=None
if operador==1:
    opcion='suma'
    print(f'Usted escogió: {opcion}')
    numero_1=round(float(input('Especifique el primer operando\n')),3)
    numero_2=round(float(input('Especifique el segundo operando\n')),3)
    resultado=round((numero_1+numero_2),3)
    print(resultado)
elif operador==2:
    opcion='resta'
    print(f'Usted escogió: {opcion}')
    numero_1=round(float(input('Especifique el primer operando\n')),2)
    numero_2=round(float(input('Especifique el segundo operando\n')),2)
    resultado=numero_1-numero_2
    print(resultado)
elif operador==3:
    opcion='multiplicación'
    print(f'Usted escogió: {opcion}')
    numero_1=round(float(input('Especifique el primer operando\n')),2)
    numero_2=round(float(input('Especifique el segundo operando\n')),2)
    resultado=numero_1*numero_2
    print(resultado)
elif operador==4:
    opcion='división'
    print(f'Usted escogió: {opcion}')
    numero_1=round(float(input('Especifique el primer operando\n')),2)
    numero_2=round(float(input('Especifique el segundo operando\n')),2)
    resultado=numero_1/numero_2
    print(resultado)
elif operador==5:
    opcion='módulo'
    print(f'Usted escogió: {opcion}')
    numero_1=round(float(input('Especifique el primer operando\n')),2)
    numero_2=round(float(input('Especifique el segundo operando\n')),2)
    resultado=numero_1%numero_2
    print(resultado)
elif operador==6:
    opcion='exponente'
    print(f'Usted escogió: {opcion}')
    numero_1=round(float(input('Especifique el primer operando\n')),2)
    numero_2=round(float(input('Especifique el segundo operando\n')),2)
    resultado=numero_1**numero_2
    print(resultado)
else:
    print('Error, opción inválida.\n Por favor, vuelva a ejecutar la calculadora.')