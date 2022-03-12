from flask import Flask, redirect, url_for, render_template, request
import sqlite3
from sqlite3 import Cursor, Error


app =  Flask(__name__)

from models.database import ClassDatabase
from models.tables import ClassTableCarr, ClassTableHist, ClassTableProd, ClassTableServ, ClassTableUser
from user import User


db = ClassDatabase('kage.db')
table_user = ClassTableUser('kage.db')
table_prod = ClassTableProd('kage.db')
table_serv = ClassTableServ('kage.db')
table_carr = ClassTableCarr('kage.db')
table_hist = ClassTableHist('kage.db')
    

state = False
valor_inserido = None
results = ''
num = None
target = ''
dados_prod = None
email_logado = ''
anonymous = True


@app.route('/')
def homepage():
    global state, user, email_logado, anonymous

    if anonymous == True:
        user = User(email_logado)

    if user.is_authenticated():
        state = True
    else:
        state = False

    return render_template('pagina_inicial.html' ,ap = True, state = state)




@app.route('/login', methods = ["GET", "POST"])
def login():
    return render_template('login.html')



@app.route('/validando-login', methods = ["GET", "POST"])
def verific_login():
    global email_logado, target, user, anonymous
    email = request.form.get('email')
    senha = request.form.get('senha')

    if len(str(email)) == 0 or len(senha) == 0:
        
        return 'É preciso preencher todos os campos'

    try:
        user_data = table_user.getUserData(email)[0]
    except:
        return 'Usuário não encontrado'
    

    if email == user_data[0] and senha == user_data[2]:
        email_logado = email
        user = User(email_logado)
        user.log()
        anonymous = False
        if target == 'perfil':
            return redirect('/perfil')
        elif target == 'prod':
            return redirect('/produto')


    else:
        return 'Login Inválido'


@app.route('/logout')
def logout():
    global email_logado, user, anonymous
    user.logout_user(email_logado)
    email_logado = None
    anonymous = True
    return redirect('/')


@app.route('/perfil')
def perfil():
    global target, state, user
    target = 'perfil'

    sinais = ['[',']','(',')', "'"]
    sinais2 = ['(',')', "'",',']

    if user.is_authenticated():
        try:
            prods = []
            prods_carr = []
            valor_total = 0 
            
            servicos = db.searchData('*', 'servicos','email_cliente', user.get_id())
            info_pessoais = db.searchData('*', 'usuarios', 'email_usu', user.get_id())
            hist = db.searchData('id_produto', 'hist', 'id_cliente', user.get_id())
            carr = db.searchData('id_produto','carr', 'id_cliente', user.get_id())

            quant = str(db.searchData('quant','carr', 'id_cliente', user.get_id()))
            for sinal in sinais:
                quant = quant.replace(sinal,'')
            quant = quant.replace(',' ," ")
            quant = quant.split()


            for item in hist:
                item = str(item)
                for sinal in sinais2:
                    item = item.replace(sinal, '')

                item = int(item)
                dados_prod = db.searchData('*', 'produtos','id_prod', item)[0]
                prods.append(dados_prod)

            for prod in carr:
                prod = str(prod)
                for sinal in sinais2:
                    prod = prod.replace(sinal, '')
                
                prod = int(prod)
                dados_carr = db.searchData('*', 'produtos','id_prod', prod)[0]
                prods_carr.append(dados_carr)


            for produto in prods_carr:
                valor_total += produto[2] 

        except:
            '''nada'''

        if user.is_authenticated():
            state = True
        else:
            state = False
        
        return render_template('perfil.html', servicos = servicos, num_serv = len(servicos), dados = info_pessoais, num_prods = len(prods), prods = prods, prods_carr = prods_carr, num_prods_carr = len(prods_carr), valor_total_carr = valor_total, quant_prod = quant, state = state)
    
    else:
        return redirect('/login')



@app.route('/alterar-dados')
def alt_dados():
    return render_template('alt_dados.html')




@app.route('/produtos', methods = ["GET", "POST"])
def produtos():
    global valor_inserido, results, num, state

    valor_inserido = ""
    
    valor_inserido = request.form.get('camp_pesq')
    if len(str(valor_inserido)) == 0:
        return redirect('/produtos')

    try:
        results = db.searchData('*','produtos','nome_prod',valor_inserido,like=True)
    except:
        return 'Não foi possível realizar a busca'

    if results == '':
        return render_template('pagina_dos_produtos.html', num = num, prods = results, num_elem = len(results), buscado = valor_inserido, state = state)

    if len(results) % 5 == 0:
        num = len(results) // 5
    elif len(results) % 5 <= 4:
        num = (len(results) // 5) + 1

    return render_template('pagina_dos_produtos.html', num = num, prods = results, num_elem = len(results), buscado = valor_inserido, state = state)



@app.route('/produto',methods = ["GET", "POST"])
def produto():
    global dados_prod

    id_prod = request.form.get('id_prod')

    try:
        dados_prod = db.searchData('*', 'produtos','id_prod',id_prod)[0]
    except:
        print('Não foi possível buscar os dados do produto')


    return render_template('pagina_do_produto.html', id_prod = id_prod, dados_prod = dados_prod)


@app.route('/add-carr', methods = ["GET", "POST"])
def add_carr():
    global target, email_logado
    
    
    if User.is_authenticated():
        id_prod = request.form.get('id_prod')

        try:
            prods = db.searchData('id_produto', 'carr', 'id_cliente', email_logado, 'id_produto', id_prod)
        except:
            print('Não foi possível realizar a busca')
            # return redirect('/produto')

        if len(prods) == 0:
            db.insertData('carr', email_logado, id_prod, 1)

        else:
            quant = db.searchData('quant', 'carr', 'id_cliente', email_logado, 'id_produto', id_prod)
            nova_quant = int(quant[0][0]) + 1
            db.updateData('carr', 'quant', nova_quant, 'id_cliente', email_logado, 'id_produto', id_prod)

        return redirect('/produto')

    else:
        target = 'prod'
        return redirect('/login')



@app.route('/serv')
def serv():
    return render_template('serv.html')
        




if __name__ == '__main__':
    
    app.run(debug = True)