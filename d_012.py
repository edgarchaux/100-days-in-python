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
entrada de datos
entrada=Entry(root)
entrada.insert(0, "Escriba su nombre")
entrada.bind("<key>", lambda e:entrada.delete(0,END))
entrada.insert(10,"pf")
entrada.pack()
Evento para la función
def pulsar_boton():
    nombre=entrada.get()
    Label(root, text=f"{nombre}").pack()
Botón
boton_1=Button(root, text="enviar", command=pulsar_boton).pack()
Bucle de ejecución
root.mainloop()'''