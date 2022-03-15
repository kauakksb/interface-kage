from app import db, lm
from models.database import ClassDatabase
from flask_login import UserMixin


manage_db = ClassDatabase('kage.db')


@lm.user_loader
def get_user(email_usu):
    return User.query.filter_by(email_usu = email_usu).first()


class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    email_usu = db.Column(db.String(50), nullable = False, primary_key = True)
    nome_usu = db.Column(db.String(80), nullable = False)
    senha_usu = db.Column(db.String(60), nullable = False)


    def __init__(self, email, name, senha):
        self.email_usu = email
        self.name_usu = name
        self.senha = senha

    def verify_password(self):

        if self.senha == manage_db.searchData('senha', 'usuarios', 'email_usu', self.email):
            return True
        else:
            return False


    @property
    def is_active(self):
        return True

    def get_id(self):
        return self.email_usu




