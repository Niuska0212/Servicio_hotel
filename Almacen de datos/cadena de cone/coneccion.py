import psycopg2

try:
    # Intenta conectarte a la base de datos
    conn = psycopg2.connect(
        dbname="hotel",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa!")
    conn.close()
except Exception as e:
    print(f"Error de conexión: {e}")