from flask import redirect, session, url_for, render_template, request
from sqlite3 import Error
from flask_login import current_user, login_user, logout_user

from models.database import ClassDatabase
from models.tables import ClassTableCarr, ClassTableHist, ClassTableProd, ClassTableServ, ClassTableUser

manage_db = ClassDatabase('kage.db')
table_user = ClassTableUser('kage.db')
table_prod = ClassTableProd('kage.db')
table_serv = ClassTableServ('kage.db')
table_carr = ClassTableCarr('kage.db')
table_hist = ClassTableHist('kage.db')


def cadastro(advise = '', aste = ''):
    return render_template("cadastro.html", p = advise, ast = aste, titulo = 'Cadastro')



def inserir_dados(email, nome, senha, cpf, estado, cidade, bairro, rua, numero_cad, comp):

    try:

        dados = [email,nome,senha,cpf,estado,cidade,bairro,rua,numero_cad,comp]

        for dado in dados:
            if dado == '':
                return False

        dom_aceitos = ['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com']


        emails = manage_db.searchData('email_usu', 'usuarios')
        email_testado = email
        email_testado = email_testado.replace('@', ' @')
        email_testado =  email_testado.split()

        if email_testado[1] in dom_aceitos:
            advise = ''
            return False

        if email in str(emails):
            return False


        cpf_usuarios = manage_db.searchData('cpf', 'usuarios')
        cpf_usuarios = str(cpf_usuarios)

        if len(cpf) == 11:
            if cpf in cpf_usuarios:
                return False

        else:
            return False


        numero = int(numero)

        try:
            manage_db.insertData('usuarios', email, nome, senha, cpf, estado, cidade, bairro, rua, numero_cad, comp)
        except Error as erro:
            print(erro)
            if '1062' in str(erro):
                i += 1
                vez += i
                advise = 'Usuário já existente' 
                return redirect('/cadastro')
            
    except:
        '''nada'''
        return redirect('/cadastro')

    return render_template('retorno.html', file = 'retorno', retorno = 'cadastro', titulo = 'Cadastro concluído')