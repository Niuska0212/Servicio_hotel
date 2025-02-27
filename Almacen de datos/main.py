from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Cliente, Empleado, Evento, Salone, Reservacione
from crud_operations import *
from tabulate import tabulate
from utils import *

#la funcion main junto con los primeros menus de al inicio, los puse mero abajo, por un error de lectura que olvide, pero no afecta en nada el funcionamiento del programa.


#Funciones de los diferentes menus de los 25 CRUD de las 5 tablas.
#Funcion menu de la tabla clientes
def menu_clientes():
    while True:
        print("\n --- Operaciones con Clientes ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Eliminar cliente")
        print("4. Modificar cliente")
        print("5. Buscar cliente")
        print("6. Listar eventos por fecha")
        print("7. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar clientes ---")
            Clientes = listar_clientes()
            if Clientes:
                for cliente in Clientes:
                    print(f"ID: {cliente.id_cliente} Nombre: {cliente.nombre} Correo: {cliente.correo} Telefono: {cliente.telefono} Direccion: {cliente.direccion}")
            else:
                print("No hay clientes registrados")
        elif opcion == "2":
            print("\n --- Agregar cliente ---")
            nombre = input("Nombre: ")
            correo = input("Correo: ") 
            telefono = input("Telefono (opcional): ") or None
            direccion = input("Direccion (opcional): ") or None
            nuevo_cliente = agregar_cliente(nombre, correo, telefono, direccion)
            if nuevo_cliente:
                print(f"Cliente {nuevo_cliente.nombre} agregado exitosamente")
            else:
                print("Error al agregar cliente")

        elif opcion == "3":
            print("\n --- Eliminar cliente ---")
            id_cliente = input("ID del cliente: ")
            cliente_eliminado = eliminar_cliente(id_cliente)
            if cliente_eliminado:
                print(f"Cliente {cliente_eliminado.nombre} eliminado exitosamente")
            else:
                print("Error al eliminar cliente")

        elif opcion == "4":
            print("\n --- Modificar cliente ---")
            print("Deja el campo vacio si no deseas modificarlo")
            print("Busca el cliente por ID")            
            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nuebo nombre Nombre: ") or None
            correo = input("Nuevo correo: ") or None
            telefono = input("Nuevo telefono (opcional): ") or None
            direccion = input("Nueva direccion (opcional): ") or None
            if actualizar_cliente(id_cliente, nombre, correo, telefono, direccion):
                print(f"Cliente {id_cliente} actualizado exitosamente")
            else:
                print("Error al actualizar cliente")
        elif opcion == "5":
            print("\n --- Buscar cliente por ID ---")
            id_cliente = int(input("ID del cliente: "))
            cliente = buscar_cliente(id_cliente)
            if cliente:
                print(f"ID: {cliente.id_cliente} Nombre: {cliente.nombre} Correo: {cliente.correo} Telefono: {cliente.telefono} Direccion: {cliente.direccion}")
            else:
                print("Cliente no encontrado")

        elif opcion == "6":
            print("\n --- Listar eventos por fecha ---")


        elif opcion == "7":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

#funcion menu de la tabla empleados
def menu_empleados():
    ROLES_VALIDOS = ['mesero', 'coordinador', 'chef', 'musico']
    while True:
        print("\n --- Operaciones con Empleados ---")
        print("1. Listar empleados")
        print("2. Agregar empleado")
        print("3. Eliminar empleado")
        print("4. Modificar empleado")
        print("5. Buscar empleado")
        print("6. Econtrar empleados disponibles por rol")
        print("7. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar empleados ---")
            empleados = listar_empleados()
            if empleados:
                for empleado in empleados:
                    print(f"ID: {empleado.id_empleado} Nombre: {empleado.nombre} Rol: {empleado.rol}")
            else:
                print("No hay empleados registrados")
        elif opcion == "2":
            print("\n --- Agregar empleado ---")
            nombre = input("Nombre: ")
            rol = input("Rol [mesero, coordinador, chef, musico]: ")
            if rol not in ROLES_VALIDOS:
                print("Rol no válido. Los roles válidos son: mesero, coordinador, chef, musico")
                continue
            nuevo_empleado = agregar_empleado(nombre, rol)
            if nuevo_empleado:
                print(f"Empleado {nuevo_empleado.nombre} agregado exitosamente")
            else:
                print("Error al agregar empleado")
        elif opcion == "3":
            print("\n --- Eliminar empleado ---")
            id_empleado = input("ID del empleado: ")
            empleado_eliminado = eliminar_empleado(id_empleado)
            if empleado_eliminado:
                print("Empleado eliminado exitosamente")
            else:
                print("Error al eliminar empleado")
        elif opcion == "4":
            print("\n --- Modificar empleado ---")
            print("Deja el campo vacío si no deseas modificarlo")
            id_empleado = int(input("ID del empleado: "))
            nombre = input("Nuevo nombre: ") or None
            rol = input("Nuevo rol: ") or None
            if rol and rol not in ROLES_VALIDOS:
                print("Rol no válido. Los roles válidos son: mesero, coordinador, chef, musico")
                continue
            if actualizar_empleado(id_empleado, nombre, rol):
                print(f"Empleado {id_empleado} actualizado exitosamente")
            else:
                print("Error al actualizar empleado")
        elif opcion == "5":
            print("\n --- Buscar empleado por ID ---")
            id_empleado = int(input("ID del empleado: "))
            empleado = buscar_empleado(id_empleado)
            if empleado:
                print(f"ID: {empleado.id_empleado} Nombre: {empleado.nombre} Rol: {empleado.rol}")
            else:
                print("Empleado no encontrado")

        elif opcion == "6":
            print("\n --- Encontrar empleados disponibles por rol en un rango de fechas ---")
            rol = input("Rol [mesero, coordinador, chef, musico]: ").strip().lower()
            if rol not in ROLES_VALIDOS:
                print("Rol no válido. Los roles válidos son: mesero, coordinador, chef, musico")
                continue
            fecha_inicio_str = input("Fecha de inicio (YYYY-MM-DD HH:MM:SS): ").strip()
            fecha_fin_str = input("Fecha de inicio (YYYY-MM-DD HH:MM:SS): ").strip()
           
            #Validar fechas
            fecha_inicio = validar_fecha(fecha_inicio_str)
            fecha_fin = validar_fecha(fecha_fin_str)
            
            if fecha_inicio is None or fecha_fin is None:
                print("Fecha no válida. Intente de nuevo con un formato YYYY-MM-DD HH:MM:SS.")
                continue
            if fecha_inicio >= fecha_fin:
                print("La fecha de inicio debe ser anterior a la fecha de fin.")
                continue
            encontrar_empleados_disponibles(rol, fecha_inicio, fecha_fin)

        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#funcion menu de la tabla eventos
