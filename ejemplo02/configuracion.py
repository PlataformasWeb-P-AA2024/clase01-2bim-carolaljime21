from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos
# mysql
# pip install mysql-connector-python
engine = create_engine('sqlite:///final1bim.db')