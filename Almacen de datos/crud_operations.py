from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Cliente, Empleado, Evento, Salone, Reservacione,AsignacionEmpleado, AsignacionSalone
from sqlalchemy import and_
from tabulate import tabulate
import datetime


#Configuracion de la coneccion a la base de datos
#DATABASE_URL = "postgresql://postgres:12345@localhost/hotel"
#engine = create_engine(DATABASE_URL)
#Session = sessionmaker(bind=engine)
#session = Session()


#CRUD para la tabla Cliente
def listar_clientes(session):
    clientes = session.query(Cliente).all()
    if clientes:
        return clientes
    print("No hay clientes registrados.")
    return None

def agregar_cliente(session,nombre, correo, telefono = None, direccion = None):
    if not nombre or not correo:
        print("El nombre y correo son obligatorios.")
        return None
    try:
        nuevo_cliente = Cliente(nombre = nombre, correo = correo, telefono = telefono, direccion = direccion)
        session.add(nuevo_cliente)
        session.commit()
        print("Cliente agregado correctamente.")
        return nuevo_cliente
    except Exception as e:
        print("Error al agregar el cliente: {e}")
        return None
    

def eliminar_cliente(session, id_cliente):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    if cliente:
        try:
            session.delete(cliente)
            session.commit()
            print("Cliente eliminado correctamente.")
            return True
        except Exception as e:
            print(f"Error al eliminar el cliente con ID {id_cliente}: {e}")
            return False
    print("Cliente no encontrado.")
    return False

def actualizar_cliente(session, id_cliente, nombre=None, correo=None, telefono=None, direccion=None):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    if cliente:
        try:
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
        except Exception as e:
            print("Error al actualizar el cliente:", e)
            return False
    print("Cliente no encontrado.")
    return False

def buscar_cliente(session, id_cliente):
    cliente = session.query(Cliente).filter_by(id_cliente = id_cliente).first()
    if cliente:
        return cliente
    print("Cliente no encontrado.")
    return None



#CRUD para la tabla Empleados

def listar_empleados(session):
    empleados = session.query(Empleado).all()
    if empleados:
        return empleados
    print("No hay empleados registrados.")
    return None

def agregar_empleado(session, nombre, rol):
    if not nombre or not rol:
        print("El nombre y el rol son obligatorios.")   
        return None
    try:
        nuevo_empleado = Empleado(nombre = nombre, rol = rol)
        session.add(nuevo_empleado)
        session.commit()
        print("Empleado agregado correctamente.")
        return nuevo_empleado   
    except Exception as e:
        print("Error al agregar el empleado:", e)
        return None

def eliminar_empleado(session, id_empleado):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()
    if empleado:
        try:
            session.delete(empleado)
            session.commit()
            print("Empleado eliminado correctamente.")
            return True
        except Exception as e:
            print(f"Error al eliminar el empleado con ID {id_empleado}: {e}")
            return False
    print("Empleado no encontrado.")
    return False

def actualizar_empleado(session, id_empleado, nombre=None, rol=None):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()
    if empleado:
        try:
            if nombre:
                empleado.nombre = nombre
            if rol:
                empleado.rol = rol
            session.commit()
            return True
        except Exception as e:
            print("Error al actualizar el empleado:", e)
            return False
    print("Empleado no encontrado.")
    return False

def buscar_empleado(session, id_empleado):
    empleado = session.query(Empleado).filter_by(id_empleado = id_empleado).first()
    if empleado:
        return empleado
    print("Empleado no encontrado.")
    return None


#CRUD para la tabla Eventos

def listar_eventos(session):
    eventos = session.query(Evento).all()
    if eventos:
        return eventos
    print("No hay eventos registrados.")
    return None

def agregar_evento(session, nombre_evento, descripcion, tipo_evento):
    if not nombre_evento or not descripcion or not tipo_evento:
        print("El nombre, descripcion y tipo de evento son obligatorios.")
        return None
    try:
        nuevo_evento = Evento(nombre_evento = nombre_evento, descripcion = descripcion, tipo_evento = tipo_evento)
        session.add(nuevo_evento)
        session.commit()
        print("Evento agregado correctamente.") 
        return nuevo_evento
    except Exception as e:
        print("Error al agregar el evento:", e) 
        return None
    

