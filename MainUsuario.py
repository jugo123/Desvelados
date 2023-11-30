import DAO.CRUDUsuario
import DTO.Varios
from DTO import Conexion, Varios, Usuarios
import os


def menuPrincipal():
    os.system('cls')
    print("Fecha:{} - Hora:{}".format(Varios.fecha_hoy_esp(), Varios.hora()))
    print("=========================")
    print("    MENÚ PRINCIPAL")
    print("=========================")
    print("   1.- (C) INGRESAR")
    print("   2.- (R) MOSTRAR")
    print("   3.- (U) ACTUALIZAR")
    print("   4.- (D) ELIMINAR")
    print("   5.- (E) SALIR")
    print("=========================")


def ingresarDatos():
    os.system('cls')
    print("=========================")
    print(" 1.- INGRESAR DATOS USUARIO")
    print("=========================")
    while True:
        rut = input("Ingrese un RUT: ")
        if Varios.valida_rut(rut):
            break
        else:
            print("\nEl RUT ingresado no es Válido :(")
    # Se da inicio a la solicitud de los datos del uauario
    Nombre = input("Ingrese su Nommbre: ")
    Apellido = input("Ingrese su Apellido: ")
    Edad = input("Ingrese su Mail: ")
    Genero = int(input("Ingrese su genero [Hombre - Mujer]"))
    CorreoElectronico = input("Ingrese su Correo Electronico")
    Telefono = input("Ingrese su Telefono")
    # Creamos ao objeto de tipo Usuario
    usu = Usuarios.Usuarios(Nombre, Apellido , Edad, Genero, CorreoElectronico, Telefono, Varios.fecha_hoy_bd())
    # Solicitar al CRUD que realice la inserción
    DAO.CRUDUsuario.ingresar(usu)


def menuMostrar():
    os.system('cls')
    print("Fecha:{} - Hora:{}".format(Varios.fecha_hoy_esp(), Varios.hora()))
    print("=========================")
    print("    MENÚ MOSTRAR")
    print("=========================")
    print("   1.- Mostrar Todos")
    print("   2.- Mostrar Uno")
    print("   3.- Mostrar Parcial")
    print("   4.- Volver")
    print("=========================")


def mostrarTodos():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR TODOS")
    print("=========================")
    datos = DAO.CRUDUsuario.mostrarTodos()
    print("ID\tNombre\t\tApellido\tEdad\tGenero\t\t\t\tCorreoElectronico\t\t\tTelefono\t\t\t\tFechaRegistro")
    for dato in datos:
        print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".
              format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))


def mostrarUno():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR UNO")
    print("=========================")
    idUsuario = int(input("Ingrese Id Usuarioa a Consultar: "))
    dato = DAO.CRUDUsuario.mostrarParticular(idUsuario)
    if dato[6] == 1:
        estado = "Activo"
    else:
        estado = "Inactivo"
    print("=========================")
    print("   DATOS DEL USUARIO")
    print("=========================")
    print("ID                   {}".format(dato[0]))
    print("Nombre               {}".format(dato[1]))
    print("Apellido             {}".format(dato[2]))
    print("Edad                 {}".format(dato[3]))
    print("Genero               {}".format(dato[4]))
    print("CorreoElectronico    {}".format(dato[5]))
    print("Telefono             {}".format(dato[6]))
    print("FechaRegistro        {}".format(dato[7]))

    input("\nPresione Enter para continuar")


def mostrarParcial():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR PARCIAL")
    print("=========================")
    cant = int(input("Ingrese Cantidad de Datos a Mostrar: "))
    datos = DAO.CRUDUsuario.mostrarParcial(cant)
    print("ID\tNombre\t\tApellido\tEdad\tGenero\t\t\t\tCorreoElectronico\t\t\tTelefono\t\t\t\tFechaRegistro")
    for dato in datos:
        print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".
              format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))


def modificarDatos():
    os.system('cls')
    listanuevos = []
    print("=========================")
    print("    MODIFICAR DATOS")
    print("=========================")
    mostrarTodos()
    idMod = int(input("\nIngrese un IdUsuario a Modificar: "))
    dato = DAO.CRUDUsuario.mostrarParticular(idMod)

    print("Id Usuario                   :{}".format(dato[0]))
    listanuevos.append(dato[0])
    # Cambiar Nombre
    print("Nombre Usuario               :{}".format(dato[1]))
    op = input("Desea Cambiar el Nombre [si-no]:")
    if op.lower() == "si":
        nombreNuevo = input("Ingrese Nombre: ")
        listanuevos.append(nombreNuevo)
    else:
        listanuevos.append(dato[1])
    # Cambiar Apellido
    print("Apellido Usuario             :{}".format(dato[2]))
    op = input("Desea Cambiar el Apellido [si-no]:")
    if op.lower() == "si":
        apellidoNuevo = input("Ingrese Apellido: ")
        listanuevos.append(apellidoNuevo)
    else:
        listanuevos.append(dato[2])

    # Modificar Edad
    print("Edad Usuario               :{}".format(dato[3]))
    op = input("Desea Cambiar la Edad [si-no]:")
    if op.lower() == "si":
        Edadnueva = input("Ingrese Mail: ")
        listanuevos.append(Edadnueva)
    else:
        listanuevos.append(dato[3])
    # Modificar Genero
    print("Genero Usuario               :{}".format(dato[4]))
    op = input("Desea Cambiar el Genero [si-no]:")
    if op.lower() == "si":
        GeneroNuevo = input("Ingrese Genero: ")
        listanuevos.append(GeneroNuevo)
    else:
        listanuevos.append(dato[4])

    # Modificar CorreoElectronico
    print("CorreoElectronico Usuario               :{}".format(dato[5]))
    op = input("Desea Cambiar el CorreoElectronico [si-no]:")
    if op.lower() == "si":
        CorreoNuevo = input("Ingrese CorreoElectronico: ")
        listanuevos.append(CorreoNuevo)
    else:
        listanuevos.append(dato[5])

    # Modificar Telefono
    print("Telefono Usuario               :{}".format(dato[6]))
    op = input("Desea Cambiar el Telefono [si-no]:")
    if op.lower() == "si":
        TelefonoNuevo = input("Ingrese Telefono: ")
        listanuevos.append(TelefonoNuevo)
    else:
        listanuevos.append(dato[6])


    # Fecha y la Hora
    listanuevos.append(DTO.Varios.fecha_hoy_bd())
    listanuevos.append(DTO.Varios.hora())
    DAO.CRUDUsuario.modificar(listanuevos)


def eliminarDatos():
    os.system('cls')
    print("=========================")
    print("    ELIMINAR USUARIO")
    print("=========================")
    mostrarTodos()
    idEliminar = int(input("Ingrese Id Usuario a Eliminar: "))
    DAO.CRUDUsuario.eliminar(idEliminar)


def mostrar():
    while True:
        menuMostrar()
        op2 = int(input("Ingrese una Opción: "))
        if op2 == 1:
            mostrarTodos()
        elif op2 == 2:
            mostrarUno()
        elif op2 == 3:
            mostrarParcial()
        if op2 == 4:
            break
        else:
            print("Opción fuera de Rango :(")


while True:
    menuPrincipal()
    op = int(input("Ingrese una Opción: "))
    if op == 1:
        ingresarDatos()
    elif op == 2:
        mostrar()
    elif op == 3:
        modificarDatos()
    elif op == 4:
        eliminarDatos()
    if op == 5:
        op2 = input("Desea Salir[SI/NO]: ")
        if op2.upper() == "SI":
            exit()
    else:
        print("Opción Fuera de Rango :(")