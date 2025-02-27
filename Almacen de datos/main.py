from crud_operations import encontrar_empleados_disponibles, session
from utils import validar_fecha


def mostrar_menu():
    print("1. Encontrar empleados disponibles")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            #solicitar datos
            rol = input("Ingrese el rol del empleado (mesero, coordinador, chef, musico): ").strip().lower()
            fecha_inicio_str = input("Ingrese la fecha de inicio (YYYY-MM-DD HH:MM:SS): ").strip()
            fecha_fin_str = input("Ingrese la fecha de fin (YYYY-MM-DD HH:MM:SS): ").strip()

            #validar fechas
            fecha_inicio = validar_fecha(fecha_inicio_str)
            fecha_fin = validar_fecha(fecha_fin_str)

            if fecha_inicio is None or fecha_fin is None:
                print("\nError: Formato de fecha inválido. Use el formato YYYY-MM-DD HH:MM:SS.")
                continue

            if fecha_inicio >= fecha_fin:
                print("\nError: La fecha de inicio debe ser anterior a la fecha de fin.")
                continue

            encontrar_empleados_disponibles(rol, fecha_inicio, fecha_fin)

        elif opcion == "2":
            print("Hasta pronto...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
