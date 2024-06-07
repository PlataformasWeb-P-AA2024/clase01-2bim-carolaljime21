from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from crear_tablas import Parroquia

# se importa información del archivo configuracion
from configuracion import engine
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad Club
parroquias = session.query(Parroquia).all()
# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Jornadas")
for s in parroquias:
    print("- Parroquia %s:\n- Jornadas:%s" % (s.nombre, s.obtener_tipos_jornada()))
#    print("Años de vida del club: %d" % (datetime.datatime.now().year - s.fundacion))
    print("---------")

