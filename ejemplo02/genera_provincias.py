from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

ruta = 'Listado-Instituciones-Educativas-02.csv'

with open(ruta, 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

lineas = [linea.strip().split('|') for linea in lineas]
lineas = lineas[1:]

provincias_set = set()

for linea in lineas:
    codigo_provincia = int(linea[2])
    nombre_provincia = linea[3]
    provincias_set.add((codigo_provincia, nombre_provincia))

for codigo, nombre in provincias_set:
    provincia = Provincia(codigo=codigo, nombre=nombre)
    session.add(provincia)

session.commit()
session.close()
