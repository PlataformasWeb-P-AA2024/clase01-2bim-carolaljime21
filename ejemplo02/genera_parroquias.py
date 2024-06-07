from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Parroquia, Provincia, Canton
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

ruta = 'Listado-Instituciones-Educativas-02.csv'

with open(ruta, 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

lineas = [linea.strip().split('|') for linea in lineas]
lineas = lineas[1:]

parroquias_set = set()

for linea in lineas:
    codigo_parroquia = int(linea[6])
    nombre_parroquia = linea[7]
    codigo_canton = int(linea[4])
    canton = session.query(Canton).filter_by(codigo=codigo_canton).first()
    parroquias_set.add((codigo_parroquia, nombre_parroquia, canton.id))

for codigo, nombre, canton_id in parroquias_set:
    parroquia = Parroquia(codigo=codigo, nombre=nombre, canton_id=canton_id)
    session.add(parroquia)

session.commit()
session.close()