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
#Parte práctica
'''
1.  Crear 4 botones'''
from tkinter import *
root=Tk()
root.title("TK")
def pulsar(numero):
    aviso=Label(root,text=f"ha pulsado el botón {numero}").pack()
    aviso=Pack()
boton_1= Button(root, text="botón 1", command=lambda:pulsar(1)).pack()
boton_1= Button(root, text="botón 2", command=lambda:pulsar(2)).pack()
boton_1= Button(root, text="botón 3", command=lambda:pulsar(3)).pack()
boton_1= Button(root, text="botón 4", command=lambda:pulsar(4)).pack()

root.mainloop()
'''
2. colocar una etiqueta a mostrar en cada botón'''
'''
3.  '''
Label(root, text="Nombre").grid(column=0,row=0)
nombre=Entry(root)
nombre.grid(column=1, row=0)
Label(root, text="Edad").grid(column=1,row=0)
Label(root, text="Edad").grid(column=0,row=0)
nombre=Entry(root)
nombre.grid(column=1, row=0)
Label(root, text="Edad").grid(column=1,row=0)
edad=Entry(root)
edad.grid(column=1, row=1)