def eliminar_evento(session, id_evento):
    evento = session.query(Evento).filter_by(id_evento = id_evento).first()
    if evento:
        try:
            session.delete(evento)
            session.commit()
            print("Evento eliminado correctamente.")
            return True
        except Exception as e:
            print(f"Error al eliminar el evento con ID {id_evento}: {e}")
            return False
    print("Evento no encontrado.")
    return False

def actualizar_evento(session, id_evento, nombre_evento=None, descripcion=None, tipo_evento=None):
    evento = session.query(Evento).filter_by(id_evento = id_evento).first()
    if evento:
        try:
            if nombre_evento:
                evento.nombre_evento = nombre_evento
            if descripcion:
                evento.descripcion = descripcion
            if tipo_evento:
                evento.tipo_evento = tipo_evento
            session.commit()
            print("Evento actualizado correctamente.")
            return True
        except Exception as e:
            print("Error al actualizar el evento:", e)
            return False
    print("Evento no encontrado.")
    return False

def buscar_evento(session, id_evento):
    evento = session.query(Evento).filter_by(id_evento = id_evento).first()
    if evento:
        return evento
    print("Evento no encontrado.")
    return None


#Crud para la tabla Salones
def listar_salones(session):
    salones = session.query(Salone).all()
    if salones:
        return salones
    print("No hay salones registrados.")
    return None

def agregar_salon(session,nombre_salon, capacidad, descripcion):
    if not nombre_salon or not capacidad or not descripcion:
        print("El nombre, capacidad y descripcion son obligatorios.")
        return None
    try:
        nuevo_salon = Salone(nombre_salon = nombre_salon, capacidad = capacidad, descripcion = descripcion)
        session.add(nuevo_salon)
        session.commit()
        print("Salon agregado correctamente.")
        return nuevo_salon
    except Exception as e:
        print("Error al agregar el salon:", e)
        return None
    
def eliminar_salon(session,id_salon):
    salon = session.query(Salone).filter_by(id_salon = id_salon).first()
    if salon:
        try:
            session.delete(salon)
            session.commit()
            print("Salon eliminado correctamente.")
            return True
        except Exception as e:
            print(f"Error al eliminar el salon con ID {id_salon}: {e}")
            return False
    print("Salon no encontrado.")
    return False

def actualizar_salon(session, id_salon, nombre_salon=None, capacidad=None, descripcion=None):
    salon = session.query(Salone).filter_by(id_salon = id_salon).first()   
    if salon:
        try:
            if nombre_salon:
                salon.nombre_salon = nombre_salon
            if capacidad:
                salon.capacidad = capacidad
            if descripcion:
                salon.descripcion = descripcion
            session.commit()
            print("Salon actualizado correctamente.")
            return True
        except Exception as e:
            print("Error al actualizar el salon:", e)
            return False
    print("Salon no encontrado.")
    return False

def buscar_salon(session, id_salon):
    salon = session.query(Salone).filter_by(id_salon = id_salon).first()
    if salon:
        return salon
    print("Salon no encontrado.")
    return None

#CRUD para la table reservaciones
def listar_reservaciones(session):
    reservaciones = session.query(Reservacione).all()
    if reservaciones:
        return reservaciones
    print("No hay reservaciones registradas.")
    return None

def agregar_reservacion(session, id_cliente, id_evento, id_salon, fecha_reservacion, fecha_evento, hora_evento, cantidad_personas):
    if not id_cliente or not id_evento or not id_salon or not fecha_reservacion or not fecha_evento or not hora_evento or not cantidad_personas:
        print("El id del cliente, id del evento, id del salon, fecha de reservacion, fecha del evento, hora del evento y cantidad de personas son obligatorios.")
        return None
    try:
        nueva_reservacion = Reservacione(id_cliente = id_cliente, id_evento = id_evento, id_salon = id_salon, fecha_reservacion = fecha_reservacion, fecha_evento = fecha_evento, hora_evento = hora_evento, cantidad_personas = cantidad_personas)
        session.add(nueva_reservacion)
        session.commit()
        print("Reservacion agregada correctamente.")
        return nueva_reservacion
    except Exception as e:
        print("Error al agregar la reservacion:", e)
        return None

 ##Comente la funcion de eliminar, para mas bien cancelar la reservacion
 #y no borrarlo, porque asi estaba en la base de datos

