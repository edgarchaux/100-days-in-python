#Tkinter- personalizar ventana-pack y grid
#Parte teórica
'''
Importaciones
from tkinter import *
creación de la ventana principal:
root=Tk()
Título de la ventana
root.title("Curso de TKinter")
Tamaño de la ventana
root.geometry("800x600+560+240")
Creación de las etiquetas
mensaje=label(root, text="Mi primer programa con TKinter.").grid(row=0, column=0)
mensaje_2=label(root, text"Usted ha pasado por aqu+i dos veces")
Mostrar etiquetas
mensaje.grid(row=1, column=0)
mensaje_2.grid(row=0, column=0)
bucle de ejecución
root.mainloop()
Método grid
'''
#práctica
'''
1.  verdadero o falso
El método grid sirve para posicionar los elementos en el orden de aparición del código false
2.  El método para mantener el paquete tkinter en marcha es mainloop verdadero
3.  crear una ventana de tkinter que se mantenga abierta'''
from tkinter import *
root=Tk()
root.title("concentración")
'''redimensionar a 600px de y 450p'''
root.geometry("600x450")
'''
6.  que la pantalla aparezca en 50 70'''
root.geometry("800x600+50+70")
'''7. crear que un par de etiquetas'''
saludo=Label(root, text="vete ya")  
'''
8.   mostrar con grit '''
saludo.grid(row=0,column=0 )
root.mainloop()