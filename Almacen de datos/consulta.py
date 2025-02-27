from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Cliente, Empleado, Evento, Salone, Servicio
from crud_operations import *
from cotizacion import mostrar_cotizacion

if __name__ == "__main__":
    DATABASE_URL = "postgresql://postgres:12345@localhost/hotel"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Menú principal
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Mostrar cotización de una reservación")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nListar clientes")
            clientes = listar_clientes()
            for cliente in clientes:
                print(cliente.nombre)

        elif opcion == "2":
            print("\nAgregar cliente")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            nuevo_cliente = agregar_cliente(nombre, correo, telefono, direccion)
            print("Cliente agregado:", nuevo_cliente.nombre)

        elif opcion == "3":
            print("\nMostrar cotización de una reservación")
            id_reservacion = int(input("ID de la reservación: "))
            try:
                mostrar_cotizacion(id_reservacion, session)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
