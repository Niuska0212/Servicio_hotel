# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from modelos import Cliente, Empleado, Evento, Salone, Servicio, Reservacione, AsignacionSalone
from sqlalchemy import and_
from tabulate import tabulate

## NIUSKAAAAAA ##
## No hace falta poner la conexión a la base de datos aqui jeje, este archivo solo tiene que tener las funciones CRUD
## y las funciones que necesiten la conexión a la base de datos, que se pasen como argumento a la función  😊 ##
## Nada más importa las funciones CRUD en el archivo main.py y ya puedes usarlas con la conexión a la base de datos que creaste en main.py ##
## :D ##


#CRUD para la tabla Cliente
def listar_clientes(session):
    clientes = session.query(Cliente).all()
    return clientes

def agregar_cliente(session, nombre, correo, telefono = None, direccion = None):
    nuevo_cliente = Cliente(nombre = nombre, correo = correo, telefono = telefono, direccion = direccion)
    session.add(nuevo_cliente)
    session.commit()
    return nuevo_cliente

def eliminar_cliente(session, id_cliente):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        return True
    return False

def actualizar_cliente(session, id_cliente, nombre=None, correo=None, telefono=None, direccion=None):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    if cliente:
        if nombre:
            cliente.nombre = nombre
        if correo:
            cliente.correo = correo
        if telefono:
            cliente.telefono = telefono
        if direccion:
            cliente.direccion = direccion
        session.commit()
        return True
    return False

def buscar_cliente(session, id_cliente):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    return cliente


#CRUD para la tabla Empleados

def listar_empleados(session):
    empleados = session.query(Empleado).all()
    return empleados

def agregar_empleado(session, nombre, rol):
    nuevo_empleado = Empleado(nombre = nombre, rol = rol)
    session.add(nuevo_empleado)
    session.commit()
    return nuevo_empleado   

def eliminar_empleado(session, id_empleado):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()
    if empleado:
        session.delete(empleado)
        session.commit()
        return True
    return False

def actualizar_empleado(session, id_empleado, nombre=None, rol=None):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()

def buscar_empleado(session, id_empleado):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()
    return empleado 

## FUNCIÓN PARA LISTAR EVENTOS POR FECHA ##
def listar_eventos_por_fecha(session, fecha):
    resultados = (
        session.query(Evento.nombre_evento, Evento.tipo_evento, Reservacione.fecha_evento, 
                      Cliente.nombre.label("cliente_nombre"), Salone.nombre_salon)
        .join(Reservacione, Evento.id_evento == Reservacione.id_evento)
        .join(Cliente, Reservacione.id_cliente == Cliente.id_cliente)
        .join(AsignacionSalone, Reservacione.id_reservacion == AsignacionSalone.id_reservacion)
        .join(Salone, AsignacionSalone.id_salon == Salone.id_salon)
        .filter(
            and_(
                Reservacione.fecha_evento >= fecha,
                Reservacione.fecha_evento < fecha + ' 23:59:59',
                Reservacione.estado_reservacion == 'activa'
            )
        )
        .all()
    )

    eventos = []
    for nombre_evento, tipo_evento, fecha_evento, cliente_nombre, nombre_salon in resultados:
        eventos.append({
            "nombre_evento": nombre_evento,
            "tipo_evento": tipo_evento,
            "fecha_evento": fecha_evento.strftime('%Y-%m-%d %H:%M:%S'),
            "cliente": cliente_nombre,
            "ubicacion": nombre_salon
        })

    if not eventos:
        return "No hay eventos programados para la fecha indicada"

    return tabulate(eventos, headers="keys", tablefmt="fancy_grid")