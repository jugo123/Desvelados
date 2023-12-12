import tkinter as tk
import pymysql
from tkinter import messagebox
import DAO.CRUDUsuario
from DTO import Usuarios, Varios


def salir_del_usuario_actual(ventana_actual):
    # Mostrar la ventana principal
    ventana.deiconify()

    # Cerrar la ventana actual
    ventana_actual.destroy()


def abrir_ventana_secundaria(ventana_actual):
    # Ocultar la ventana actual
    ventana_actual.withdraw()

    # Crear y mostrar la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.minsize(width=400, height=200)
    ventana_secundaria.config(padx=30, pady=30)

    # Botón para salir del usuario actual
    tk.Button(ventana_secundaria, text="Salir del Usuario",command=lambda: salir_del_usuario_actual(ventana_secundaria)).pack(pady=10)


def volver_a_principal(ventana_actual):
    # Mostrar la ventana principal
    ventana.deiconify()

    # Cerrar la ventana actual
    ventana_actual.destroy()

def open_login_window():
    def verificar_credenciales():
        nombre_usuario_ingresado = cuadro_usuario.get()
        contraseña_ingresada = cuadro_contraseña.get()

        # Conectar a la base de datos MySQL
        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='proyecto_agil'
        )
        cursor = conexion.cursor()

        # Realizar una consulta para obtener los usuarios con las credenciales ingresadas
        cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = %s AND contraseña = %s",
                       (nombre_usuario_ingresado, contraseña_ingresada))
        usuarios = cursor.fetchall()

        # Cerrar la conexión a la base de datos
        conexion.close()

        if usuarios:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            abrir_ventana_secundaria(login_window)  # llevara a una ventana secundaria al ingersar correctamente
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # Ocultar la ventana principal
    ventana.withdraw()

    login_window = tk.Toplevel(ventana)
    login_window.title("Log In")
    login_window.minsize(width=400, height=200)
    login_window.config(padx=30, pady=30)

    # Campos de entrada para nombre de usuario y contraseña
    tk.Label(login_window, text="Nombre de Usuario:").pack(pady=5)
    cuadro_usuario = tk.Entry(login_window)
    cuadro_usuario.pack(pady=5)

    tk.Label(login_window, text="Contraseña:").pack(pady=5)
    cuadro_contraseña = tk.Entry(login_window, show="*")
    cuadro_contraseña.pack(pady=5)

    # Botón de inicio de sesión
    tk.Button(login_window, text="Iniciar Sesión", command=verificar_credenciales).pack(pady=10)

    # Botón para volver a la ventana principal y cerrar la ventana de registro
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

    # Mapear roles a valores numéricos (ajusta según tus necesidades)
    roles = {"Médico": 1, "Programador": 2, "Investigador": 3, "Infectólogo": 4, "Autoridad": 5}
    rol_numeric = roles.get(rol)

    # Crear un objeto de tipo Usuario
    usuario = Usuarios.Usuarios(nombre, apellido, nombre_usuario, rut, rol, email, contraseña)

    # Solicitar al CRUD que realice la inserción (ajusta esto según tu implementación real)
    DAO.CRUDUsuario.ingresar(usuario)

    messagebox.showinfo("Éxito", "Datos de usuario ingresados correctamente")

def open_signup_window():
    global entry_rut, entry_nombre, entry_apellido, entry_nombre_usuario, entry_rol, entry_email, entry_contraseña

    # Ocultar la ventana principal
    ventana.withdraw()

    signup_window = tk.Toplevel(ventana)
    signup_window.title("Sign Up")
    signup_window.minsize(width=400, height=200)
    signup_window.config(padx=30, pady=30)

    # Campos de entrada para los datos del usuario
    tk.Label(signup_window, text="RUT:").pack(pady=5)
    entry_rut = tk.Entry(signup_window)
    entry_rut.pack(pady=5)

    tk.Label(signup_window, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(signup_window)
    entry_nombre.pack(pady=5)

    tk.Label(signup_window, text="Apellido:").pack(pady=5)
    entry_apellido = tk.Entry(signup_window)
    entry_apellido.pack(pady=5)

    tk.Label(signup_window, text="Nombre de Usuario:").pack(pady=5)
    entry_nombre_usuario = tk.Entry(signup_window)
    entry_nombre_usuario.pack(pady=5)

    tk.Label(signup_window, text="Rol:").pack(pady=5)
    roles = ["Médico", "Programador", "Investigador", "Infectólogo", "Autoridad"]
    entry_rol = tk.StringVar(signup_window)
    entry_rol.set(roles[0])  # Valor predeterminado
    tk.OptionMenu(signup_window, entry_rol, *roles).pack(pady=5)

    tk.Label(signup_window, text="Email:").pack(pady=5)
    entry_email = tk.Entry(signup_window)
    entry_email.pack(pady=5)

    tk.Label(signup_window, text="Contraseña:").pack(pady=5)
    entry_contraseña = tk.Entry(signup_window, show="*")
    entry_contraseña.pack(pady=5)

    # Botón para ingresar los datos del usuario
    tk.Button(signup_window, text="Ingresar Datos", command=ingresar_datos_en_registro).pack(pady=10)

    # Botón para volver a la ventana principal y cerrar la ventana de registro
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

# Inicia el bucle principal de la aplicación
ventana.mainloop()
