from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crud_operations import *

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Listar clientes")
    print("2. Agregar cliente")
    print("3. Buscar cliente por ID")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("6. Listar eventos por fecha")
    print("7. Listar eventos con servicio de catering por mes")
    print("8. Salir")

if __name__ == "__main__":
    DATABASE_URL = "postgresql://postgres:matraca04@localhost:5434/hotel_db"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nListar clientes")
            clientes = listar_clientes(session)
            for cliente in clientes:
                print(f"ID: {cliente.id_cliente}, Nombre: {cliente.nombre}, Correo: {cliente.correo}, Teléfono: {cliente.telefono}")

        elif opcion == "2":
            print("\nAgregar cliente")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            nuevo_cliente = agregar_cliente(session, nombre, correo, telefono, direccion)
            print(f"Cliente agregado: {nuevo_cliente.nombre}")

        elif opcion == "3":
            print("\nBuscar cliente por ID")
            id_cliente = int(input("ID del cliente: "))
            cliente = buscar_cliente(session, id_cliente)
            if cliente:
                print(f"Cliente encontrado: {cliente.nombre}, Correo: {cliente.correo}, Teléfono: {cliente.telefono}")
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            print("\nActualizar cliente")
            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
            correo = input("Nuevo correo (deja vacío para no cambiar): ")
            telefono = input("Nuevo teléfono (deja vacío para no cambiar): ")
            direccion = input("Nueva dirección (deja vacío para no cambiar): ")
            cliente_actualizado = actualizar_cliente(session, id_cliente, nombre or None, correo or None, telefono or None, direccion or None)

        elif opcion == "5":
            print("\nEliminar cliente")
            id_cliente = int(input("ID del cliente: "))
            eliminar_cliente(session, id_cliente)
            print("Cliente eliminado.")

        elif opcion == "6":
            print("\nListar eventos por fecha")

            fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
            try:
                eventos = listar_eventos_por_fecha(session, fecha)
                print(eventos)
            except Exception as e:
                print(f"Error al listar eventos!, procura escribir la fecha en el formato correcto YYYY-MM-DD") 

        elif opcion == "7":
            print("\nListar evento con servicio de catering por mes")

            try: 
                mes = int(input("Ingresa el mes (1-12): "))
                año = int(input("Ingresa el año (YYYY): "))
                eventos = listar_eventos_por_mes_con_catering(session, mes, año)
                print(eventos)
            except:
                print("Error al listar eventos, procura ingresar un mes y año válidos")

        elif opcion == "8":
            print("\nSaliendo del programa. Hasta Luego!")
            break


        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")
