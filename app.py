from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin

from sqlite3 import Cursor, Error


app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'


lm = LoginManager()
lm.init_app(app)
db = SQLAlchemy(app)


from flask import redirect, session, url_for, render_template, request
from sqlite3 import Error
from flask_login import current_user, login_user, logout_user

from models.database import ClassDatabase
from models.tables import ClassTableCarr, ClassTableHist, ClassTableProd, ClassTableServ, ClassTableUser



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



manage_db = ClassDatabase('kage.db')
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
vez = 0
vez_comp = 0


@app.route('/')
def homepage():

    return render_template('pagina_inicial.html')




@app.route('/login', methods = ["GET", "POST"])
def login():
    return render_template('login.html')



@app.route('/validando-login', methods = ["GET", "POST"])
def verific_login():
    global target

    email = request.form.get('email')
    senha = request.form.get('senha')


    user = User.query.filter_by(email_usu = email).first()

    if not email or not senha:
        return redirect('/login')

    try:
        user_data = table_user.getUserData(email)[0]
    except:
        return redirect('/login')
    

    if email == user_data[0] and senha == user_data[2]:
        login_user(user)        
        return redirect(f'/{target}')
        
    else:
        return 'Login Inválido'



@app.route('/logout')
def logout():

    logout_user()
    return redirect('/')



@app.route('/perfil')
def perfil():
    global target, user
    target = 'perfil'

    sinais = ['[',']','(',')', "'"]
    sinais2 = ['(',')', "'",',']

    if current_user.is_authenticated:
        try:    
            prods = []
            prods_carr = [] 
            valor_total = 0
            
            servicos = manage_db.searchData('*', 'servicos','email_cliente', current_user.get_id())
            info_pessoais = manage_db.searchData('*', 'usuarios', 'email_usu', current_user.get_id())
            hist = manage_db.searchData('id_produto', 'hist', 'id_cliente', current_user.get_id())
            carr = manage_db.searchData('id_produto','carr', 'id_cliente', current_user.get_id())

            quant = str(manage_db.searchData('quant','carr', 'id_cliente', current_user.get_id()))
            for sinal in sinais:
                quant = quant.replace(sinal,'')
            quant = quant.replace(',' ," ")
            quant = quant.split()


            for item in hist:
                item = str(item)
                for sinal in sinais2:
                    item = item.replace(sinal, '')

                item = int(item)
                dados_prod = manage_db.searchData('*', 'produtos','id_prod', item)[0]
                prods.append(dados_prod)

            for prod in carr:
                prod = str(prod)
                for sinal in sinais2:
                    prod = prod.replace(sinal, '')
                
                prod = int(prod)
                dados_carr = manage_db.searchData('*', 'produtos','id_prod', prod)[0]
                prods_carr.append(dados_carr)


            for pos, produto in enumerate(prods_carr):  
                valor_total += int(produto[2]) * int(quant[pos])        

        except:
            '''nada'''

        
        return render_template('perfil.html', servicos = servicos, num_serv = len(servicos), dados = info_pessoais, num_prods = len(prods), prods = prods,  prods_carr = prods_carr, tamanho = len(prods_carr), valor_total_carr = valor_total, quant_prod = quant)
    
    else:
        return redirect('/login')




@app.route('/cadastro')
def cadastro():
    global aste, vez, advise

    if vez %2 == 0:
        return render_template("cadastro.html")

    elif vez %2 == 1:
        vez += 1
        return render_template("cadastro.html", p = advise, ast = aste, value_email = email, value_senha = senha, value_nome = nome, value_cpf = cpf, value_est = estado, value_cid = cidade, value_bair = bairro, value_rua = rua, value_num = str(numero), value_comp = comp)
    



