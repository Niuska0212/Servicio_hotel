from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crud_operations import *
from utils import *

#la funcion main junto con los primeros menus de al inicio, los puse mero abajo, por un error de lectura que olvide, pero no afecta en nada el funcionamiento del programa.
#corregi los session, ya todas las funciones lo tienen.
#asi como validacion en las id con valores id para que sean datos reales.
#y tambien la validacion de las fechas en la funcion de encontrar empleados disponibles por rol en un rango de fechas.
#y tambien la validacion de los roles en la funcion de agregar empleado.

#modifique la funcion de ELIMINAR RESERVACION, porque en la base de datos es cancelada o activa
#y es mejor que en la base de datos este de esa forma.



#Funciones de los diferentes menus de los 25 CRUD de las 5 tablas. Mas las demas funciones.
#Funcion menu de la tabla clientes
def menu_clientes(session):
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
            Clientes = listar_clientes(session)
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
            nuevo_cliente = agregar_cliente(session, nombre, correo, telefono, direccion)
            if nuevo_cliente:
                print(f"Cliente {nuevo_cliente.nombre} agregado exitosamente")
            else:
                print("Error al agregar cliente")
        elif opcion == "3":
            print("\n --- Eliminar cliente ---")
            id_cliente = input("ID del cliente: ")
            cliente = buscar_cliente(id_cliente)  # Verificar si el cliente existe

            if cliente:
                print(f"¿Deseas eliminar al cliente {cliente.nombre} (ID: {cliente.id_cliente})? (S/N)")
                confirmacion = input("Respuesta: ").lower()

                if confirmacion == "s":
                    cliente_eliminado = eliminar_cliente(id_cliente)
                    if cliente_eliminado:
                        print(f"Cliente {cliente_eliminado.nombre} eliminado exitosamente")
                    else:
                        print("Error al eliminar cliente")
                else:
                    print("Eliminación cancelada")
            else:
                print("Cliente no encontrado.")
            
        elif opcion == "4":
            print("\n --- Modificar cliente ---")
            print("Deja el campo vacio si no deseas modificarlo")
            print("Busca el cliente por ID")
            try:
                id_cliente = int(input("ID del cliente: "))
            except ValueError:
                print("ID no valido. Intente de nuevo.")
                continue

            nombre = input("Nuevo nombre: ") or None
            correo = input("Nuevo correo: ") or None
            telefono = input("Nuevo telefono (opcional): ") or None
            direccion = input("Nueva direccion (opcional): ") or None
            if actualizar_cliente(session, id_cliente, nombre, correo, telefono, direccion):
                print(f"Cliente {id_cliente} actualizado exitosamente")
            else:
                print("Error al actualizar cliente")
        elif opcion == "5":
            print("\n --- Buscar cliente por ID ---")
            try:
                id_cliente = int(input("ID del cliente: "))
            except ValueError:
                print("ID no valido. Intente de nuevo.")
                continue

            cliente = buscar_cliente(session, id_cliente)
            if cliente:
                print(f"ID: {cliente.id_cliente} Nombre: {cliente.nombre} Correo: {cliente.correo} Telefono: {cliente.telefono} Direccion: {cliente.direccion}")
            else:
                print("Cliente no encontrado")
        elif opcion == "6":
            print("\n --- Listar eventos por fecha ---")
            # Implementar la función de listar eventos por fecha
            fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
            try:
                eventos = listar_eventos_por_fecha(session, fecha)
                print(eventos)
            except Exception as e:
                print(f"Error al listar eventos!, procura escribir la fecha en el formato correcto YYYY-MM-DD") 
        elif opcion == "7":
            print("Regresando al menu principal")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

