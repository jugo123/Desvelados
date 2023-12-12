import tkinter as tk
import pymysql
from DAO import CRUDUsuario  # Asegúrate de que la estructura de tus directorios coincida

# Función para verificar el nombre de usuario y la contraseña
def verificar_credenciales():
    nombre_usuario_ingresado = cuadro_usuario.get()
    contraseña_ingresada = cuadro_contraseña.get()

    # Conectar a la base de datos MySQL
    conexion = pymysql.connect(
        host='localhost',
        user = 'root',
        password = '',
        db = 'proyecto_agil'
        )
    cursor = conexion.cursor()

    # Realizar una consulta para obtener los usuarios con las credenciales ingresadas
    cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = %s AND contraseña = %s",
                   (nombre_usuario_ingresado, contraseña_ingresada))
    usuarios = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    conexion.close()

    if usuarios:
        etiqueta_resultado.config(text="¡Credenciales correctas!")
    else:
        etiqueta_resultado.config(text="¡Usuario o contraseña incorrectos!")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Verificar Credenciales")
ventana.minsize(width=400, height=200)
ventana.config(padx=30, pady=30)

# Crear un cuadro de texto para el nombre de usuario
cuadro_usuario = tk.Entry(ventana, width=30)
cuadro_usuario.pack(pady=10)

# Crear un cuadro de texto para la contraseña
cuadro_contraseña = tk.Entry(ventana, show="*", width=30)  # El parámetro show="*" oculta la contraseña
cuadro_contraseña.pack(pady=10)

# Crear un botón para verificar las credenciales
boton_verificar = tk.Button(ventana, text="Log in", command=verificar_credenciales)
boton_verificar.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Añadir aquí el resto de tu interfaz Tkinter y lógica de la aplicación


# Iniciar el bucle principal
ventana.mainloop()
