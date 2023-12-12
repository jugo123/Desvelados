from tkinter import *
from tkinter import ttk


class IngSin:
    def __init__(self, vent):
        self.vent = vent
        self.vent.title("ingreso de sintomas")
        vent.geometry("400x300")
        # crear contenedor (frame), recuadro que permite tener elementos
        frame = LabelFrame(self.vent, text="ingrese  datos de virus")
        # grid sirme para posicionar elementos
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        # ingreso de nombre
        Label(frame, text="nombre: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

        # ingreso de sintoma 1
        Label(frame, text="sintoma: ").grid(row=2, column=0)
        self.sintoma = Entry(frame)
        self.sintoma.grid(row=2, column=1)

        # ingreso de sintoma 2
        Label(frame, text="sintoma 2: ").grid(row=3, column=0)
        self.sintoma = Entry(frame)
        self.sintoma.grid(row=3, column=1)

        # ingreso de sintoma 3
        Label(frame, text="sintoma 3: ").grid(row=4, column=0)
        self.sintoma = Entry(frame)
        self.sintoma.grid(row=4, column=1)

        # agregar boton de guardado (W+E es para ocupar es para ocupar todo el espacio disponible)
        ttk.Button(frame, text="guardar datos").grid(row=5, columnspan=2, sticky=W + E)

        # crear tabla
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=6, column=0, columnspan=2)
        self.tree.heading('#0', text='nombre virus', anchor=CENTER)
        self.tree.heading('#1', text='sintoma', anchor=CENTER)


if __name__ == '__main__':
    vent = Tk()
    applicacion = IngSin(vent)
    vent.mainloop()
