import email
import sqlite3
from sqlite3 import Error
from models.database import ClassDatabase

class ClassTableUser:

    colunas = ['email_usu','nome_usu','senha','cpf','estado','cidade','bairro','rua','num','complemento']

    def __init__(self, name_db, admin=False) -> None:
        
        self.name_db = name_db
        self.admin = admin
        self.db = ClassDatabase(self.name_db)



    def getUserData(self, email:str):
        return self.db.searchData('*', 'usuarios','email_usu',email)


    def searchUser(self,email):
        if email in str(self.db.searchData('email_usu', 'usuarios')):
            return True
        else:
            return False



    def createUser(self, email:str, name:str, senha:str, cpf:str,*endereco):

        if self.searchUser(email):
            print('Usuário já existente')
            return

        try:
            estado, cidade, bairro, rua, num, comp = endereco
            self.db.insertData('usuarios', email, name,senha, cpf, estado, cidade, bairro, rua, num, comp)
        except:
            return

        print('Cadastro concluído com sucesso')



    def updateUser(self,email,*novos_dados):

        if len(novos_dados) != 10:
            print('Número de parâmetros incorreto')
            return

        try:
            for coluna, dado in zip(self.colunas,novos_dados):
                self.db.updateData('usuarios', coluna, dado, 'email_usu',email,commit=False)
        except:
            print('Não foi possível atualizar os dados')
            self.db.closeConn()
            return

        self.db.con.commit()
        self.db.closeConn()
        print('Dados atualizados com sucesso')



    def deleteUser(self,email):

        if not self.searchUser(email):
            print('Usuário não existe')
            return

        try:
            self.db.deleteData('usuarios','email_usu',email)
        except:
            print('Não foi possível deletar usuário')
            return
        
        print('Usuário excluído com sucesso')






class ClassTableProd:

    colunas = ['nome_prod', 'valor', 'quant', 'id_de_fabricacao', 'img_prod']

    def __init__(self, name_db):

        self.name_db = name_db
        self.db = ClassDatabase(self.name_db)

    def getProdData(self, id_prod):
        return self.db.searchData('*','produtos','id_prod',id_prod)

    def searchProd(self,value_search,param_busca):

        if param_busca == 'id_prod':
            if value_search in str(self.db.searchData('id_prod', 'produtos')):
                return True
            else: 
                return False

        elif param_busca == 'nome_prod':
            if value_search in str(self.db.searchData('nome_prod', 'produtos')):
                return True
            else:
                return False



    def createProd(self, nome_prod:str, valor:float, quant:int, id_fab:str, img_prod:str):

        if self.searchProd(nome_prod,'nome_prod'):
            print('Nome de Produto já cadastrado')

        try:
            self.db.insertData('produtos', 0, nome_prod, valor, quant, id_fab, img_prod)
        except:
            print('Não foi possível cadastrar o porduto')

        print('Produto cadastrado com sucesso')
        


    def updateProd(self,id_prod,*new_values):

        if len(new_values) != 5:
            print('Número de parâmetros incorreto')
            return

        try:
            for coluna,value in zip(self.colunas, new_values):
                self.db.updateData('produtos', coluna, value, 'id_prod', id_prod, commit=False)
        except:
            print('Não foi possível alterar os dados')
            self.db.closeConn()
            return
        
        self.db.con.commit()
        self.db.closeConn()
        print('Produto atualizado com sucesso')
        

    def deleteProd(self,id_prod):

        if not self.searchProd(id_prod,'id_prod'):
            print('Produto não existe')

        try:
            self.db.deleteData('produtos','id_prod',id_prod)
        except:
            print('Não foi possível excluir o produto')
            return

        print('Produto excluído com sucesso')




