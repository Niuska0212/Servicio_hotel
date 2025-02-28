from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

def validar_fecha(fecha_str):
    try:
        fecha_str = fecha_str.strip()
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        return fecha
    except ValueError as e:
        logging.error(f"Error al convertir la fecha: {e}")
        return None
