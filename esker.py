from tkinter import *



import mysql.connector
 
 
 
dbConnect={
    'host':'localhost',
    'user': 'root',
    'passwd':'',
    'database':'tablamovimientos'
}


conexion = mysql.connector.connect(**dbConnect)
cursor=conexion.cursor()

sql="Select * from movimientos"
cursor.execute(sql)

resultados=cursor.fetchall()





raiz=Tk()

raiz.title("ERP CLASE")

raiz.resizable(1,1)#Tamaño ventana width/heigth

#raiz.iconbitmap("gato.ico")#cambio icono archivo con extension .ico  conversor.ico 

raiz.geometry("650x350")#tamaño ventana por defecto

raiz.config(bg="green")

lblTablaMovimientos=Label(raiz,text="Tabla Movimientos",font=('bold',30))
lblTablaMovimientos.place(x=20,y=30)
lblTablaMovimientos.pack()

lblSQL=Label(raiz,text=resultados,font=('bold',10))
lblSQL.place(x=20,y=60)
lblSQL.pack()

raiz.mainloop()#Siempre ultimo