@app.route('/inserir-dados', methods = ['POST', 'GET'])
def insert_cad():

    global advise, vez, target
    global email, senha, nome, cpf, estado, cidade, bairro, rua, numero, comp
    i = 0

    try:
        email = request.form.get('email')
        senha = request.form.get('senha')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        estado = request.form.get('est')
        cidade = request.form.get('cid')
        bairro  = request.form.get('bair')
        rua = request.form.get('rua')
        numero = request.form.get('num')
        comp = request.form.get('comp')

        dados = [email,nome,senha,cpf,estado,cidade,bairro,rua,numero,comp]

        for dado in dados:
            if dado == '':
                advise = "É preciso preencher todos os campos"
                aste = '*'
                i += 1
                vez += i
                return redirect ('/cadastro')


        dom_aceitos = ['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com']

        email_testado = email
        email_testado = email_testado.replace('@', ' @')
        email_testado = email_testado.split()


        if email_testado[1] in dom_aceitos:

            emails = manage_db.searchData('email_usu', 'usuarios')

            if email in str(emails):
                advise = 'Email inválido'
                i += 1
                vez += i
                return redirect ('/cadastro')
        else:
            advise = 'Email inválido'
            i += 1
            vez += i
            return redirect ('/cadastro')

        cpf_usuarios = manage_db.searchData('cpf', 'usuarios')
        cpf_usuarios = str(cpf_usuarios)

        if len(cpf) == 11:
            if cpf in cpf_usuarios:
                advise = 'CPF já cadastrado em outra conta'
                aste = '*'
                i += 1
                vez += i
                return redirect('/cadastro')

        else:
            advise = 'CPF inválido'
            aste = '*'
            i += 1
            vez += i
            return redirect('/cadastro')


        numero = int(numero)

        try:
            manage_db.insertData('usuarios', email, senha, nome, cpf, estado, cidade, bairro, rua, numero, comp)
        except Error as erro:
            print(erro)
            if '1062' in str(erro):
                i += 1
                vez += i
                advise = 'Usuário já existente' 
                return redirect('/cadastro')
            
    except:
        '''nada'''

    return 'Cadastro concluído com sucesso!'




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
        results = manage_db.searchData('*','produtos','nome_prod',valor_inserido,like=True)
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
    if id_prod:
        id_prod_busca = id_prod

    try:
        dados_prod = manage_db.searchData('*', 'produtos','id_prod',id_prod_busca)[0]
    except:
        print('Não foi possível buscar os dados do produto')

    return render_template('pagina_do_produto.html', id_prod = id_prod, dados_prod = dados_prod)





@app.route('/add-carr', methods = ["GET", "POST"])
def add_carr():
    global target
    
    
    if current_user.is_authenticated:
        id_prod = request.form.get('id_prod')

        try:
            prods = manage_db.searchData('id_produto', 'carr', 'id_cliente', current_user.get_id(), 'id_produto', id_prod)
        except:
            print('Não foi possível realizar a busca')
            return redirect('/produto')

        if len(prods) == 0:
            manage_db.insertData('carr', email_logado, id_prod, 1)

        else:
            quant = manage_db.searchData('quant', 'carr', 'id_cliente', current_user.get_id(), 'id_produto', id_prod)
            nova_quant = int(quant[0][0]) + 1
            manage_db.updateData('carr', 'quant', nova_quant, 'id_cliente', current_user.get_id(), 'id_produto', id_prod)

        return redirect('/produto')

    else:
        target = 'produto'
        return redirect('/login')



@app.route('/rev-carr')
def rev_carr():
    global target

    if current_user.is_authenticated:

        id_prod = request.form.get('id_prod')

        try:
            prods = manage_db.searchData('id_produto', 'carr', 'id_cliente', current_user.get_id(), 'id_produto', id_prod)
        except:
            print('Não foi possível realizar a busca')
            return redirect('/produto')

        try:
            manage_db.deleteData('carr', 'id_cliente', current_user.get_id(), 'id_produto', id_prod)
        except:
            return redirect('/')
    
    else:
        target = 'carrinho'
        return redirect('/login')


