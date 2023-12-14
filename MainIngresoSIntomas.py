import tkinter as tk
import pymysql
from tkinter import messagebox
import DAO.CRUDSintomas
from DTO import Sintomas, Varios
from tkinter import *


ventana = Tk()
ventana.title("ingreso de sintomas")
ventana.geometry("600x500")


nombre= StringVar()
sintoma= StringVar()

marco = LabelFrame(ventana, text = "ventana de ingreso de sintomas")
marco.place(x=50, y=50 , width=500, height=400)


lblNombre = Label(marco, text = "nombre de virus" ).grid(column=0, row=0, padx=5, pady=5)
txtNombre = Entry(marco, textvariable=sintoma).grid(column=1,row=0)

lblSintoma = Label(marco, text = "sintoma" ).grid(column=0, row=1, padx=5, pady=5)
txtSintoma = Entry(marco, textvariable=sintoma).grid(column=1,row=1)

Label(marco, text="aqui van los mensajes", fg="green").grid(column=1, row=2,columnspan=4)

vistadatos = ttk.Treeview(marco)
vistadatos.grid(column=1, row=3,columnspan=4)
vistadatos["columns"]=("nombre", "sintoma")
vistadatos.column("#0", width=0, stretch=NO)
vistadatos.column("nombre", width=150, anchor=CENTER)
vistadatos.column("sintoma", width=150, anchor=CENTER)
vistadatos.heading("nombre", text="Nombre", anchor=CENTER)
vistadatos.heading("sintoma", text="Sintoma", anchor=CENTER)

#botones
btnGuardar= Button(marco, text="Guardar", command=lambda:guardar())
btnGuardar.grid(column=1, row=4)


def llenar_tabla():
    vaciar_tabla()
    sql="select * from "
def vaciar_tabla():
    filas = vistadatos.get_children()
    for fila in filas:
        vistadatos.delete(fila)

def guardar():
    val= (nombre.get(), sintoma.get())
    sql= "insert into Sintomas(nombre, sintoma) values (%s, %s)"
    db.cursor.execute(sql)
    db.connection.commit()
    Label.config(text="datos guardados con exito", fg="green")
    llenar_tabla()

ventana.mainloop()
