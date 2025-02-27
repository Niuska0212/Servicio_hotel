from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric, ForeignKey, TIMESTAMP, CheckConstraint, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

#base de datos
DATABASE_URI = 'postgresql+psycopg2://postgres:Administracion199.@localhost/servicio_fiestas'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# modelos
class Cliente(Base):
    __tablename__ = 'clientes'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20))
    direccion = Column(Text)
    reservaciones = relationship('Reservacion', back_populates='cliente')

class Evento(Base):
    __tablename__ = 'eventos'
    id_evento = Column(Integer, primary_key=True, autoincrement=True)
    nombre_evento = Column(String(200), nullable=False)
    descripcion = Column(Text)
    tipo_evento = Column(Enum('conferencia', 'boda', 'reunion_corporativa', 'cena_privada', name='tipo_evento'), nullable=False)
    fecha_creacion = Column(TIMESTAMP, server_default=func.now())
    fecha_actualizacion = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    reservaciones = relationship('Reservacion', back_populates='evento')

class Reservacion(Base):
    __tablename__ = 'reservaciones'
    id_reservacion = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente', ondelete='CASCADE'), nullable=False)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento', ondelete='CASCADE'), nullable=False)
    fecha_solicitud = Column(TIMESTAMP, server_default=func.now())
    fecha_evento = Column(TIMESTAMP, nullable=False)
    fecha_cancelacion = Column(TIMESTAMP)
    estado_reservacion = Column(Enum('activa', 'cancelada', name='estado_reservacion'), server_default='activa')
    cliente = relationship('Cliente', back_populates='reservaciones')
    evento = relationship('Evento', back_populates='reservaciones')
    asignaciones_salones = relationship('AsignacionSalon', back_populates='reservacion')
    asignaciones_servicios = relationship('AsignacionServicio', back_populates='reservacion')
    asignaciones_empleados = relationship('AsignacionEmpleado', back_populates='reservacion')

class Salon(Base):
    __tablename__ = 'salones'
    id_salon = Column(Integer, primary_key=True, autoincrement=True)
    nombre_salon = Column(String(100), nullable=False)
    capacidad = Column(Integer, nullable=False)
    descripcion = Column(Text)
    asignaciones_salones = relationship('AsignacionSalon', back_populates='salon')

class Servicio(Base):
    __tablename__ = 'servicios'
    id_servicio = Column(Integer, primary_key=True, autoincrement=True)
    nombre_servicio = Column(String(100), nullable=False)
    descripcion = Column(Text)
    costo = Column(Numeric(10, 2), nullable=False)
    asignaciones_servicios = relationship('AsignacionServicio', back_populates='servicio')

class Empleado(Base):
    __tablename__ = 'empleados'
    id_empleado = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    rol = Column(Enum('mesero', 'coordinador', 'chef', 'musico', name='rol'), nullable=False)
    asignaciones_empleados = relationship('AsignacionEmpleado', back_populates='empleado')

class Facturacion(Base):
    __tablename__ = 'facturacion'
    id_factura = Column(Integer, primary_key=True, autoincrement=True)
    id_reservacion = Column(Integer, ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'), nullable=False)
    monto_total = Column(Numeric(10, 2), nullable=False)
    moneda_origen = Column(Enum('USD', 'EUR', 'MXN', name='moneda_origen'), nullable=False)
    tipo_cambio = Column(Numeric(10, 2), nullable=False)
    monto_convertido = Column(Numeric(10, 2), nullable=False)
    fecha_pago = Column(TIMESTAMP, server_default=func.now())

class AsignacionSalon(Base):
    __tablename__ = 'asignacion_salones'
    id_asignacion = Column(Integer, primary_key=True, autoincrement=True)
    id_reservacion = Column(Integer, ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'), nullable=False)
    id_salon = Column(Integer, ForeignKey('salones.id_salon', ondelete='CASCADE'), nullable=False)
    fecha_inicio = Column(TIMESTAMP, nullable=False)
    fecha_fin = Column(TIMESTAMP, nullable=False)
    reservacion = relationship('Reservacion', back_populates='asignaciones_salones')
    salon = relationship('Salon', back_populates='asignaciones_salones')

class AsignacionEmpleado(Base):
    __tablename__ = 'asignacion_empleados'
    id_asignacion_empleado = Column(Integer, primary_key=True, autoincrement=True)
    id_reservacion = Column(Integer, ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'), nullable=False)
    id_empleado = Column(Integer, ForeignKey('empleados.id_empleado', ondelete='CASCADE'), nullable=False)
    fecha_inicio = Column(TIMESTAMP, nullable=False)
    fecha_fin = Column(TIMESTAMP, nullable=False)
    reservacion = relationship('Reservacion', back_populates='asignaciones_empleados')
    empleado = relationship('Empleado', back_populates='asignaciones_empleados')

class AsignacionServicio(Base):
    __tablename__ = 'asignacion_servicios'
    id_asignacion_servicio = Column(Integer, primary_key=True, autoincrement=True)
    id_reservacion = Column(Integer, ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'), nullable=False)
    id_servicio = Column(Integer, ForeignKey('servicios.id_servicio', ondelete='CASCADE'), nullable=False)
    cantidad = Column(Integer, server_default='1')
    reservacion = relationship('Reservacion', back_populates='asignaciones_servicios')
    servicio = relationship('Servicio', back_populates='asignaciones_servicios')

class HistorialEventos(Base):
    __tablename__ = 'historial_eventos'
    id_historial = Column(Integer, primary_key=True, autoincrement=True)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento', ondelete='CASCADE'), nullable=False)
    nombre_anterior = Column(String(200))
    descripcion_anterior = Column(Text)
    fecha_cambio = Column(TIMESTAMP, server_default=func.now())
