from classes import ManipulaDB


print('###############################################################')
print("\t\t\tCADASTRO DE ALUNOS")
print('###############################################################')

conecta=ManipulaDB()



while True:

    print('\t\t\t1.Adicionar\n\t\t\t2.Pesquisar\n\t\t\t3.Listar\n\t\t\t4.Atualizar\n\t\t\t5.Excluir\n\t\t\t6.Sair')
    op = input('O que voce quer fazer? ')

    def Adicionar():
        op = 's'
        while op == 's':
            matricula=input('Digite a matrícula do aluno(a): ')
            nome_aluno=input('Digite o nome do aluno(a): ')
            nota_1=input('Digite a nota da P1: ')
            nota_2=input('Digite a nota da P2: ')
            nota_3=input('Digite a nota da P3: ')

            try:
                conecta.insere_aluno_db(matricula,nome_aluno)
                conecta.insere_notas_aluno_db(matricula,nota_1,nota_2,nota_3)
                print('Aluno(a) adicionado(a) com sucesso!!')
            except:
                print('Esse número de matricula já existe')
                return

            sair = input('Deseja continuar adicionando s/n? ')
            if sair == 'n':
                op = 'n'


    def Pesquisar():
        op = 's'
        while op == 's':
            matricula=input('Digite a matricula do aluno(a) a ser pesquisado(a): ')
            conecta.pesquisa_aluno_db(matricula)
            sair = input('Deseja continuar pesquisando s/n? ')
            if sair == 'n':
                op = 'n' 
    
    
    def Listar():
        conecta.ver_dados_aluno_db()
        print('###############################################################')

    def Atualizar():
        op='s'
        while op=='s':
            matricula=input('Digite a matricula do(a) aluno(a) a ser atualizado(a): ')
            nova_matricula=input('Digite a nova matricula do(a) aluno(a): ')
            novo_nome=input('Digite o nome do(a) aluno(a): ')
            nova_nota_p1=input('Digite a nova nota da P1 do(a) aluno(a): ')
            nova_nota_p1=int(nova_nota_p1)
            nova_nota_p2=input('Digite a nova nota da P2 do(a) aluno(a): ')
            nova_nota_p3=input('Digite a nova nota da P3 do(a) aluno(a): ')
            conecta.atualiza_dados_aluno_db(nova_matricula,novo_nome,matricula)
            conecta.atualiza_dados_notas_alunos_db(nova_matricula,matricula,nova_nota_p1,nova_nota_p2,nova_nota_p3)
            print('Dados atualizados com sucesso!!')
            sair = input('Deseja continuar atualizando s/n ? ')
            if sair == 'n':
                op = 'n'





    def Excluir():
        op = 's'
        while op == 's':
            matricula=input('Digite a matrícula do(a) aluno(a) a ser excluido(a): ')
            confirma=input('Deseja realmente excluir o(a) aluno(a) s/n ? ')
            if confirma=='n':
                sair = input('Deseja continuar excluindo s/n ? ')
                if sair == 'n':
                    op = 'n'
                return
            else:
                conecta.deleta_alunos_db(matricula)
                print('Aluno(a) excluido(a) com sucesso!!')
            sair = input('Deseja continuar excluindo s/n ? ')
            if sair == 'n':
                op = 'n'

    if op == '1':
        Adicionar()
    elif op == '2':
        Pesquisar()
    elif op == '3':
        Listar()
    elif op=='4':
        Atualizar()
    elif op==5:
        Excluir()
    else:
        break

    sair = input('Deseja voltar ao menu s/n ? ')
    if sair == 'n':
        break 