@app.route('/carrinho', methods = ["GET", "POST"])
def carrinho():
    global user, target, state 

    if current_user.is_authenticated:

        list_prods = []
        quant = []
        valor = 0

        try:
            viewed_prod = request.form.get('id_prod')

            try:
                prods = manage_db.searchData('id_produto', 'carr', 'id_cliente', current_user.get_id(), 'id_produto', viewed_prod)
            except:
                print('Não foi possível realizar a busca')
                return redirect('/produto')

            if len(prods) == 0:
                manage_db.insertData('carr', current_user.get_id(), viewed_prod, 1)
                print('Não foi possível inserir produto')

            else:
                quant = manage_db.searchData('quant', 'carr', 'id_cliente', current_user.get_id(), 'id_produto', viewed_prod)
                nova_quant = int(quant[0][0]) + 1
                manage_db.updateData('carr', 'quant', nova_quant, 'id_cliente', current_user.get_id(), 'id_produto', viewed_prod)

                print('Não foi possível adicionar o produto')
        except:
            print('Não foi possível inserir produto no carrinho')

        try:
            id_prods = manage_db.searchData('id_produto, quant','carr','id_cliente', current_user.get_id())

            for pos, id_prod in enumerate(id_prods):
                prods = manage_db.searchData('*', 'produtos', 'id_prod',id_prod[0])
                list_prods.append(prods[0][:])
                valor += int(prods[0][2]) * id_prods[pos][1]
                quant.append(id_prods[pos][1])
                prods.clear()
        except:
            return render_template('carrinho.html')


        return render_template('carrinho.html', tamanho = len(list_prods), prods = list_prods, quant = quant , valor = valor, state = state)

    else:
        target = 'carrinho'
        return redirect('/login')






@app.route('/pag-compra', methods = ["POST", "GET"])
def pag_compra():
    global user, state, aviso_comp, vez_comp

    list_prods = []
    quant = []
    valor = 0   

    try:
        id_prods = manage_db.searchData('id_produto, quant','carr','id_cliente', current_user.get_id())
        print(id_prods)
        for pos, id_prod in enumerate(id_prods):
            prods = manage_db.searchData('*', 'produtos', 'id_prod', id_prod[0])
            list_prods.append(prods[0][:])
            valor += int(prods[0][2]) * id_prods[pos][1]
            quant.append(id_prods[pos][1])
            prods.clear()
    except:
        print('Não foi possível buscar os dados dos produtos')
        return redirect('/produto')

    frete = valor * 0.05

    if vez_comp % 2 == 0:
        aviso_comp = ''
        return render_template('pagina_de_compra.html', prods = list_prods, valor = valor, frete = frete, tamanho = len(list_prods), quant =  quant, aviso_comp = aviso_comp)
    elif vez_comp % 2 == 1:
        vez_comp += 1
        return render_template('pagina_de_compra.html', prods = list_prods, valor = valor, frete = frete, tamanho = len(list_prods), quant =  quant, aviso_comp = aviso_comp)




@app.route('/entrega-pagamento', methods = ["POST", "GET"])
def entrega_pagamento():
    global aviso_comp, vez_comp, dados_compra

    list_prods = []
    quant = []
    valor = 0  

    email_compra = request.form.get('email-compra')
    nome_compra = request.form.get('nome-compra')
    sobrenome_compra = request.form.get('dobrenome_compra')
    cpf_compra = request.form.get('cpf-compra')
    telefone_compra = request.form.get('telefone-compra')

    dados_compra = [email_compra, nome_compra, sobrenome_compra, cpf_compra, telefone_compra]


    try:
        for item in dados_compra:
            if item == '':
                vez_comp += 1
                aviso_comp = 'É preciso preencher todos os campos'
                return redirect('/pag-compra')

        if len(cpf_compra) != 11:
            vez_comp += 1
            aviso_comp = 'CPF inválido'
            return redirect('/pag-compra')

        if not cpf_compra.isnumeric():
            vez_comp += 1
            aviso_comp = 'CPF inválido'
            return redirect('/pag-compra')
    
    except:
        vez_comp += 1
        return redirect('/pag-compra')

    try:
        id_prods = manage_db.searchData('id_produto, quant','carr','id_cliente', current_user.get_id())
        print(id_prods)
        for pos, id_prod in enumerate(id_prods):
            prods = manage_db.searchData('*', 'produtos', 'id_prod', id_prod[0])
            list_prods.append(prods[0][:])
            valor += int(prods[0][2]) * id_prods[pos][1]
            quant.append(id_prods[pos][1])
            prods.clear()
    except:
        print('Não foi possível buscar os dados dos produtos')
        return redirect('/produto')

    frete1 = valor * 0.03
    frete2 = valor * 0.0425

    return render_template('entr-pag.html' ,prods = list_prods, valor = valor, frete1 = frete1, frete2 = frete2, tamanho = len(list_prods), quant =  quant)




