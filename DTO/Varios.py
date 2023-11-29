from datetime import datetime, date, time


def fecha_hoy():
    fecha = datetime.now()
    fecha_ = "{}-{}-{}".format(fecha.year, fecha.month, fecha.day)
    return fecha_


def hora():
    hora = datetime.now()
    hora_ = "{}:{}:{}".format(hora.hour, hora.minute, hora.second)
    return hora_