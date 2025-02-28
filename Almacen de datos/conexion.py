from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base 

DATABASE_URL = "postgresql://postgres:Administracion199.@localhost:5432/servicio_fiestas"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

session = Session()


try:
    session.execute(text("SELECT 1"))
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print("Error al conectar con la base de datos:", e)

