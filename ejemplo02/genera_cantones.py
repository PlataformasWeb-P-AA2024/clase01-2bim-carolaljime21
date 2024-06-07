from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia, Canton
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

ruta = 'Listado-Instituciones-Educativas-02.csv'

with open(ruta, 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

lineas = [linea.strip().split('|') for linea in lineas]
lineas = lineas[1:]

cantones_set = set()

for linea in lineas:
    codigo_canton = int(linea[4])
    nombre_canton = linea[5]
    codigo_provincia = int(linea[2])
    provincia = session.query(Provincia).filter_by(codigo=codigo_provincia).first()
    cantones_set.add((codigo_canton, nombre_canton, provincia.id))

for codigo, nombre, provincia_id in cantones_set:
    canton = Canton(codigo=codigo, nombre=nombre, provincia_id=provincia_id)
    session.add(canton)

session.commit()
session.close()