def menu_eventos():
    EVENTOS_VALIDOS = ['conferencia', 'boda', 'reunion_corporativa', 'cena_privada']
    while True:
        print("\n --- Operaciones con Eventos ---")
        print("1. Listar eventos")
        print("2. Agregar evento")
        print("3. Eliminar evento")
        print("4. Modificar evento")
        print("5. Buscar evento")
        print("6. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar eventos ---")
            eventos = listar_eventos()
            if eventos:
                for evento in eventos:
                    print(f"ID: {evento.id_evento} Nombre: {evento.nombre_evento} Tipo: {evento.tipo_evento}")
            else:
                print("No hay eventos registrados")
        elif opcion == "2":
            print("\n --- Agregar evento ---")
            nombre_evento = input("Nombre: ")
            descripcion = input("Descripcion: ") or None
            tipo_evento = input("Tipo [conferencia, boda, reunion_corporativa, cena_privada]: ")
            if tipo_evento not in EVENTOS_VALIDOS:
                print("Tipo de evento no válido. Los tipos válidos son: conferencia, boda, reunion_corporativa, cena_privada")
                continue
            nuevo_evento = agregar_evento(nombre_evento, descripcion, tipo_evento)
            if nuevo_evento:
                print(f"Evento {nuevo_evento.nombre_evento} agregado exitosamente")
            else:
                print("Error al agregar evento")
        elif opcion == "3":
            print("\n --- Eliminar evento ---")
            id_evento = input("ID del evento: ")
            evento_eliminado = eliminar_evento(id_evento)
            if evento_eliminado:
                print("Evento eliminado exitosamente")
            else:
                print("Error al eliminar evento")
        elif opcion == "4":
            print("\n --- Modificar evento ---")
            print("Deja el campo vacío si no deseas modificarlo")
            id_evento = int(input("ID del evento: "))
            nombre_evento = input("Nuevo nombre: ") or None
            descripcion = input("Nueva descripcion: ") or None
            tipo_evento = input("Nuevo tipo: ") or None
            if tipo_evento and tipo_evento not in EVENTOS_VALIDOS:
                print("Tipo de evento no válido. Los tipos válidos son: conferencia, boda, reunion_corporativa, cena_privada")
                continue
            if actualizar_evento(id_evento, nombre_evento, descripcion, tipo_evento):
                print(f"Evento {id_evento} actualizado exitosamente")
            else:
                print("Error al actualizar evento")
        elif opcion == "5":
            print("\n --- Buscar evento por ID ---")
            id_evento = int

