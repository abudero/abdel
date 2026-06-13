import email
from pickletools import read_uint1
from turtle import RawTurtle


class Normalization:

    def __init__(self, email='', passwerd=''):
        self._email= email
        self._password= passwerd
    
    def __str__(self):
        return f'''Email:{self._email}, password:{self._password}'''
    
    @property
    def email(self):
        return self._email
    
    @ email.setter
    def email(self, email):
        self._email= email

    @property
    def password(self):
        return self._password
    
    @ password.setter
    def password(self, password):
        self._password= password

if __name__=='__main__':
    person1=Normalization('abdel@gmail.com', 'lsadkfjasf')
    print(person1)