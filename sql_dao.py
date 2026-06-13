from cursor_pool import CursorForPool
from normalization import Normalization
class CrudDao:

    _SELECT='SELECT * FROM emailandpassword'
    _INSERT='INSERT INTO emailandpassword(email, passwordd) VALUES(%s, %s)'
    _UPDATE='UPDATE emailandpassword SET email=%s, password=%s WHERE email=%s'
    _DELETE='DELETE FROM emailandpassword WHERE email=%s'

    @classmethod 
    def select(cls):
        with CursorForPool() as cursor:
            cursor.execute(cls._SELECT)
            register= cursor.fetchall()
            emails_passwords=[]
            for registers in register:
                email_password= Normalization(registers[0], registers[1], registers[2], 
                                              registers[3], registers[4])
                emails_passwords.append(email_password)
                return emails_passwords
    
    @classmethod
    def insert(cls, insertar):
        with CursorForPool() as cursor:
            values=[(v.email, v.passwordd) 
                    for v in insertar]
            cursor.execute(cls._INSERT, values)
            return cursor.rowcount
    
    @classmethod
    def update(cls, update):
        with CursorForPool() as cursor:
            value=[(v.email, v.passwordd)
                for v in update]
            cursor.execute(cls._UPDATE, value)
            return cursor.rowcount
    
    @classmethod
    def delete(cls, delete):
        with CursorForPool() as cursor:
            value=[(v.email, v.passwordd)
                for v in delete]
            cursor.execute(cls._DELETE, value)
            return cursor.rowcount

if __name__=='__main__':
     
    select1= CrudDao.select()
    for selec in select1:
        print(selec)
    
    # insertt= Normalization('fran@gmail.com', 'añflkjfd4511')
    # insert1= CrudDao.insert(insertt)
    # print(f'se insertaron {insert1} product(s)')

    # update= Gestion(Name_product='Gun', Type_product='weapons', amount=21, coste=15, Code=4)
    # update1= Crud_connect.update(update)
    # print(f'se actualizaron {update1} product(s)')

#     delete= Gestion(Code=4)
#     delete1= Crud_connect.delete(delete)
#     print(f'sea eliminado {delete1} product(s)')