#funcion menu de la tabla salones
def menu_salones():
    while True:
        print("\n --- Operaciones con Salones ---")
        print("1. Listar salones")
        print("2. Agregar salon")
        print("3. Eliminar salon")
        print("4. Modificar salon")
        print("5. Buscar salon")
        print("6. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar salones ---")
            salones = listar_salones()
            if salones:
                for salon in salones:
                    print(f"ID: {salon.id_salon} Nombre: {salon.nombre_salon} Capacidad: {salon.capacidad}")
            else:
                print("No hay salones registrados")
        elif opcion == "2":
            print("\n --- Agregar salon ---")
            nombre_salon = input("Nombre: ")
            capacidad = int(input("Capacidad: "))
            descripcion = input("Descripcion: ") or None
            nuevo_salon = agregar_salon(nombre_salon, capacidad, descripcion)
            if nuevo_salon:
                print(f"Salon {nuevo_salon.nombre_salon} agregado exitosamente")
            else:
                print("Error al agregar salon")
        elif opcion == "3":
            print("\n --- Eliminar salon ---")
            id_salon = input("ID del salon: ")
            salon_eliminado = eliminar_salon(id_salon)
            if salon_eliminado:
                print("Salon eliminado exitosamente")
            else:
                print("Error al eliminar salon")
        elif opcion == "4":
            print("\n --- Modificar salon ---")
            print("Deja el campo vacío si no deseas modificarlo")
            id_salon = int(input("ID del salon: "))
            nombre_salon = input("Nuevo nombre: ") or None
            capacidad = int(input("Nueva capacidad: ")) or None
            descripcion = input("Nueva descripcion: ") or None
            if actualizar_salon(id_salon, nombre_salon, capacidad, descripcion):
                print(f"Salon {id_salon} actualizado exitosamente")
            else:
                print("Error al actualizar salon")
        elif opcion == "5":
            print("\n --- Buscar salon por ID ---")
            id_salon = int(input("ID del salon: "))
            salon = buscar_salon(id_salon)
            if salon:
                print(f"ID: {salon.id_salon} Nombre: {salon.nombre_salon} Capacidad: {salon.capacidad}")
            else:
                print("Salon no encontrado")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#ufncion menu de la tabla reservaciones
def menu_reservaciones():
    while True:
        print("\n --- Operaciones con Reservaciones ---")
        print("1. Listar reservaciones")
        print("2. Agregar reservacion")
        print("3. Eliminar reservacion")
        print("4. Modificar reservacion")
        print("5. Buscar reservacion")
        print("6. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar reservaciones ---")
            reservaciones = listar_reservaciones()
            if reservaciones:
                for reservacion in reservaciones:
                    print(f"ID: {reservacion.id_reservacion} Cliente: {reservacion.cliente.nombre} Fecha: {reservacion.fecha_reservacion} Salón: {reservacion.salon.nombre_salon}")
            else:
                print("No hay reservaciones registradas")
        elif opcion == "2":
            print("\n --- Agregar reservacion ---")
            id_cliente = int(input("ID del cliente: "))
            id_salon = int(input("ID del salon: "))
            fecha_reservacion = input("Fecha de la reservacion (YYYY-MM-DD): ")
            nueva_reservacion = agregar_reservacion(id_cliente, id_salon, fecha_reservacion)
            if nueva_reservacion:
                print(f"Reservacion {nueva_reservacion.id_reservacion} agregada exitosamente")
            else:
                print("Error al agregar reservacion")
        elif opcion == "3":
            print("\n --- Eliminar reservacion ---")
            id_reservacion = input("ID de la reservacion: ")
            reservacion_eliminada = eliminar_reservacion(id_reservacion)
            if reservacion_eliminada:
                print("Reservacion eliminada exitosamente")
            else:
                print("Error al eliminar reservacion")
        elif opcion == "4":
            print("\n --- Modificar reservacion ---")
            print("Deja el campo vacío si no deseas modificarlo")
            id_reservacion = int(input("ID de la reservacion: "))
            id_cliente = int(input("Nuevo ID del cliente: ")) or None
            id_salon = int(input("Nuevo ID del salon: ")) or None
            fecha_reservacion = input("Nueva fecha de la reservacion (YYYY-MM-DD): ") or None
            if actualizar_reservacion(id_reservacion, id_cliente, id_salon, fecha_reservacion):
                print(f"Reservacion {id_reservacion} actualizada exitosamente")
            else:
                print("Error al actualizar reservacion")    
        elif opcion == "5":
            print("\n --- Buscar reservacion por ID ---")
            id_reservacion = int(input("ID de la reservacion: "))
            reservacion = buscar_reservacion(id_reservacion)
            if reservacion:
                print(f"ID: {reservacion.id_reservacion} Cliente: {reservacion.cliente.nombre} Fecha: {reservacion.fecha_reservacion} Salón: {reservacion.salon.nombre_salon}")
            else:
                print("Reservacion no encontrada")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")




#Esta funcion sive solo para poner como el menu, no es necesario para el funcionamiento del programa.
def mostrar_menu():
    print("\n --- Menu Principal ---")
    print("1. Operaciones con Clientes")
    print("2. Operaciones con Empleados")
    print("3. Operaciones con Eventos")
    print("4. Operaciones con Salones")
    print("5. Operaciones con Reservaciones")
    print("6. Salir")

#Esta funcion es la que se encarga de seleccionar el menu que se desea ver
#aqui pueden poner las funciones de sus menus.
def seleccionar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            menu_eventos()
        elif opcion == "4":
            menu_salones()
        elif opcion == "5":
            menu_reservaciones()    
        elif opcion == "6":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

#Esta funcion es la que se encarga de conectar a la base de datos y cerrar la conexion
#al finalizar el programa.
if __name__ == "__main__":
    DATABASE_URL = "postgresql://postgres:12345@localhost/hotel"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    seleccionar_menu()

    session.close()