#def eliminar_reservacion(session, id_reservacion):
#    reservacion = session.query(Reservacione).filter_by(id_reservacion = id_reservacion).first()
#    if reservacion:
#        try:
#            session.delete(reservacion)
#            session.commit()
#            print("Reservacion eliminada correctamente.")
#            return True
#        except Exception as e:
#            print(f"Error al eliminar la reservacion con ID {id_reservacion}: {e}")
#            return False
#    print("Reservacion no encontrada.")
#    return False

def cancelar_reservacion(session, id_reservacion):
    reservacion = session.query(Reservacione).filter_by(id_reservacion=id_reservacion).first()
    if reservacion:
        try:
            reservacion.estado_reservacion = 'cancelada'
            reservacion.fecha_cancelacion = datetime.datetime.now()  # Asegúrate de importar datetime
            session.commit()
            print("Reservacion cancelada correctamente.")
            return True
        except Exception as e:
            print(f"Error al cancelar la reservacion con ID {id_reservacion}: {e}")
            return False
    print("Reservacion no encontrada.")
    return False


def actualizar_reservacion(session, id_reservacion, id_cliente=None, id_evento=None, id_salon=None, fecha_reservacion=None, fecha_evento=None, hora_evento=None, cantidad_personas=None):
    reservacion = session.query(Reservacione).filter_by(id_reservacion = id_reservacion).first()
    if reservacion:
        try:
            if id_cliente:
                reservacion.id_cliente = id_cliente
            if id_evento:
                reservacion.id_evento = id_evento
            if id_salon:
                reservacion.id_salon = id_salon
            if fecha_reservacion:
                reservacion.fecha_reservacion = fecha_reservacion
            if fecha_evento:
                reservacion.fecha_evento = fecha_evento
            if hora_evento:
                reservacion.hora_evento = hora_evento
            if cantidad_personas:
                reservacion.cantidad_personas = cantidad_personas
            session.commit()
            print("Reservacion actualizada correctamente.")
            return True
        except Exception as e:
            print("Error al actualizar la reservacion:", e)
            return False
    print("Reservacion no encontrada.")
    return False

def buscar_reservacion(session, id_reservacion):
    reservacion = session.query(Reservacione).filter_by(id_reservacion = id_reservacion).first()
    if reservacion:
        return reservacion
    print("Reservacion no encontrada.")
    return None



#Funcion para encontrar empleados disponibles por fechas
def encontrar_empleados_disponibles(session, rol, fecha_inicio, fecha_fin):
    try:
        #roles
        empleados_disponibles = session.query(Empleado).filter(Empleado.rol == rol).all()
        empleados_finales = []

        #disponibilidad
        for empleado in empleados_disponibles:
            asignaciones = session.query(AsignacionEmpleado).filter(
                AsignacionEmpleado.id_empleado == empleado.id_empleado
            ).all()

            disponible = True
            for asignacion in asignaciones:
                if not (asignacion.fecha_fin <= fecha_inicio or asignacion.fecha_inicio >= fecha_fin):
                    disponible = False
                    break 

            if disponible:
                empleados_finales.append(empleado)

        if empleados_finales:
            print(f"\nEmpleados disponibles para el rol '{rol}' entre {fecha_inicio} y {fecha_fin}:")
            for empleado in empleados_finales:
                print(f"ID: {empleado.id_empleado}, Nombre: {empleado.nombre}")
        else:
            print(f"\nNo hay empleados disponibles para el rol '{rol}' entre {fecha_inicio} y {fecha_fin}.")

    except Exception as e:
        print(f"\nError inesperado: {e}")



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