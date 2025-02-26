# coding: utf-8
from sqlalchemy import CheckConstraint, Column, Computed, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True, server_default=text("nextval('clientes_id_cliente_seq'::regclass)"))
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(20))
    direccion = Column(Text)


class Empleado(Base):
    __tablename__ = 'empleados'
    __table_args__ = (
        CheckConstraint("(rol)::text = ANY ((ARRAY['mesero'::character varying, 'coordinador'::character varying, 'chef'::character varying, 'musico'::character varying])::text[])"),
        CheckConstraint("(rol)::text = ANY ((ARRAY['mesero'::character varying, 'coordinador'::character varying, 'chef'::character varying, 'musico'::character varying])::text[])")
    )

    id_empleado = Column(Integer, primary_key=True, server_default=text("nextval('empleados_id_empleado_seq'::regclass)"))
    nombre = Column(String(100), nullable=False)
    rol = Column(String(50), nullable=False)


class Evento(Base):
    __tablename__ = 'eventos'
    __table_args__ = (
        CheckConstraint("(tipo_evento)::text = ANY ((ARRAY['conferencia'::character varying, 'boda'::character varying, 'reunion_corporativa'::character varying, 'cena_privada'::character varying])::text[])"),
        CheckConstraint("(tipo_evento)::text = ANY ((ARRAY['conferencia'::character varying, 'boda'::character varying, 'reunion_corporativa'::character varying, 'cena_privada'::character varying])::text[])")
    )

    id_evento = Column(Integer, primary_key=True, server_default=text("nextval('eventos_id_evento_seq'::regclass)"))
    nombre_evento = Column(String(200), nullable=False)
    descripcion = Column(Text)
    tipo_evento = Column(String(50), nullable=False)
    fecha_creacion = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    fecha_actualizacion = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class Salone(Base):
    __tablename__ = 'salones'

    id_salon = Column(Integer, primary_key=True, server_default=text("nextval('salones_id_salon_seq'::regclass)"))
    nombre_salon = Column(String(100), nullable=False)
    capacidad = Column(Integer, nullable=False)
    descripcion = Column(Text)


class Servicio(Base):
    __tablename__ = 'servicios'

    id_servicio = Column(Integer, primary_key=True, server_default=text("nextval('servicios_id_servicio_seq'::regclass)"))
    nombre_servicio = Column(String(100), nullable=False)
    descripcion = Column(Text)
    costo = Column(Numeric(10, 2), nullable=False)


class Temporada(Base):
    __tablename__ = 'temporadas'
    __table_args__ = (
        CheckConstraint('multiplicador > (0)::numeric'),
    )

    id_temporada = Column(Integer, primary_key=True, server_default=text("nextval('temporadas_id_temporada_seq'::regclass)"))
    nombre_temporada = Column(String(100), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    multiplicador = Column(Numeric(5, 2), nullable=False)


class HistorialEvento(Base):
    __tablename__ = 'historial_eventos'

    id_historial = Column(Integer, primary_key=True, server_default=text("nextval('historial_eventos_id_historial_seq'::regclass)"))
    id_evento = Column(ForeignKey('eventos.id_evento', ondelete='CASCADE'))
    nombre_anterior = Column(String(200))
    descripcion_anterior = Column(Text)
    fecha_cambio = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    evento = relationship('Evento')


class PreciosTemporada(Base):
    __tablename__ = 'precios_temporada'

    id_precio_temporada = Column(Integer, primary_key=True, server_default=text("nextval('precios_temporada_id_precio_temporada_seq'::regclass)"))
    id_servicio = Column(ForeignKey('servicios.id_servicio', ondelete='CASCADE'))
    id_temporada = Column(ForeignKey('temporadas.id_temporada', ondelete='CASCADE'))
    costo_ajustado = Column(Numeric(10, 2), nullable=False)

    servicio = relationship('Servicio')
    temporada = relationship('Temporada')


class Reservacione(Base):
    __tablename__ = 'reservaciones'
    __table_args__ = (
        CheckConstraint("(estado_reservacion)::text = ANY ((ARRAY['activa'::character varying, 'cancelada'::character varying])::text[])"),
        CheckConstraint("(estado_reservacion)::text = ANY ((ARRAY['activa'::character varying, 'cancelada'::character varying])::text[])")
    )

    id_reservacion = Column(Integer, primary_key=True, server_default=text("nextval('reservaciones_id_reservacion_seq'::regclass)"))
    id_cliente = Column(ForeignKey('clientes.id_cliente', ondelete='CASCADE'))
    id_evento = Column(ForeignKey('eventos.id_evento', ondelete='CASCADE'))
    fecha_solicitud = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    fecha_evento = Column(DateTime, nullable=False)
    fecha_cancelacion = Column(DateTime)
    estado_reservacion = Column(String(20), server_default=text("'activa'::character varying"))

    cliente = relationship('Cliente')
    evento = relationship('Evento')


class AsignacionEmpleado(Base):
    __tablename__ = 'asignacion_empleados'

    id_asignacion_empleado = Column(Integer, primary_key=True, server_default=text("nextval('asignacion_empleados_id_asignacion_empleado_seq'::regclass)"))
    id_reservacion = Column(ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'))
    id_empleado = Column(ForeignKey('empleados.id_empleado', ondelete='CASCADE'))
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)

    empleado = relationship('Empleado')
    reservacione = relationship('Reservacione')


class AsignacionSalone(Base):
    __tablename__ = 'asignacion_salones'

    id_asignacion = Column(Integer, primary_key=True, server_default=text("nextval('asignacion_salones_id_asignacion_seq'::regclass)"))
    id_reservacion = Column(ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'))
    id_salon = Column(ForeignKey('salones.id_salon', ondelete='CASCADE'))
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)

    reservacione = relationship('Reservacione')
    salone = relationship('Salone')


class AsignacionServicio(Base):
    __tablename__ = 'asignacion_servicios'

    id_asignacion_servicio = Column(Integer, primary_key=True, server_default=text("nextval('asignacion_servicios_id_asignacion_servicio_seq'::regclass)"))
    id_reservacion = Column(ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'))
    id_servicio = Column(ForeignKey('servicios.id_servicio', ondelete='CASCADE'))
    cantidad = Column(Integer, server_default=text("1"))

    reservacione = relationship('Reservacione')
    servicio = relationship('Servicio')


class Facturacion(Base):
    __tablename__ = 'facturacion'
    __table_args__ = (
        CheckConstraint("(moneda_origen)::text = ANY ((ARRAY['USD'::character varying, 'EUR'::character varying, 'MXN'::character varying])::text[])"),
        CheckConstraint("(moneda_origen)::text = ANY ((ARRAY['USD'::character varying, 'EUR'::character varying, 'MXN'::character varying])::text[])")
    )

    id_factura = Column(Integer, primary_key=True, server_default=text("nextval('facturacion_id_factura_seq'::regclass)"))
    id_reservacion = Column(ForeignKey('reservaciones.id_reservacion', ondelete='CASCADE'))
    monto_total = Column(Numeric(10, 2), nullable=False)
    moneda_origen = Column(String(10), nullable=False)
    tipo_cambio = Column(Numeric(10, 2), nullable=False)
    monto_convertido = Column(Numeric(10, 2), Computed('(monto_total * tipo_cambio)', persisted=True))
    fecha_pago = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    reservacione = relationship('Reservacione')
