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
#