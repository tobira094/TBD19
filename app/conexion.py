import psycopg2
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('config.conf')
USER = CONFIG['datos_conexion']['usuario']
PASS = CONFIG['datos_conexion']['contra']

try:
    conexion = psycopg2.connect(user = USER,
                                  password = PASS,
                                  host = "192.168.194.105",
                                  port = "5432",
                                  database = "tbd19")
    
    cursor = conexion.cursor()

except (Exception, psycopg2.Error) as error :
    print ("Error conectandose a PostgreSQL", error)

finally:
    #closing database connection.
        if(conexion):
            cursor.close()
            conexion.close()
            print("Conexion cerrada")