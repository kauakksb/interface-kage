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


def perfil():

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

        
        return render_template('perfil.html', servicos = servicos, num_serv = len(servicos), dados = info_pessoais, num_prods = len(prods), prods = prods,  prods_carr = prods_carr, tamanho = len(prods_carr), valor_total_carr = valor_total, quant_prod = quant, titulo = 'Área Restrita', file = 'perfil', filejs = 'area-restrita')
    
    else:
        return redirect('/login')