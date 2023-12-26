import tkinter as tk
import pymysql
from tkinter import messagebox
import Modelo.CRUDUsuario
from Presentador import Usuarios
from MainIngresoVirus import VentanaVirus
from MainIngresoSintomas import VentanaSintomas
from MainIngresoADN import VentanaADN
def salir_del_usuario_actual(ventana_actual):
    ventana.deiconify()
    ventana_actual.destroy()

def abrir_ventana_secundaria(ventana_actual, id_usuario, rol_usuario):
    ventana_actual.withdraw()

    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.minsize(width=400, height=200)
    ventana_secundaria.config(padx=30, pady=30)

    # Botón para abrir ventana ingreso sintomas
    tk.Button(ventana_secundaria, text="ingresar sintomas", command=lambda: ingresar_sintomas(ventana_secundaria)).pack(pady=10)

    # Botón para abrir ventana ingreso virus
    tk.Button(ventana_secundaria, text="ingresar virus", command=lambda: ingresar_virus(ventana_secundaria)).pack(pady=10)

    # Botón para abrir ventana ingreso de ADN
    tk.Button(ventana_secundaria, text="Ingresar ADN", command=lambda: ingresar_adn(ventana_secundaria, rol_usuario)).pack(pady=10)

    # Botón para salir de la ventana secundaria
    tk.Button(ventana_secundaria, text="Salir del Usuario", command=lambda: salir_del_usuario_actual(ventana_secundaria)).pack(pady=10)
def ingresar_sintomas(ventana_secundaria):
    # Ocultar la ventana actual
    ventana_secundaria.withdraw()

    ventana_sintomas = tk.Toplevel(ventana)
    ventana_sintomas.title("Ingreso de síntomas")
    ventana_sintomas.geometry("600x500")

    app_sintomas = VentanaSintomas(ventana_sintomas)

def ingresar_virus(ventana_secundaria):
    # Ocultar la ventana actual
    ventana_secundaria.withdraw()

    ventana_virus = tk.Toplevel(ventana)
    ventana_virus.title("Ingreso de datos de virus")
    ventana_virus.geometry("600x500")

    app_virus = VentanaVirus(ventana_virus)
def ingresar_adn(ventana_secundaria, rol_usuario):
    if rol_usuario == "Infectólogo":
        ventana_adn = tk.Toplevel(ventana_secundaria)
        ventana_adn.title("Ingreso de ADN")
        ventana_adn.geometry("600x500")

        app_adn = VentanaADN(ventana_adn, rol_usuario)
    else:
        messagebox.showwarning("Acceso no autorizado", "Solo los infectólogos pueden acceder a esta función.")

def volver_a_principal(ventana_actual):
    ventana.deiconify()
    ventana_actual.destroy()

