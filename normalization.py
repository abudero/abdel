class Normalization:

    def __init__(self, email='', passwordd=''):
        self._email= email
        self._passwordd= passwordd
    
    def __str__(self):
        return f'''Email:{self._email}, password:{self._passwordd}'''
    
    @property
    def email(self):
        return self._email
    
    @ email.setter
    def email(self, email):
        self._email= email

    @property
    def passwordd(self):
        return self._passwordd
    
    @ passwordd.setter
    def passwordd(self, passwordd):
        self._passwordd= passwordd

if __name__=='__main__':
    person1=Normalization('abdel@gmail.com', 'lsadkfjasf')
    print(person1)