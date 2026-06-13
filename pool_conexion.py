import sys
from psycopg2 import pool

class PoolConexion:    

    _DATABASE='validador'
    _USERNAME='postgres'
    _PASSWORD='admin'
    _DB_PORT='5432'
    _HOST='127.0.0.1'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool= pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                host=cls._HOST,
                                user= cls._USERNAME,
                                password= cls._PASSWORD,
                                database=cls._DATABASE,
                                port=cls._DB_PORT)
                print(f'Se conecto correctamente al pool: {cls._pool}')
                return cls._pool
            except Exception as error:
                print(f'Ocurrio un error al conectar el pool: {error}')
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def obtenerconection(cls):
        connect= cls.obtener_pool().getconn()
        print(f'coneccion obtenida del pool: {connect}')
        return connect

    @classmethod
    def port_free(cls, connection):
        if connection is not None:
            cls._pool.putconn(connection)
            print(f'Regresando al pool: {connection}')
    
    @classmethod
    def close_connection(cls):
        cls.obtener_pool().closeall()

if __name__=='__main__':
  connection1= PoolConexion.obtenerconection()
  PoolConexion.port_free(connection1)
  connection2= PoolConexion.obtenerconection()
  connection3= PoolConexion.obtenerconection()
  PoolConexion.port_free(connection3)
  connection4= PoolConexion.obtenerconection()
  connection5= PoolConexion.obtenerconection()
  PoolConexion.port_free(connection5)
  connection6= PoolConexion.obtenerconection()
    