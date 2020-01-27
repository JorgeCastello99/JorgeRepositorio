from tkinter import *


raiz=Tk()

raiz.title("Ventana de proyecto")

raiz.resizable(1,1)#Tamaño ventana width/heigth

#raiz.iconbitmap("gato.ico")#cambio icono archivo con extension .ico  conversor.ico 

raiz.geometry("650x350")#tamaño ventana por defecto

raiz.config(bg="green")

miFrame=Frame()

miFrame.pack(fill="y",expand="True")#empaquetar

miFrame.config(bg="red")

miFrame.config(width="650",height="350")

miFrame.config(relief="groove")



raiz.mainloop()#Siempre ultimo