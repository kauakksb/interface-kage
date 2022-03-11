
class User:

    state = False
    email = None

    def __init__(self, email, name, senha, cpf, estado, cidade, bairro, rua, num, comp):

        self.email = email
        self.name = name
        self.senha = senha
        self.cpf = cpf
        self.estado = estado
        self.cidade =  cidade
        self.bairro = bairro
        self.rua = rua
        self.num = num
        self.comp = comp


    @classmethod
    def is_anonymous(cls):
        if cls.state:
            return False
        elif not cls.state:
            return True

    @classmethod
    def is_authenticated(cls):
        return cls.state

    @property
    def is_active(self):
        return True
    

    @classmethod
    def log(cls, email):
        if cls.is_authenticated():
            print('Usuário já está logado')
            return

        cls.email = email
        cls.state = True

    @classmethod
    def logout_user(cls, email):
        if email == cls.email:
            cls.state = False
            cls.email = None

    @classmethod
    def get_id(cls):
        return cls.email

