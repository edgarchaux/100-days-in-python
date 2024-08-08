#Iniciación a los eventos con TKinter
#Parte teórica
'''
Eventos con mouse y teclado
Se trata de que se ejecute una acción cuando se ejecute un activador
GUI
son los programas de interfaz gráfica
Importaciones
from tkinter import *
crear ventana principal
root=Tk()
Título de la ventana
root.title("Curso de Tkinter de programación fácil")
entrada=Entry(root)
entrada.pack()
Evento para la función
def pulsar_boton():
    texto=entrada.get()
    Label(root, text=f"{texto}").pack()
Botón
boton_1=Button(root, text="pulsa aquí", command=pulsar_boton).pack()
Bucle de ejecución
root.mainloop()'''