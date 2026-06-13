from pool_conexion import PoolConexion

class CursorForPool:
    def __init__(self):
        self._connection= None
        self._cursor= None

    def __enter__(self):
        print('dentro del metodo with __enter__')
        self._connection= PoolConexion.obtenerconection()
        self._cursor= self._connection.cursor()
        return self._cursor
    
    def __exit__(self, exc_type, exc, tb):
        print('Saliendo del metodo with __exit__')
        if exc:
            self._connection.rollback()
            print(f'Ocurrio una exección, se hace rollback: {exc_type, exc, tb}')
        else:
            self._connection.commit()
            print('Commit de la transacción')
        self._cursor.close()
        PoolConexion.port_free(self._connection)

if __name__== '__main__':
    with CursorForPool() as cursor:
        cursor.execute('SELECT * FROM emailandpassword')
        print(cursor.fetchall())