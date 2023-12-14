
"""import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ingreso de síntomas")
ventana.geometry("600x500")

nombre = tk.StringVar()
sintoma = tk.StringVar()

marco = tk.LabelFrame(ventana, text="Ventana de ingreso de síntomas")
marco.place(x=50, y=50, width=500, height=400)

lblNombre = tk.Label(marco, text="Nombre de virus").grid(column=0, row=0, padx=5, pady=5)
txtNombre = tk.Entry(marco, textvariable=nombre)
txtNombre.grid(column=1, row=0)

lblSintoma = tk.Label(marco, text="Síntoma").grid(column=0, row=1, padx=5, pady=5)
txtSintoma = tk.Entry(marco, textvariable=sintoma)
txtSintoma.grid(column=1, row=1)

tk.Label(marco, text="Aquí van los mensajes", fg="green").grid(column=1, row=2, columnspan=4)

vistadatos = ttk.Treeview(marco)
vistadatos.grid(column=1, row=3, columnspan=4)
vistadatos["columns"] = ("nombre", "sintoma")
vistadatos.column("#0", width=0, stretch=tk.NO)
vistadatos.column("nombre", width=150, anchor=tk.CENTER)
vistadatos.column("sintoma", width=150, anchor=tk.CENTER)
vistadatos.heading("nombre", text="Nombre", anchor=tk.CENTER)
vistadatos.heading("sintoma", text="Síntoma", anchor=tk.CENTER)

# Función para guardar datos en la base de datos
def guardar():
    nombre_virus = nombre.get()
    sintoma_valor = sintoma.get()

    if nombre_virus and sintoma_valor:
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='proyecto_agil'
            )
            cursor = conexion.cursor()

            # Insertar datos en la base de datos
            query = "INSERT INTO Sintomas (nombre, sintoma) VALUES (%s, %s)"
            cursor.execute(query, (nombre_virus, sintoma_valor))
            conexion.commit()

            messagebox.showinfo("Éxito", "Datos guardados correctamente")

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error al guardar datos en la base de datos: {e}")

        finally:
            if conexion:
                conexion.close()
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

# Botones
btnGuardar = tk.Button(marco, text="Guardar", command=guardar)
btnGuardar.grid(column=1, row=4)

ventana.mainloop()"""

import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ingreso de síntomas")
ventana.geometry("600x500")

nombre = tk.StringVar()
sintoma = tk.StringVar()

marco = tk.LabelFrame(ventana, text="Ventana de ingreso de síntomas")
marco.place(x=50, y=50, width=500, height=400)

lblNombre = tk.Label(marco, text="Nombre de virus").grid(column=0, row=0, padx=5, pady=5)
txtNombre = tk.Entry(marco, textvariable=nombre)
txtNombre.grid(column=1, row=0)

lblSintoma = tk.Label(marco, text="Síntoma").grid(column=0, row=1, padx=5, pady=5)
txtSintoma = tk.Entry(marco, textvariable=sintoma)
txtSintoma.grid(column=1, row=1)

tk.Label(marco, text="Aquí van los mensajes", fg="green").grid(column=1, row=2, columnspan=4)

vistadatos = ttk.Treeview(marco)
vistadatos.grid(column=1, row=3, columnspan=4)
vistadatos["columns"] = ("nombre", "sintoma")
vistadatos.column("#0", width=0, stretch=tk.NO)
vistadatos.column("nombre", width=150, anchor=tk.CENTER)
vistadatos.column("sintoma", width=150, anchor=tk.CENTER)
vistadatos.heading("nombre", text="Nombre", anchor=tk.CENTER)
vistadatos.heading("sintoma", text="Síntoma", anchor=tk.CENTER)

# Función para guardar datos en la base de datos
def guardar():
    nombre_virus = nombre.get()
    sintoma_valor = sintoma.get()

    if nombre_virus and sintoma_valor:
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='proyecto_agil'
            )
            cursor = conexion.cursor()

            # Insertar datos en la base de datos
            query = "INSERT INTO Sintomas (nombre, sintoma) VALUES (%s, %s)"
            cursor.execute(query, (nombre_virus, sintoma_valor))
            conexion.commit()

            messagebox.showinfo("Éxito", "Datos guardados correctamente")

            # Actualizar la vista de datos
            mostrar_datos()

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error al guardar datos en la base de datos: {e}")

        finally:
            if conexion:
                conexion.close()
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

# Función para mostrar datos en la vista de datos
def mostrar_datos():
    vistadatos.delete(*vistadatos.get_children())  # Limpiar la tabla antes de mostrar nuevos datos

    try:
        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='proyecto_agil'
        )
        cursor = conexion.cursor()

        # Obtener datos de la base de datos
        query = "SELECT nombre, sintoma FROM Sintomas"
        cursor.execute(query)
        datos = cursor.fetchall()

        # Mostrar datos en la vista
        for dato in datos:
            vistadatos.insert("", "end", values=dato)

    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error al obtener datos de la base de datos: {e}")

    finally:
        if conexion:
            conexion.close()

# Botones
btnGuardar = tk.Button(marco, text="Guardar", command=guardar)
btnGuardar.grid(column=1, row=4)

ventana.mainloop()


