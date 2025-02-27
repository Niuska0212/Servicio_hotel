from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Cliente, Empleado, Evento, Salone, Reservacione
from crud_operations import *


if __name__ == "__main__":
    DATABASE_URL = "postgresql://postgres:12345@localhost/hotel"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    seleccionar_menu()

    

def seleccionar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")






def mostrar_menu():
    print("\n --- Menu Principal ---")
    print("1. Operaciones con Clientes")
    print("2. Operaciones con Empleados")
    print("3. Operaciones con Eventos")
    print("4. Operaciones con Salones")
    print("5. Operaciones con Reservaciones")
    print("6. Salir")



def manu_clientes():
    while True:
        print("\n --- Operaciones con Clientes ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Eliminar cliente")
        print("4. Modificar cliente")
        print("5. Buscar cliente")
        print("6. Regresar al menu principal")
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

