import psycopg2
import pandas as pd
from senha import senha


class ConectaDB():
    def __init__(self):
        host = 'localhost'
        dbname = 'Cadastro_Alunos'
        user = 'postgres'
        password = senha
        sslmode = 'allow'
        conn_string = f'host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}'
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()

        def cria_tabela_alunos():
            self.cursor.execute('CREATE TABLE IF NOT EXISTS public.alunos ('
                                'matricula integer NOT NULL,'
                                'nome_aluno text COLLATE pg_catalog."default" NOT NULL,'
                                'CONSTRAINT alunos_pkey PRIMARY KEY (matricula))'
                                'TABLESPACE pg_default;'

                                'ALTER TABLE IF EXISTS public.alunos'
                                    ' OWNER to postgres;'                                                                     
            )
        cria_tabela_alunos()
        def cria_tabela_notas_alunos():
            self.cursor.execute('CREATE TABLE IF NOT EXISTS public.notas_alunos ('
            'matricula integer NOT NULL,'
            'nota_1 numeric,'
            'nota_2 numeric,'
            'nota_3 numeric,'
            'CONSTRAINT fk_matricula FOREIGN KEY (matricula)'
                'REFERENCES public.alunos (matricula) MATCH SIMPLE'
                ' ON UPDATE CASCADE'
                ' ON DELETE CASCADE'
                ' NOT VALID)'
            'TABLESPACE pg_default;'
            'ALTER TABLE IF EXISTS public.notas_alunos'
            ' OWNER to postgres;')
        cria_tabela_notas_alunos()
                                        


class ManipulaDB(ConectaDB): 

    

    def insere_aluno_db(self, matricula, nome_aluno):
        self.cursor.execute(
            'INSERT INTO alunos (matricula,nome_aluno) VALUES (%s,%s)', (matricula, nome_aluno))
        self.conn.commit()

    def ver_dados_aluno_db(self):
        self.cursor.execute('SELECT * FROM alunos')
        pega_dados = self.cursor.fetchall()
        def ver_dados_notas_alunos_db():
            self.cursor.execute('SELECT * FROM notas_alunos')
            pega_dados = self.cursor.fetchall()
            ver_dados_notas = pd.DataFrame(pega_dados, columns=[
                                    'Matrícula', 'P1', 'P2', 'P3'])
            return ver_dados_notas
        ver_dados_notas=ver_dados_notas_alunos_db()
        if len(pega_dados)!=0:
            ver_dados=pd.DataFrame(pega_dados,columns=['Matrícula', 'Nome do Aluno(a)'])
            junta_data_frame=pd.merge(ver_dados,ver_dados_notas,how='outer')
            print(junta_data_frame)
        else:
            print('Nenhum aluno(a) foi registrado(a)')
            
    def pesquisa_aluno_db(self, matricula):
        self.cursor.execute(
            'SELECT * FROM alunos WHERE matricula=%s', (matricula,))
        pega_dados = self.cursor.fetchall()
        if len(pega_dados)!=0:
            ver_dados = pd.DataFrame(pega_dados, columns=[
                                    'Matrícula', 'Nome do Aluno(a)'])
            print(ver_dados)
        else:
            print('Esse número de matricula não existe')

    def atualiza_dados_aluno_db(self, matricula_nova, nome_aluno, matricula):
        self.cursor.execute('UPDATE alunos SET matricula=%s, nome_aluno=%s WHERE matricula=%s',
                            (matricula_nova, nome_aluno, matricula))
        self.conn.commit()

    def deleta_alunos_db(self, matricula):
        self.cursor.execute(
            'DELETE FROM alunos WHERE matricula=%s', (matricula,))
        self.conn.commit()

    
    def insere_notas_aluno_db(self, matricula, nota_1, nota_2, nota_3):
        self.cursor.execute(
            'INSERT INTO notas_alunos (matricula,nota_1,nota_2,nota_3) VALUES (%s,%s,%s,%s)', (matricula, nota_1, nota_2, nota_3))
        self.conn.commit()

    

    def pesquisa_notas_alunos_db(self, matricula):
        self.cursor.execute(
            'SELECT * FROM notas_alunos WHERE matricula=%s ', (matricula,))
        pega_dados = self.cursor.fetchall()
        ver_dados = pd.DataFrame(pega_dados, columns=[
                                    'Matrícula', 'P1', 'P2', 'P3'])
        print(ver_dados)

    def atualiza_dados_notas_alunos_db(self, matricula_nova,matricula, nota_1, nota_2, nota_3):
        self.cursor.execute(
            'UPDATE notas_alunos SET matricula=%s, nota_1=%s, nota_2=%s, nota_3=%s WHERE matricula=%s', (matricula_nova,nota_1, nota_2, nota_3, matricula_nova))
        self.conn.commit()

    

    def fecha_db(self):
        self.cursor.close()
        self.conn.close()


#c = ManipulaDB()
#c.ver_dados_aluno_db()
#c.insere_aluno_db(106,'Felipe Luiz')
#c.atualiza_dados_aluno_db(104,'Felipe Luiz',106)
#c.ver_dados_aluno_db()
#c.fecha_db()
