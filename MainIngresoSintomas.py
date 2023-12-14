import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class VentanaSintomas:
    def __init__(self, master):
        self.master = master
        self.master.title("Ingreso de síntomas")
        self.master.geometry("600x500")

        self.nombre = tk.StringVar()
        self.sintoma = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        self.marco = tk.LabelFrame(self.master, text="Ventana de ingreso de síntomas")
        self.marco.place(x=50, y=50, width=500, height=400)

        lblNombre = tk.Label(self.marco, text="Nombre de virus").grid(column=0, row=0, padx=5, pady=5)
        txtNombre = tk.Entry(self.marco, textvariable=self.nombre)
        txtNombre.grid(column=1, row=0)

        lblSintoma = tk.Label(self.marco, text="Síntoma").grid(column=0, row=1, padx=5, pady=5)
        txtSintoma = tk.Entry(self.marco, textvariable=self.sintoma)
        txtSintoma.grid(column=1, row=1)

        tk.Label(self.marco, text="Aquí van los mensajes", fg="green").grid(column=1, row=2, columnspan=4)

        self.vistadatos = ttk.Treeview(self.marco)
        self.vistadatos.grid(column=1, row=3, columnspan=4)
        self.vistadatos["columns"] = ("nombre", "sintoma")
        self.vistadatos.column("#0", width=0, stretch=tk.NO)
        self.vistadatos.column("nombre", width=150, anchor=tk.CENTER)
        self.vistadatos.column("sintoma", width=150, anchor=tk.CENTER)
        self.vistadatos.heading("nombre", text="Nombre", anchor=tk.CENTER)
        self.vistadatos.heading("sintoma", text="Síntoma", anchor=tk.CENTER)

        btnGuardar = tk.Button(self.marco, text="Guardar", command=self.guardar)
        btnGuardar.grid(column=1, row=4)

        self.mostrar_datos()

    def guardar(self):
        nombre_virus = self.nombre.get()
        sintoma_valor = self.sintoma.get()

        if nombre_virus and sintoma_valor:
            try:
                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='proyecto_agil'
                )
                cursor = conexion.cursor()

                query = "INSERT INTO Sintomas (nombre, sintoma) VALUES (%s, %s)"
                cursor.execute(query, (nombre_virus, sintoma_valor))
                conexion.commit()

                messagebox.showinfo("Éxito", "Datos guardados correctamente")

                self.mostrar_datos()

            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error al guardar datos en la base de datos: {e}")

            finally:
                if conexion:
                    conexion.close()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def mostrar_datos(self):
        self.vistadatos.delete(*self.vistadatos.get_children())

        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='proyecto_agil'
            )
            cursor = conexion.cursor()

            query = "SELECT nombre, sintoma FROM Sintomas"
            cursor.execute(query)
            datos = cursor.fetchall()

            for dato in datos:
                self.vistadatos.insert("", "end", values=dato)

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error al obtener datos de la base de datos: {e}")

        finally:
            if conexion:
                conexion.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaSintomas(root)
    root.mainloop()
