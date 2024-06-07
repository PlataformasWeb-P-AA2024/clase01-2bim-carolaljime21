from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from configuracion import engine


Base = declarative_base()

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return f"Provincia: {self.nombre} (Código: {self.codigo})"
    
    def obtener_numero_docentes(self):
        suma = 0
        for l in self.cantones:
            for a in l.parroquias:
                for e in a.establecimientos:
                    suma += e.numero_docentes
        return suma
    
    def obtener_lista_parroquias(self):
        lista = []
        for c in self.cantones:
            for p in c.parroquias:
                lista.append(p.nombre)
        return lista

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return f"Cantón: {self.nombre} (Código: {self.codigo})\nProvincia: {self.provincia.nombre}"
    
    def obtener_numero_estudiantes(self):
        suma = 0
        for l in self.parroquias:
            for a in l.establecimientos:
                suma += a.numero_estudiantes
        return suma

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")

    def __repr__(self):
        return f"Parroquia: {self.nombre} (Código: {self.codigo})\nCantón: {self.canton.nombre}"
    
    def obtener_numero_establecimientos(self):
        return len(self.establecimientos)
    
    def obtener_tipos_jornada(self):
        jornadas = []
        for l in self.establecimientos:
            jornadas.append(l.jornada)
        jornadas = set(jornadas)
        return jornadas

            

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigo_amie = Column(String(10), unique=True, nullable=False)
    nombre = Column(String(200), nullable=False)
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    zona_administrativa = Column(String(20))
    denominacion_distrito = Column(String(100))
    codigo_distrito = Column(String(10))
    codigo_circuito = Column(String(20))
    sostenimiento = Column(String(50))
    regimen_escolar = Column(String(50))
    jurisdiccion = Column(String(50))
    tipo_educacion = Column(String(50))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    nivel = Column(String(50))
    etnia = Column(String(50))
    acceso = Column(String(50))
    numero_estudiantes = Column(Integer)
    numero_docentes = Column(Integer)
    estado = Column(String(50))

    def __repr__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Código AMIE: {self.codigo_amie}\n"
                f"Parroquia: {self.parroquia.nombre} (Código: {self.parroquia.codigo})\n"
                f"Cantón: {self.parroquia.canton.nombre} (Código: {self.parroquia.canton.codigo})\n"
                f"Provincia: {self.parroquia.canton.provincia.nombre} (Código: {self.parroquia.canton.provincia.codigo})\n"
                f"Zona Administrativa: {self.zona_administrativa}\n"
                f"Denominación del Distrito: {self.denominacion_distrito}\n"
                f"Código de Distrito: {self.codigo_distrito}\n"
                f"Código de Circuito Educativo: {self.codigo_circuito}\n"
                f"Sostenimiento: {self.sostenimiento}\n"
                f"Régimen Escolar: {self.regimen_escolar}\n"
                f"Jurisdicción: {self.jurisdiccion}\n"
                f"Tipo de Educación: {self.tipo_educacion}\n"
                f"Modalidad: {self.modalidad}\n"
                f"Jornada: {self.jornada}\n"
                f"Nivel: {self.nivel}\n"
                f"Etnia: {self.etnia}\n"
                f"Acceso: {self.acceso}\n"
                f"Número de Estudiantes: {self.numero_estudiantes}\n"
                f"Número de Docentes: {self.numero_docentes}\n"
                f"Estado: {self.estado}\n"
                f"----------------------------------------")



# Crear tablas en la base de datos
Base.metadata.create_all(engine)