#funcion menu de la tabla empleados
def menu_empleados(session):
    ROLES_VALIDOS = ['mesero', 'coordinador', 'chef', 'musico']
    while True:
        print("\n --- Operaciones con Empleados ---")
        print("1. Listar empleados")
        print("2. Agregar empleado")
        print("3. Eliminar empleado")
        print("4. Modificar empleado")
        print("5. Buscar empleado")
        print("6. Encontrar empleados disponibles por rol en un rango de fechas")
        print("7. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar empleados ---")
            empleados = listar_empleados(session)
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
            nuevo_empleado = agregar_empleado(session, nombre, rol)
            if nuevo_empleado:
                print(f"Empleado {nuevo_empleado.nombre} agregado exitosamente")
            else:
                print("Error al agregar empleado")
        elif opcion == "3":
            print("\n --- Eliminar empleado ---")
            id_empleado = input("ID del empleado: ")
            empleado = buscar_empleado(session, id_empleado)  # Verificar si el empleado existe

            if empleado:
                print(f"¿Deseas eliminar al empleado {empleado.nombre} (ID: {empleado.id_empleado})? (S/N)")
                confirmacion = input("Respuesta: ").lower()  # Convertir a minúscula para evitar problemas

                if confirmacion == "s":  # Si el usuario confirma con "S"
                    empleado_eliminado = eliminar_empleado(session, id_empleado)
                    if empleado_eliminado:
                        print(f"Empleado {empleado_eliminado.nombre} eliminado exitosamente")
                    else:
                        print("Error al eliminar empleado")
                else:  # Si el usuario no confirma
                    print("Eliminación cancelada")
            else:
                print("Empleado no encontrado.")
        elif opcion == "4":
            print("\n --- Modificar empleado ---")
            print("Deja el campo vacío si no deseas modificarlo")
            try:
                id_empleado = int(input("ID del empleado: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue

            nombre = input("Nuevo nombre: ") or None
            rol = input("Nuevo rol: ") or None
            if rol and rol not in ROLES_VALIDOS:
                print("Rol no válido. Los roles válidos son: mesero, coordinador, chef, musico")
                continue
            if actualizar_empleado(session, id_empleado, nombre, rol):
                print(f"Empleado {id_empleado} actualizado exitosamente")
            else:
                print("Error al actualizar empleado")
        elif opcion == "5":
            print("\n --- Buscar empleado por ID ---")
            try:
                id_empleado = int(input("ID del empleado: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue

            empleado = buscar_empleado(session, id_empleado)
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
            fecha_fin_str = input("Fecha de finalizacion (YYYY-MM-DD HH:MM:SS): ").strip()
           
            # Validar fechas
            fecha_inicio = validar_fecha(fecha_inicio_str)
            fecha_fin = validar_fecha(fecha_fin_str)

            if fecha_inicio is None or fecha_fin is None:
                print("Fecha no válida. Intente de nuevo con un formato YYYY-MM-DD HH:MM:SS.")
                continue
            if fecha_inicio >= fecha_fin:
                print("La fecha de inicio debe ser anterior a la fecha de fin.")
                continue
            encontrar_empleados_disponibles(session, rol, fecha_inicio, fecha_fin)
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#funcion menu de la tabla eventos
def menu_eventos(session):
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
            eventos = listar_eventos(session)
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
            nuevo_evento = agregar_evento(session, nombre_evento, descripcion, tipo_evento)
            if nuevo_evento:
                print(f"Evento {nuevo_evento.nombre_evento} agregado exitosamente")
            else:
                print("Error al agregar evento")
        elif opcion == "3":
            print("\n --- Eliminar evento ---")
            id_evento = input("ID del evento: ")
            evento = buscar_evento(session, id_evento)  # Verificar si el evento existe

            if evento:
                print(f"¿Deseas eliminar el evento {evento.nombre} (ID: {evento.id_evento})? (S/N)")
                confirmacion = input("Respuesta: ").lower()  # Convertir a minúscula para evitar problemas

                if confirmacion == "s":  # Si el usuario confirma con "S"
                    evento_eliminado = eliminar_evento(session, id_evento)
                    if evento_eliminado:
                        print(f"Evento {evento_eliminado.nombre} eliminado exitosamente")
                    else:
                        print("Error al eliminar evento")
                else:  # Si el usuario no confirma
                    print("Eliminación cancelada")
            else:
                print("Evento no encontrado.")

        elif opcion == "4":
            print("\n --- Modificar evento ---")
            print("Deja el campo vacío si no deseas modificarlo")
            try:
                id_evento = int(input("ID del evento: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            nombre_evento = input("Nuevo nombre: ") or None
            descripcion = input("Nueva descripcion: ") or None
            tipo_evento = input("Nuevo tipo: ") or None
            if tipo_evento and tipo_evento not in EVENTOS_VALIDOS:
                print("Tipo de evento no válido. Los tipos válidos son: conferencia, boda, reunion_corporativa, cena_privada")
                continue
            if actualizar_evento(session, id_evento, nombre_evento, descripcion, tipo_evento):
                print(f"Evento {id_evento} actualizado exitosamente")
            else:
                print("Error al actualizar evento")
        elif opcion == "5":
            print("\n --- Buscar evento por ID ---")
            try:
                id_evento = int(input("ID del evento: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            evento = buscar_evento(session, id_evento)
            if evento:
                print(f"ID: {evento.id_evento} Nombre: {evento.nombre_evento} Tipo: {evento.tipo_evento}")
            else:
                print("Evento no encontrado")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#funcion menu de la tabla salones
def menu_salones(session):
    while True:
        print("\n --- Operaciones con Salones ---")
        print("1. Listar salones")
        print("2. Agregar salón")
        print("3. Eliminar salón")
        print("4. Modificar salón")
        print("5. Buscar salón")
        print("6. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar salones ---")
            salones = listar_salones(session)
            if salones:
                for salon in salones:
                    print(f"ID: {salon.id_salon} Nombre: {salon.nombre_salon} Capacidad: {salon.capacidad}")
            else:
                print("No hay salones registrados")
        elif opcion == "2":
            print("\n --- Agregar salón ---")
            nombre_salon = input("Nombre: ")
            try:
                capacidad = int(input("Capacidad: "))
            except ValueError:
                print("Capacidad no válida. Intente de nuevo.")
                continue
            descripcion = input("Descripción: ") or None
            nuevo_salon = agregar_salon(session, nombre_salon, capacidad, descripcion)
            if nuevo_salon:
                print(f"Salón {nuevo_salon.nombre_salon} agregado exitosamente")
            else:
                print("Error al agregar salón")
        elif opcion == "3":
            print("\n --- Eliminar salón ---")
            id_salon = input("ID del salón: ")
            salon = buscar_salon(session, id_salon)  # Verificar si el salón existe

            if salon:
                print(f"¿Deseas eliminar el salón {salon.nombre} (ID: {salon.id_salon})? (S/N)")
                confirmacion = input("Respuesta: ").lower()  # Convertir a minúscula para evitar problemas

                if confirmacion == "s":  # Si el usuario confirma con "S"
                    salon_eliminado = eliminar_salon(session, id_salon)
                    if salon_eliminado:
                        print(f"Salón {salon_eliminado.nombre} eliminado exitosamente")
                    else:
                        print("Error al eliminar salón")
                else:  # Si el usuario no confirma
                    print("Eliminación cancelada")
            else:
                print("Salón no encontrado.")

        elif opcion == "4":
            print("\n --- Modificar salón ---")
            print("Deja el campo vacío si no deseas modificarlo")
            try:
                id_salon = int(input("ID del salón: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            nombre_salon = input("Nuevo nombre: ") or None
            capacidad = input("Nueva capacidad: ") or None
            descripcion = input("Nueva descripción: ") or None
            if actualizar_salon(session, id_salon, nombre_salon, capacidad, descripcion):
                print(f"Salón {id_salon} actualizado exitosamente")
            else:
                print("Error al actualizar salón")
        elif opcion == "5":
            print("\n --- Buscar salón por ID ---")
            try:
                id_salon = int(input("ID del salón: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            salon = buscar_salon(session, id_salon)
            if salon:
                print(f"ID: {salon.id_salon} Nombre: {salon.nombre_salon} Capacidad: {salon.capacidad}")
            else:
                print("Salón no encontrado")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#funcion menu de la tabla reservaciones
def menu_reservaciones(session):
    while True:
        print("\n --- Operaciones con Reservaciones ---")
        print("1. Listar reservaciones")
        print("2. Agregar reservacion")
        print("3. Cancelar reservacion")
        print("4. Modificar reservacion")
        print("5. Buscar reservacion")
        print("6. Calcular Costo de Reservacion")
        print("7. Regresar al menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n --- Listar reservaciones ---")
            reservaciones = listar_reservaciones(session)
            if reservaciones:
                for reservacion in reservaciones:
                    print(f"ID: {reservacion.id_reservacion} Cliente: {reservacion.cliente.nombre} Fecha: {reservacion.fecha_reservacion} Salón: {reservacion.salon.nombre_salon}")
            else:
                print("No hay reservaciones registradas")

        elif opcion == "2":
            print("\n --- Agregar reservacion ---")
            try:
                id_cliente = int(input("ID del cliente: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            try:
                id_salon = int(input("ID del salon: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            fecha_reservacion = input("Fecha de la reservacion (YYYY-MM-DD): ")
            nueva_reservacion = agregar_reservacion(session, id_cliente, id_salon, fecha_reservacion)
            if nueva_reservacion:
                print(f"Reservacion {nueva_reservacion.id_reservacion} agregada exitosamente")
            else:
                print("Error al agregar reservacion")

        elif opcion == "3":
            print("\n --- Cancelar reservación ---")
            id_reservacion = input("ID de la reservación: ")
            reservacion = buscar_reservacion(session, id_reservacion)  # Verificar si la reservación existe

            if reservacion:
                print(f"¿Deseas cancelar la reservación {reservacion.nombre} (ID: {reservacion.id_reservacion})? (S/N)")
                confirmacion = input("Respuesta: ").lower()  # Convertir a minúscula para evitar problemas

                if confirmacion == "s":  # Si el usuario confirma con "S"
                    reservacion_cancelada = cancelar_reservacion(session, id_reservacion)
                    if reservacion_cancelada:
                        print(f"Reservación {reservacion.nombre} cancelada exitosamente")
                    else:
                        print("Error al cancelar reservación")
                else:  # Si el usuario no confirma
                    print("Cancelación de reservación cancelada")
            else:
                print("Reservación no encontrada.")

        elif opcion == "4":
            print("\n --- Modificar reservacion ---")
            print("Deja el campo vacío si no deseas modificarlo")
            try:
                id_reservacion = int(input("ID de la reservacion: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            try:
                id_cliente = int(input("Nuevo ID del cliente: ")) or None
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            try:
                id_salon = int(input("Nuevo ID del salon: ")) or None
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            fecha_reservacion = input("Nueva fecha de la reservacion (YYYY-MM-DD): ") or None
            if actualizar_reservacion(session, id_reservacion, id_cliente, id_salon, fecha_reservacion):
                print(f"Reservacion {id_reservacion} actualizada exitosamente")
            else:
                print("Error al actualizar reservacion")

        elif opcion == "5":
            print("\n --- Buscar reservacion por ID ---")
            try:
                id_reservacion = int(input("ID de la reservacion: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue
            reservacion = buscar_reservacion(session, id_reservacion)
            if reservacion:
                print(f"ID: {reservacion.id_reservacion} Cliente: {reservacion.cliente.nombre} Fecha: {reservacion.fecha_reservacion} Salón: {reservacion.salon.nombre_salon}")
            else:
                print("Reservacion no encontrada")

        elif opcion == "6":
            print("\n --- Calcular costo de reservación ---")
            try:
                id_reservacion = int(input("ID de la reservación: "))
            except ValueError:
                print("ID no válido. Intente de nuevo.")
                continue

            # Llamar a la función para calcular el costo
            costo_total = calcular_costo_reservacion(session, id_reservacion)

            if costo_total is not None:
                print(f"El costo total de la reservación {id_reservacion} es: ${costo_total:.2f}")

        elif opcion == "7":
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
def seleccionar_menu(session):
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes(session)
        elif opcion == "2":
            menu_empleados(session)
        elif opcion == "3":
            menu_eventos(session)
        elif opcion == "4":
            menu_salones(session)
        elif opcion == "5":
            menu_reservaciones(session)    
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

    seleccionar_menu(session)

    session.close()