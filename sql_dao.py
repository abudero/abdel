from cursor_pool import CursorForPool
from normalization import Normalization
class CrudDao:

    _SELECT='SELECT * FROM emailandpassword'
    _INSERT='INSERT INTO emailandpassword(email, passwordd) VALUES(%s, %s)'
    _UPDATE='UPDATE emailandpassword SET passwordd=%s WHERE email=%s'
    _DELETE='DELETE FROM emailandpassword WHERE email=%s'

    @classmethod 
    def select(cls):
        with CursorForPool() as cursor:
            cursor.execute(cls._SELECT)
            register= cursor.fetchall()
            emails_passwords=[]
            for registers in register:
                email_password= Normalization(registers[0], registers[1])
                emails_passwords.append(email_password)
            return emails_passwords
    
    @classmethod
    def insert(cls, insertar):
        with CursorForPool() as cursor:
            values=[(v.email, v.passwordd) 
                    for v in insertar]
            cursor.executemany(cls._INSERT, values)
            return cursor.rowcount
    
    @classmethod
    def update(cls, update):
        with CursorForPool() as cursor:
            value=[(v.passwordd, v.email)
                for v in update]
            cursor.executemany(cls._UPDATE, value)
            return cursor.rowcount
    
    @classmethod
    def delete(cls, delete):
        with CursorForPool() as cursor:
            value=[(v.email,)
                for v in delete]
            cursor.executemany(cls._DELETE, value)
            return cursor.rowcount

if __name__=='__main__':
     
    select1= CrudDao.select()
    for selec in select1:
        print(selec)
    
    # insertt= Normalization('fran@gmail.com', 'añflkjfd4511')
    # insert1= CrudDao.insert([insertt])
    # print(f'se insertaron {insert1} nuevos correos')

    # update= Normalization('abdel@gmail.com','dlskjasñlgks5214')
    # update1= CrudDao.update([update])
    # print(f'se actualizaron {update1} correo(s)')

    # delete= Normalization('abdel@gmail.com')
    # delete1= CrudDao.delete([delete])
    # print(f'sea eliminado {delete1} email(s)')