class ClassTableServ:

    colunas = ['']

    def __init__(self,name_db) -> None:
        
        self.name_db = name_db
        self.db = ClassDatabase(self.name_db)


    def getServData(self,id_serv):
        return self.db.searchData('*','servicos','id_serv',id_serv)



    def searchServ(self,id_serv,email_cliente):
        if id_serv in str(self.db.searchData('id_serv','servicos','email_cliente',email_cliente)):
            return True
        else:
            return False



    def createServ(self, email_cliente, nome_cliente, mod_maq, valor, descricao, status):

        try:
            self.db.insertData('servicos', email_cliente, nome_cliente, mod_maq, valor, descricao, status)
        except:
            print('Não foi possível cadastrar o serviço')
            return

        print('Serviço cadastrado com sucesso')


    def updateServ(self,id_serv,email_cliente,*new_values):
        
        if not self.searchServ(id_serv,email_cliente):
            print('Serviço não existe')
            return

        if len(new_values) != 6:
            print('Número de parâmetros incorreto')
            return

        try:
            for coluna, value in zip(self.colunas,new_values):
                self.db.updateData('servicos', coluna, value,'id_serv', id_serv, commit=False)
        except:
            print('Não foi possível atualizar o serviço')
            self.db.closeConn()
            return

        self.db.con.commit()
        self.db.closeConn()
        print('Serviço atualizado com sucesso')

    def deleteServ(self,id_serv,email_cliente):

        if not self.searchServ(id_serv,email_cliente):
            print('Serviço não existe')
            return

        try:
            self.db.deleteData('servicos','id_serv',id_serv, 'email_cliente', email_cliente)
        except:
            print('Não foi possível excluir o Serviço')
            return

        print('Serviço excluído com sucesso')






class ClassTableCarr:
    def __init__(self,name_db):
        
        self.name_db = name_db
        self.db = ClassDatabase(self.name_db)



    def getCarrData(self, id_cliente):
        return self.db.searchData('*','carr','id_cliente',id_cliente)



    def searchCarr(self, id_prod, id_cliente):

        if id_prod in str(self.db.searchData('id_produto','carr','id_cliente',id_cliente)):
            return True
        else:
            return False


    def addProdCarr(self, id_prod, id_cliente, quant):

        if self.searchCarr(id_prod, id_cliente):
            print('Produto já adicionado ao carrinho')
            return

        try:
            self.db.insertData('carr', id_cliente, id_prod, quant)
        except:
            print('Não foi possível adicionar o produto ao Carrinho')
            return

        print('Produto adicionado ao carrinho com sucesso')


    
    def updateCarr(self, nova_quant, id_prod, id_cliente):
        
        try:
            self.db.updateData('carr','quant', nova_quant, 'id_produto', id_prod, 'id_cliente', id_cliente)
        except:
            print('Não foi possível atualizar o carrinho')

        print('Carrinho atualizado com sucesso')


    def deleteCarr(self, id_prod, id_cliente):

        if self.searchCarr(id_prod, id_cliente):
            print('O produto não está no carrinho')
            return

        try:
            self.db.deleteData('carr', 'id_produto', id_prod, 'id_cliente', id_cliente)
        except:
            print('Não foi possível deletar o produto')

        print('Produto removido com sucesso')





class ClassTableHist:
    def __init__(self,name_db):
        
        self.name_db = name_db
        self.db = ClassDatabase(self.name_db)



    def getHistData(self, id_cliente):
        return self.db.searchData('*','hist','id_cliente',id_cliente)



    def searchHist(self, id_prod, id_cliente):

        if id_prod in str(self.db.searchData('id_produto','hist','id_cliente',id_cliente)):
            return True
        else:
            return False


    def addProdHist(self, id_prod, id_cliente):

        if self.searchCarr(id_prod, id_cliente):
            print('Produto já adicionado ao histórico')
            return

        try:
            self.db.insertData('hist', id_cliente, id_prod)
        except:
            print('Não foi possível adicionar o produto ao Histórico')
            return

        print('Produto adicionado ao histórico com sucesso')



    def deleteHist(self, id_prod, id_cliente):

        if self.searchCarr(id_prod, id_cliente):
            print('O produto não está no histórico')
            return

        try:
            self.db.deleteData('hist', 'id_produto', id_prod, 'id_cliente', id_cliente)
        except:
            print('Não foi possível deletar o produto')

        print('Produto removido com sucesso')



if __name__ == '__main__':
    'nada'