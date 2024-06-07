from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
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
    codigo_amie = linea[0]
    nombre = linea[1]
    codigo_parroquia = int(linea[6])
    parroquia = session.query(Parroquia).filter_by(codigo=codigo_parroquia).first()
    
    # Establecimiento 936 incorrecto: 
    # 09H02926    |DR EUGENIO ESPEJO EXTENCION 05 R                                            |                                                9 |GUAYAS      |                                            904 |BALZAR                     |                                             90450 |BALZAR                                                   |Zona 5              |BALZAR – COLIMES - PALESTINA                      |09D13              |09D13C02_b                   |Particular    |COSTA           |Hispana      |Popular Permanente  |A Distancia                 |Matutina              |Educación Básica                        |Bachillarato y Alfabetizacion P.P. |2                                 |Terrestre             |                60 |7      |Activa

    # 09H06159    |HARVARD INTERNATIONAL LANGUAJE CENTER                                       |                                                9 |GUAYAS      |                                            910 |MILAGRO                    |                                             91050 |MILAGRO                                                  |Zona 5              |MILAGRO                                           |09D17              |                             |Particular    |COSTA           |Hispana      |Popular Permanente  |Presencial                  |Matutina              |Vesperina y Nocturna                    |Artesanal P.P |                                  |Terrestre             |                 8 |1      |Activa

    establecimiento = Establecimiento(
        codigo_amie=codigo_amie,
        nombre=nombre,
        parroquia_id=parroquia.id,
        zona_administrativa=linea[8],
        denominacion_distrito=linea[9],
        codigo_distrito=linea[10],
        codigo_circuito=linea[11],
        sostenimiento=linea[12],
        regimen_escolar=linea[13],
        jurisdiccion=linea[14],
        tipo_educacion=linea[15],
        modalidad=linea[16],
        jornada=linea[17],
        nivel=linea[18],
        etnia=linea[19],
        acceso=linea[20],
        numero_estudiantes=int(linea[21]),
        numero_docentes=int(linea[22]),
        estado=linea[23]
    )
    
    session.add(establecimiento)

session.commit()
session.close()