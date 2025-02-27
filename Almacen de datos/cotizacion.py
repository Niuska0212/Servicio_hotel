from sqlalchemy.orm import sessionmaker
from modelos import Cotizacion, Producto, DetalleCotizacion, Servicio


def mostrar_cotizacion_total(id_reservacion, session):

    cotizacion = session.query(Cotizacion).filter(Cotizacion.id_cotizacion == id_reservacion).first()

    if not cotizacion:
        raise ValueError(f"No se encontró la cotización con ID {id_reservacion}")


    total = cotizacion.total  
    print(f"ID de Cotización: {cotizacion.id_cotizacion}")
    print(f"Cliente ID: {cotizacion.id_cliente}")
    print(f"Total cotización (productos): ${cotizacion.total}")


    detalles = session.query(DetalleCotizacion).filter(DetalleCotizacion.id_cotizacion == cotizacion.id_cotizacion).all()

    if detalles:
        print("\nDetalles de Productos:")
        for detalle in detalles:
            producto = session.query(Producto).filter(Producto.id_producto == detalle.id_producto).first()
            if producto:
                subtotal = producto.precio * detalle.cantidad
                print(f"Producto: {producto.nombre}, Cantidad: {detalle.cantidad}, Subtotal: ${subtotal}")
                total += subtotal  


    servicios = session.query(Servicio).filter(Servicio.id_cotizacion == cotizacion.id_cotizacion).all()

    if servicios:
        print("\nServicios adicionales:")
        for servicio in servicios:
            print(f"Servicio: {servicio.nombre}, Precio: ${servicio.precio}")
            total += servicio.precio  


    print(f"\nTotal final de la cotización (productos + servicios adicionales): ${total}")



def crear_sesion():
    DATABASE_URL = "postgresql://postgres:12345@localhost/hotel"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session



if __name__ == "__main__":
    session = crear_sesion()

    # Menú principal
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Mostrar cotización total de una reservación")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nListar clientes")
            clientes = listar_clientes(session)
            for cliente in clientes:
                print(cliente.nombre)

        elif opcion == "2":
            print("\nAgregar cliente")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            nuevo_cliente = agregar_cliente(session, nombre, correo, telefono, direccion)
            print("Cliente agregado:", nuevo_cliente.nombre)

        elif opcion == "3":
            print("\nMostrar cotización total de una reservación")
            id_reservacion = int(input("ID de la reservación: "))
            try:
                mostrar_cotizacion_total(id_reservacion, session)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