def open_login_window():
    def verificar_credenciales():
        nombre_usuario_ingresado = cuadro_usuario.get()
        contraseña_ingresada = cuadro_contraseña.get()

        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='proyecto_agil'
        )
        cursor = conexion.cursor()

        cursor.execute("SELECT idUsuario, rol FROM usuarios WHERE nombreUsuario = %s AND contraseña = %s",
                       (nombre_usuario_ingresado, contraseña_ingresada))
        usuario = cursor.fetchone()

        conexion.close()

        if usuario:
            id_usuario_actual = usuario[0]
            rol_usuario_actual = usuario[1]

            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            abrir_ventana_secundaria(login_window, id_usuario_actual, rol_usuario_actual)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    ventana.withdraw()

    login_window = tk.Toplevel(ventana)
    login_window.title("Log In")
    login_window.minsize(width=400, height=200)
    login_window.config(padx=30, pady=30)

    frame = tk.Frame(login_window)
    frame.pack(pady=10)

    tk.Label(frame, text="Nombre de Usuario:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
    cuadro_usuario = tk.Entry(frame)
    cuadro_usuario.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(frame, text="Contraseña:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
    cuadro_contraseña = tk.Entry(frame, show="*")
    cuadro_contraseña.grid(row=1, column=1, pady=5, padx=5)

    tk.Button(login_window, text="Iniciar Sesión", command=verificar_credenciales).pack(pady=10)
    tk.Button(login_window, text="Volver a Principal", command=lambda: volver_a_principal(login_window)).pack(pady=10)

def ingresar_datos_en_registro():
    global entry_rut, entry_nombre, entry_apellido, entry_nombre_usuario, entry_rol, entry_email, entry_contraseña

    rut = entry_rut.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    nombre_usuario = entry_nombre_usuario.get()
    rol = entry_rol.get()
    email = entry_email.get()
    contraseña = entry_contraseña.get()

    roles = {"Médico": 1, "Programador": 2, "Investigador": 3, "Infectólogo": 4, "Autoridad": 5}
    rol_numeric = roles.get(rol)

    usuario = Usuarios.Usuarios(nombre, apellido, nombre_usuario, rut, rol, email, contraseña)

    Modelo.CRUDUsuario.ingresar(usuario)

    messagebox.showinfo("Éxito", "Datos de usuario ingresados correctamente")

def open_signup_window():
    global entry_rut, entry_nombre, entry_apellido, entry_nombre_usuario, entry_rol, entry_email, entry_contraseña

    ventana.withdraw()

    signup_window = tk.Toplevel(ventana)
    signup_window.title("Sign Up")
    signup_window.minsize(width=400, height=200)
    signup_window.config(padx=30, pady=30)

    frame = tk.Frame(signup_window)
    frame.pack(pady=10)

    tk.Label(frame, text="RUT:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
    entry_rut = tk.Entry(frame)
    entry_rut.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(frame, text="Nombre:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
    entry_nombre = tk.Entry(frame)
    entry_nombre.grid(row=1, column=1, pady=5, padx=5)

    tk.Label(frame, text="Apellido:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
    entry_apellido = tk.Entry(frame)
    entry_apellido.grid(row=2, column=1, pady=5, padx=5)

    tk.Label(frame, text="Nombre de Usuario:").grid(row=3, column=0, pady=5, padx=5, sticky="w")
    entry_nombre_usuario = tk.Entry(frame)
    entry_nombre_usuario.grid(row=3, column=1, pady=5, padx=5)

    tk.Label(frame, text="Rol:").grid(row=4, column=0, pady=5, padx=5, sticky="w")
    roles = ["Médico", "Programador", "Investigador", "Infectólogo", "Autoridad"]
    entry_rol = tk.StringVar(frame)
    entry_rol.set(roles[0])
    tk.OptionMenu(frame, entry_rol, *roles).grid(row=4, column=1, pady=5, padx=5)

    tk.Label(frame, text="Email:").grid(row=5, column=0, pady=5, padx=5, sticky="w")
    entry_email = tk.Entry(frame)
    entry_email.grid(row=5, column=1, pady=5, padx=5)

    tk.Label(frame, text="Contraseña:").grid(row=6, column=0, pady=5, padx=5, sticky="w")
    entry_contraseña = tk.Entry(frame, show="*")
    entry_contraseña.grid(row=6, column=1, pady=5, padx=5)

    tk.Button(signup_window, text="Ingresar Datos", command=ingresar_datos_en_registro).pack(pady=10)
    tk.Button(signup_window, text="Volver a Principal", command=lambda: volver_a_principal(signup_window)).pack(pady=10)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("menu principal")
ventana.minsize(width=400, height=200)
ventana.config(padx=30, pady=30)

# Botón "Log In"
login_button = tk.Button(ventana, text="Log In", command=open_login_window)
login_button.pack(pady=10)

# Botón "Sign Up"
signup_button = tk.Button(ventana, text="Sign Up", command=open_signup_window)
signup_button.pack(pady=10)

ventana.mainloop()