from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Cliente, Empleado, Evento, Salone, Servicio
from crud_operations import *


if __name__ == "__main__":
    DATABASE_URL = "postgresql://postgres:12345@localhost/hotel"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    #CRUD para la tabla Cliente
    print("Listar clientes")
    clientes = listar_clientes()
    for cliente in clientes:
        print(cliente.nombre)

    print("\nAgregar cliente")
    nuevo_cliente = agregar_cliente("Cachetada", "Cachetada@example.com", "12345678", "Calle 135")
    print("Cliente agregado:", nuevo_cliente.nombre)

    print("Listar clientes")
    clientes = listar_clientes()
    for cliente in clientes:
        print(cliente.nombre)

    print("\nBuscar cliente")
    cliente = buscar_cliente(1)
    print("Cliente encontrado:", cliente.nombre)

    print("\nActualizar cliente")
    actualizar_cliente(1, nombre="Juan Sope Perez")
    cliente = buscar_cliente(1)
    print("Cliente actualizado:", cliente.nombre)

    print("\nEliminar cliente")
    eliminar_cliente(1)    

    print("Listar clientes")
    clientes = listar_clientes()
    for cliente in clientes:
        print(cliente.nombre)








