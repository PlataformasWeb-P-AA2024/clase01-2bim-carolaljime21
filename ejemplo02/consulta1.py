from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from crear_tablas import Canton

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
cantones = session.query(Canton).all()
# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Número de estudiantes por cantón")
for s in cantones:
    print("Canton %s: %s" % (s.nombre, s.obtener_numero_estudiantes()))
#    print("Años de vida del club: %d" % (datetime.datatime.now().year - s.fundacion))
    print("---------")

