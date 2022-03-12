
class User:

    state = False
    email = None

    def __init__(self, email):

        self.email = email


    @classmethod
    def is_anonymous(cls):
        if cls.state:
            return False
        elif not cls.state:
            return True

    
    def is_authenticated(self):
        return self.state

    @property
    def is_active(self):
        return True
    

    def log(self):
        if self.is_authenticated():
            print('Usuário já está logado')
            return

        self.state = True


    def logout_user(self,email):
        if email == self.email:
            self.state = False
            self.email = None


    def get_id(self):
        return self.email

