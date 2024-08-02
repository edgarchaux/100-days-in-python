#Introducción a TKINDER e importación de módulos
#Parte teórica
'''Los módulos o bibliotecas en python son herramientas que
facilitan el acceso y manipulación de algunos métodos.
Para realizar una importación
importaciones
from tkinter import *
si en vsc el paquete está en gris, quiere decir que no está siendo utilizado
tkinter es un paquete para crear interfaces gráficas
sintaxis creación de la ventana principal
root=Tk()
creación de la etiqueta
mensaje=label(root, text="Mi primer programa con Tkinter")
Muestra la etiqueta
mensaje.pack()
no mostrará nada porque se necesita un bucle así:
root.mainloop()
'''