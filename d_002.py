#Este es el día 2 de los 100 días en python
#Teoría
#Tipos de datos y conversiones
#Strings
'''Tipo de texto. Para imprimir el tipo print se usan las comillas simples y las dobles.
por ejemplo print('Este es un "string"')'''
#len
'''Es una función que devuelve el número de caracteres de una palabra. Por ejemplo:
print(len('amarillo')) devuelve 8. La función len recibe strings o variables. la opción len(amarillo[2]) devuelve a, ya que es la posición en el string contando a partir de 0'''
#int
'''Tipo de dato para numeros enteros. Con los que se pueden hacer operaciones básicas. Por ejemplo
a =1; b=2; print(a+b). la anterior sentencia imprimirá 12. Pero 12 no es el resultado de 1+2.
Esto se debe a que la función print no ejecuta operaciones matemáticas, sino que + concatena líneas de caracteres.
Si se desea ejecutar el resultado, se debe llamar una nueva variable. Por ejemplo:
a=1; b=2; c=a+b; print(c)'''
#Cálculo de exponentes
'''Para calcular potencias se utiliza el signo * 2 veces. Por ejemplo: a=2**3 print(a) imprimirá 8'''
#Orden de las operaciones:
'''Se ejecutan primero la multiplicación y división, luego la suma y la resta'''
#float
'''Son números racionales. Es decir decimales. Ejemplo: numero1=1; numero2=2; print(numero1+numero 2). Impreme 3'''
#round
'''Para redondear al alta un número se usa round(). Por ejemplo: print(round (7.3)), imprime 8
Para imprimir una aproximación manteniendo un número fijo de decimale, por ejemplo 2 se le da un segundo número al argumento.
Por ejemplo: print(round(7.34567,2)), imprime 7.35'''
#floor
'''La función floor redonea hacia abajo eliminando todos los decimales. se utiliza con el simbolo doble de la división. Por ejemplo: print(7//2), da como resultado 3'''
#Módulo
'''Operador que devuelve el resto de la división. Se usa el simbolo %. Por ejemplo: 7%2 devuelve 1. Porque 3*2=6, entonces al 7 le sobra 1 para que la división sea exacta.'''
#Operadores de asignación de incremento y decrecimiento
'''Los operadores de asignación de incremento reasignan una variable para que se incremente automáticamente en un valor designado. Por ejemplo: a=1; a+=1; print(a), imprime 2.'''
#Operadores de asignación de decremento
'''Reasigna el valor disminuendo la variable en el valor seleccionado. Ejemplo: a=100; a-=20; print(a) Imprime 80'''
#str
'''Si se quiere forzar a que una variable la imprima como string se usa la función str. Ejemplo. suma=75; print('El valor de la suma es: '+ str(suma)). Imprimirá la concatenación resultante'''
#Formateo de strings
'''Para imprimir la concatenación en una línea sin cambiar su tipo de dato se puede usar la opción f de la función print así:
print(f'El resultado de la suma es: {suma}')'''
#Booleanos
'''Estos tipos de datos solo reciben uno de dos tipos de datos: False o True'''
#Tipo de dato
'''Para consultar el tipo de dato se utiliza la función type. Así: a=7; b='ayer'; c=False; type(a), Imprimirá el tipo de dato de la variable a'''
#int
'''Transforma un número a un tipo integer. Ejemplo: a=2.0;b=int(a); print(b), imprimirá int'''
#float
'''Transforma datos a float. Por ejemplo: a='2.3'; float(a); print(type(a)), imprimirá float, que es el tipo de dato de la variable'''
#Práctica
'''
1.  ¿Cuáles de estos strings son correctos?
a.  "Hoy es un gran día para programar"
b.  'El cielo está nublado"
c.  '¿Qué día es hoy?'
d.  "Mañana, en inglés se dijo "morning""
Respuesta: a, c
2.  ¿Qué error devuelven los strings mal escritos?
sintax error
3. Imprime en la consola el número de caracteres que tien la palabra 'automáticmente'. Lo puedes hacer con variable o directamente'''
print(len('automaticamente'))
'''
4.  Muestra en la consola solo el caracter de la á con acento de 'automáticamente' usando el posicionamiento de string'''
palabra='automáticamente'
print(palabra[5])
'''
5.  Realizar 10^5 con el uso del operador exponente'''
print(10**5)
'''
6.  Realizar la misma operación sin el operador exponente'''
print(10*10*10*10*10)
'''
7.  ¿En qué dos estados puede estar un dato booleano?
Respuesta: True, False
8.  Mostrar el tipo de dato de la variable numero_1=675.87'''
a=675.87
print(type(a))
'''
9.  Mostrar la cantidad de dígitos que tiene (768763843) usando len()'''
a='768763843'
print(len(a))
'''
10. Convertir los datos float a integer'''
num_1='14.527'
num_2='560.92'
num_1=float(num_1)
num_2=float(num_2)
num_1=int(num_1)
num_2=int(num_2)
print(type(num_1))
print(type(num_2))
'''
11. Redondear los números con la cantidad de cifras indicadas:
num_1= 10.897654876534  -->3 cifras
num_2= 7674.7886    -->2 cifras
num_3= 68754.78     -->1 cifra'''
num_1= 10.897654876534
num_2= 7674.7886
num_3= 68754.78
num_1=round(num_1,3)
print(num_1)
num_2=round(num_2,2)
print(num_2)
num_3=round(num_3,1)
print(num_3)
'''
12. ¿Cúal es la diferencia entre el operador módulo y el floor division?
Respuesta: El módulo es el resto de la división, en cambio floor division es el resultado entero de la división
13. Asignar con los operadores de incremento o decremento
num_1=10    -->+60
num_2=24    -->-100
num_3=65.67 -->+4.33'''
num_1=10
num_2=24
num_3=65.67
num_1+=60
num_2-=100
num_3+=4.33
print(num_1)
print(num_2)
print(num_3)
'''
14. Mediante el formateo de strings, mostrar todos los valores con la frase El valor 769.97 es bastante más grande que 4. ¿Am I a string? The answer is True, sin utilizar la concatenación'''
num_1=4
num_2=769.97
texto='am I a string'
decision=True
print(f'El valor {num_2} es bastante más grande que {num_1}. ¿{texto}? The answer is {decision}.')
#Project
'''Construir una calculadora sencilla de exponentes.
La calculadora deberá pedirle al usuario los números que quiere.'''
print('---Calculadora de exponentes---')
num_1=int(input('Introduzca el primer número\n '))
num_2=int(input('Introduzca el segundo número\n '))
resultado=num_1**num_2
print(f'El resultado de {num_1} elevado a {num_2} es {resultado}.')