@app.route('/finalizar-compra', methods = ["POST", "GET"])
def finalizar_compra():

    cep_compra = request.form.get('cep')
    rua_compra = request.form.get('rua-compra')
    num_compra = request.form.get('numero-compra')
    comp_compra = request.form.get('comp-compra')
    bair_compra = request.form.get('bairro')
    cidade_compra = request.form.get('cidade')
    estado_compra = request.form.get('estado')
    num_cartao = request.form.get('num-card')
    nome_cartao = request.form.get('nome-card')
    mes_cartao = request.form.get('mes')
    ano_cartao = request.form.get('ano')
    cod_segur = request.form.get('cod-sec')

    dados = [cep_compra, rua_compra, num_compra, comp_compra, bair_compra, cidade_compra, estado_compra, num_cartao, nome_cartao, mes_cartao, ano_cartao, cod_segur]

    for elem in dados:
        if not elem:
            return redirect('/entrega-pagamento')   

    try:
        produtos = manage_db.searchData('id_produto', 'carr', 'id_cliente', current_user.get_id())
        for produto in produtos:
            manage_db.insertData('hist', current_user.get_id(), produto[0], commit=False)
    except:
        manage_db.closeConn()
        return 'Não foi possível realizar a compra'

    manage_db.con.commit()
    manage_db.closeConn()
    return 'Compra realizada com sucesso'







@app.route('/serv')
def serv():
    global user, target, state

    if current_user.is_authenticated:
        return render_template('serv.html')

    else:
        target = 'serv'
        return redirect('/login')
        



@app.route('/insert-serv', methods = ["POST", "GET"])
def insert_serv():
    global user


    if current_user.is_authenticated:
        cliente = request.form.get('cliente')
        quant_manut = int(request.form.get('quant-serv'))
        type_serv = request.form.get('type-serv')

        maquinas = []

        if quant_manut <= 5:
            for i in range(0,quant_manut):
                mod_maq = request.form.get(f'mod-maq{i+1}')
                detal = request.form.get(f'detal{i+1}')
                info = [mod_maq, detal]
                maquinas.append(info[:])
                info.clear()


            try:
                for i in range(0, quant_manut):
                    maq = maquinas[i][0]
                    det = maquinas[i][1]
                    table_serv.createServ(current_user.get_id(),cliente,maq,'Desconhecido',0.0,det,'Em Avaliação', type_serv    , commit=False)

            except Error as erro:
                print(f'Não foi possível registrar os serviços         {erro}')
                table_serv.db.closeConn()
                return redirect('/serv')

            table_serv.db.con.commit()
            table_serv.db.closeConn()
            print('Serviços registrados com sucesso')
            return redirect('/serv')

        else:
            print('Número de registros inválido')
            return redirect('/serv')

    else:
        print('Usuário não logado')
        return redirect('/login')

    


@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


@app.route('/quem-somos-nos')
def quem_somos_nos():
    return render_template('quem_somos_nos.html')



@app.route('/login-admin')
def login_admin():
    global target
    target = 'admin'
    return render_template('login')

@app.route('/admin')
def admin():
    return  render_template('admin.html')



if __name__ == '__main__':
    app.run(debug = True)