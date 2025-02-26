from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Cliente, Empleado, Evento, Salone, Servicio



#Configuracion de la coneccion a la base de datos
DATABASE_URL = "postgresql://postgres:12345@localhost/hotel"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


#CRUD para la tabla Cliente
def listar_clientes():
    clientes = session.query(Cliente).all()
    return clientes

def agregar_cliente(nombre, correo, telefono = None, direccion = None):
    nuevo_cliente = Cliente(nombre = nombre, correo = correo, telefono = telefono, direccion = direccion)
    session.add(nuevo_cliente)
    session.commit()
    return nuevo_cliente

def eliminar_cliente(id_cliente):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        return True
    return False

def actualizar_cliente(id_cliente, nombre=None, correo=None, telefono=None, direccion=None):
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

def buscar_cliente(id_cliente):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    return cliente


#CRUD para la tabla Empleados

def listar_empleados():
    empleados = session.query(Empleado).all()
    return empleados

def agregar_empleado(nombre, rol):
    nuevo_empleado = Empleado(nombre = nombre, rol = rol)
    session.add(nuevo_empleado)
    session.commit()
    return nuevo_empleado   

def eliminar_empleado(id_empleado):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()
    if empleado:
        session.delete(empleado)
        session.commit()
        return True
    return False

def actualizar_empleado(id_empleado, nombre=None, rol=None):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()

def buscar_empleado(id_empleado):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()
    return empleado 

