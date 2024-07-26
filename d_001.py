'''Este es el primer día de una serie de 100 días aprendiendo python. En el primer día se aprenderán las variables, salida y entrada de datos.'''
#Teoría
#Print()
'''Lo primero que se suele enseñar es cómo imprimir en consola los resultados de los programas que se realizan.
Para ello, se utiliza la función print()'''
print ('Hola mundo')

#Variables: 

'''Son contenedores de valores que pueden variar su valor. Para asignar variables se debe designar un valor de equivalencia
Convención de nombre de variables: en minúsculas, sin acentos, sin caracteres especiales y sin empezar con números. Para más de una palabra se usa el guión bajo.
Ejemplos de variables convencionalmente bien declaradas:
nombre_variable
_nombre_variable
nombre
numero1
Ejemplos de variables mal declaradas:
nombre-variable
1numero
nombre$variable
Ejemplos de variables convencionalmente mal declaradas
número1
China
España
adreCa
Hay que recordar que python es un lenguaje de programación key sensitive. Por tanto distingue entre mayúsculas y minúsculas
'''
#Salto de línea
'''Se usa para imprimir los valores una línea más abajo, Por ejemplo:
print ('Buenos días, señor juez\n')'''
#Concatenar
'''Une frases'''
#Comentarios
'''Existen 2 formas de hacer comentarios. Mediante # y mediante 3 comillas. python no lee los comentarios '''
#Práctica
'''Asignar una variable:'''
frase_bienvenida='Primer día de python'
'''Imorimir la anteior variable'''
print(frase_bienvenida)
'''Asignar el valar de una variable que está contenida dentro de otra variable e imprimirla:'''
variable_1='Hola    mundo'
variable_2= variable_1
print(variable_2)
'''Pedir al usuario que llene una varible con el valor de su elección e imprimir su valor:'''
nombre=input('Digite su nombre: \n')
print('Bienvenido/a '+nombre)
#Ejercicios:
'''1. Imprime la siguiente frase en la consola:
Estoy en el día 1 del reto python.'''
print('Estoy en el día 1 del reto python')
'''2. Almacena la frase alterior en una variable'''
frase = 'Estoy en el día 1 del reto python'
'''3. Imprime el valor de la variable frase'''
print(frase)
'''4. Observar las siguientes variables: '''
a='rojo'
b='naranja'
c='azul'
d='verde'
'''5. Asignar el valor verde a la variable a sin escribirlo con el teclado e imprimirlo'''
a=d
print(a)
'''6. asignar el valor 'rojo' a la variable c, sin asignar directamente a sobre c, ni escribir el valor literalmente'''
a='rojo'
b=a; a=b
c=b
print(a)
print(b)
print(c)
print(d)
'''7. Es correcto el siguiente código:
frase_1='Esta es la primera frase'; frase_2='Esta es la segunda frase' '''
'Sí es correcto, aunque por buenas prácticas es mejor separar las líneas de código'
'''8. ¿Hay algún error en la siguiente línea?'''
'''print      (       '¡Qué print más raro!')'''
'No hay ningún error, es sólo estético'
'''9. ¿Cómo sacarías estos dos strings juntos en el print()?'''
frase_1='Me llamo Andrés'
frase_2='encantado.'
print(frase_1+' '+frase_2)
#Mini proyecto
'''Construir un programa que haga lo siguiente:
1. Fase de saludo inicial 
2. Entrada del usuario preguntando el nombre
3. Entrada del usuario preguntando la edad
4. Entrada del usuario preguntando el país de nacimiento
5. Comentarios en cada sección del código (donde creas necesario)
6. Recoger los datos e imprimirlos
7. Utilizar saltos de línea donde creas conveniente'''
#Variables de entrada
saludo='Bienvenido/a '
nombre=input('¿Cómo te llamas?\n')
edad=input('¿Qué edad tienes\n')
pais=input('¿En qué país naciste?\n')
#Imprimiendo las variables
print(saludo+nombre+' de '+edad+' años nacido en '+pais)