import sqlite3
from sqlite3 import Cursor, Error


class ClassDatabase:

    cursor = None
    con = None
    state = False
    cl_created = False
    colunas = []

    def __init__(self, name_file):
        
        self.name_file = name_file


    def connection(self):
        if self.state == True:
            print('Conexão com o banco de dados em andamento')
            return

        try:
            self.con = sqlite3.connect(self.name_file)
        except:
            return "Não foi possível conectar"

        print(f'Conectado com sucesso ao banco de dados')
        self.cursor = self.con.cursor()

        self.state = True


    
    def closeConn(self):
        if not self.state:
            print('Não há conexão com o banco de dados em andamento')
            return

        self.cursor.close()
        self.con.close()

        print('Conexão com o banco de dados encerrada')
        self.state = False
        


    def setColumn(self, name:str, type_cl:type, length:int, null:bool=True, auto_in:bool=False, primary_key:bool=False):

        if type_cl == str:
            typeofcl = 'VARCHAR'
        elif type_cl == int:
            typeofcl = 'INT'
        elif type_cl == float:
            typeofcl = 'FLOAT'
         
        comando = f'''{name} {typeofcl}({length})'''

        if null == False:
            comando = f'{comando} NOT NULL'
        
            if auto_in == True:
                comando = f'{comando} AUTO_INCREMENT'

            if primary_key == True:
                comando = f'{comando} PRIMARY KEY'
                
        elif null == True:
            if auto_in == True or primary_key == True:
                print('Condições para criação de tabela não foram atendidas')
                return

        self.cl_created = True
        self.colunas += comando
        
        return self.colunas

    
    
    def createTable(self, name_tb:str, colunas:list):

        if self.cl_created == False:
            print('É preciso criar as colunas da tabela primeiro: setColumn()')
            return

        self.connection()

        if type(colunas) == list:
            # Escrevendo comando de criação de tabela
            comando = f'''CREATE TABLE {name_tb}('''
            for coluna in colunas:
                comando += coluna

            comando = comando+')'

            # Tentado executar comando de criação de tabela
            try:
                self.cursor.execute(comando)
            except Error as erro:
                print(erro)

            # Encerra a conexão com o banco de dados caso ela esteja ativa
            self.closeConn()

            self.cl_created = False
            self.colunas = []

        else:
            print('Algum valor inserido no parâmetro "colunas" não é uma lista')



    def getTables(self):
        self.connection()

        try:
            self.cursor.execute('select name from sqlite_master where type = "table"')
            colunas = self.cursor.fetchall()
        except Error as erro:
            return erro
    
        self.closeConn()
        return colunas



    def insertData(self, name_tb, *values, commit = True):
        self.connection()

        tamanho = len(values) - 1
        comando = f'''INSERT INTO {name_tb} VALUES('''

        # Adicionando valores ao comando de inserção de dados
        for pos,dado in enumerate(values):

            # Adiciona complemntentos de dados de acordo com o tipo de dado
            if type(dado) == str:
                dado = f'"{dado}"'
                if pos != tamanho:
                    dado = f'{dado}, '

            elif type(dado) == int or type(dado) == float:
                dado = str(dado)
                if pos != tamanho:
                    dado = f'{dado}, '

               
            comando += dado # Acrescentando dado à query

        comando += ');'

        # Tentando executar comando de inserção de dados na tabela
        self.cursor.execute(comando)
        if commit == True:
            self.con.commit()


        # Encerrando conexão com o banco de dados caso ainda esteja conectado
        if commit == True:
            self.closeConn()



    def searchData(self,info,name_tb, *param_search, like:bool=False):

        self.connection()
        comando = f'''SELECT {info} FROM {name_tb}'''

        # Comando SQL para um parâmetro de busca
        if len(param_search) == 2:
            
            id_busca , valor_busca = param_search
            comando = f'''{comando} WHERE {id_busca} = {valor_busca}'''

            if type(valor_busca) == str:
                comando = comando.replace(f'{valor_busca}',f'"{valor_busca}"')

                if like == True:
                    comando = comando.replace(f'"{valor_busca}"',f'"%{valor_busca}%"')
                    comando = comando.replace('=','LIKE')

        # Comando SQL para dois parâmetros de busca
        elif len(param_search) == 4:

            id_busca , valor_busca, id_busca2, valor_busca2 = param_search
            comando = f'''{comando} WHERE {id_busca} = {valor_busca} and {id_busca2} = {valor_busca2}'''

            if type(valor_busca) == str:
                comando = comando.replace(f'{valor_busca}',f'"{valor_busca}"')

                if like == True:
                    comando = comando.replace(f'"{valor_busca}"',f'"%{valor_busca}%"')
                    comando = comando.replace('=','LIKE')

            if type(valor_busca2) == str:
                comando = comando.replace(f'{valor_busca2}',f'"{valor_busca2}"')

                if like == True:
                    comando = comando.replace(f'"{valor_busca2}"',f'"%{valor_busca2}%"')
                    comando = comando.replace('=','LIKE')


        # Mensagem exibida caso o número de parâmetros inseridos não seja o ideal
        elif len(param_search) == 1 or len(param_search) ==  3 or len(param_search) > 4:
            print('O número de parâmetros inseridos está incorreto')
            self.closeConn()
            return

        # Tentando executar comando de busca
        try:
            self.cursor.execute(comando)
            retorno = self.cursor.fetchall()
        except Error as erro:
            retorno = erro
            print(retorno)
            self.closeConn()
            return 

        # Encerra a conexão com o banco de dados 
        self.closeConn()
        return retorno



    def updateData(self,tb_name,info,novo_valor, *param_search,commit=True):
        self.connection()

        if len(param_search) == 2:

            id_busca, valor_busca = param_search
            comando = f'UPDATE {tb_name} SET {info} = {novo_valor} WHERE {id_busca} = {valor_busca}'

            if type(valor_busca) == str:
                comando = comando.replace(f"{valor_busca}",f'"{valor_busca}"')

        elif len(param_search) == 4:

            id_busca, valor_busca, id_busca2, valor_busca2 = param_search
            comando = f'UPDATE {tb_name} SET {info} = {novo_valor} WHERE {id_busca} = {valor_busca} and {id_busca2} = {valor_busca2}'

            if type(valor_busca) == str:
                comando = comando.replace(f"{valor_busca}",f'"{valor_busca}"')
            
            if type(valor_busca2) == str:
                comando = comando.replace(f"{valor_busca2}",f'"{valor_busca2}"')

        elif len(param_search) == 1 or len(param_search) == 3 or len(param_search) == 0 or len(param_search) > 4:
            print('O número de parâmetros inseridos está incorreto')
            self.closeConn()
            return

        if type(novo_valor) == str:
            comando = comando.replace(f'{novo_valor}',f'"{novo_valor}"')

        


        try:
            self.cursor.execute(comando)
            if commit == True:
                self.con.commit()
        except Error as erro:
            print(erro)
            self.closeConn()
            return

        # Encerrando conexão com o banco de dados caso ainda esteja conectado
        if commit == True:
            self.closeConn()



    def deleteData(self,tb_name,*param_del):
        self.connection()

        if len(param_del) == 2:
            id_busca, valor_busca = param_del
            comando = f'DELETE FROM {tb_name} WHERE {id_busca} = {valor_busca}'

        elif len(param_del) == 4:
            id_busca, valor_busca, id_busca2, valor_busca2 = param_del
            comando = f'DELETE FROM {tb_name} WHERE {id_busca} = {valor_busca} and {id_busca2} = {valor_busca2}'

        elif len(param_del) == 1 or len(param_del) == 3 or len(param_del) > 4:
            print('O número de parâmetros inseridos está incorreto')
            self.closeConn()
            return

        try:
            self.cursor.execute(comando)
            self.con.commit()
        except Error as erro:
            print(erro)
            self.closeConn()
            return
        
        # Encerrando conexão com o banco de dados
        self.closeConn()


if __name__ == '__main__':
    'nada'