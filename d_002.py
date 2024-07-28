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
'''La función floor redonea hacia abajo eliminando todos los decimales. se utiliza con el simpolo doble de la división. Por ejemplo: print(7//2), da como resultado 3'''
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