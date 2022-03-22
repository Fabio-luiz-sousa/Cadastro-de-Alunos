
print('###############################################################')
print("\t\t\tCADASTRO DE ALUNOS")
print('###############################################################')
dados = {'matricula': [], 'nome': [], 'nota1': [], 'nota2': [], 'nota3': []}


while True:

    print('\t\t\t1.Adicionar\n\t\t\t2.Pesquisar\n\t\t\t3.Listar\n\t\t\t4.Excluir')
    op = input('O que voce quer fazer? ')

    def Adicionar():
        op = 's'
        while op == 's':
            insere_matricula = input('Digite a matricula do aluno(a): ')
            if insere_matricula in dados['matricula']:
                print('Erro!!! Esse número de matricula já existe')
                continue
            else:
                dados['matricula'].append(insere_matricula)
            insere_nome = input('Digite o nome do aluno(a): ')
            dados['nome'].append(insere_nome)
            insere_nota1 = input(
                'Digite a nota da primeira prova do aluno(a): ')
            dados['nota1'].append(insere_nota1)
            insere_nota2 = input(
                'Digite a nota da segunda prova do aluno(a): ')
            dados['nota2'].append(insere_nota2)
            insere_nota3 = input(
                'Digite a nota da terceira prova do aluno(a): ')
            dados['nota3'].append(insere_nota3)
            print('Aluno(a) adicionado(a) com seucesso!!')
           

            sair = input('Deseja continuar adicionando s/n? ')
            if sair == 'n':
                op = 'n'

    def Pesquisar():
        op = 's'
        while op == 's':
            modo_pesquisa = input(
                'PESQUISA:\n1.Nome\n2.Matricula\nO que voce quer fazer? ')
            if modo_pesquisa == '1':
                pesquisa_nome = input(
                    'Digite o nome do aluno(a) a ser pesquisado(a): ')
                if pesquisa_nome not in dados['nome']:
                    print('Esse aluno(a) nao exixte!!')
                else:
                    for i in dados['nome']:
                        indice = dados['nome'].index(i)
                        if i == pesquisa_nome:
                            print('Matricula:', dados['matricula'][indice])
                            print('Nome:', dados['nome'][indice])
                            print('Nota1:', dados['nota1'][indice])
                            print('Nota2:', dados['nota2'][indice])
                            print('Nota3:', dados['nota3'][indice])
                            print()
            else:
                pesquisa_matricula = input(
                    'Digite a matricula do aluno(a) a ser pesquisado(a): ')
                if pesquisa_matricula not in dados['matricula']:
                    print('Esse aluno(a) nao exixte!!')
                else:
                    indice = dados['matricula'].index(pesquisa_matricula)
                    print('Matricula:', dados['matricula'][indice])
                    print('Nome:', dados['nome'][indice])
                    print('Nota1:', dados['nota1'][indice])
                    print('Nota2:', dados['nota2'][indice])
                    print('Nota3:', dados['nota3'][indice])

            sair = input('Deseja continuar pesquisando s/n? ')
            if sair == 'n':
                op = 'n'

    def Listar():
        if dados['matricula'].__len__() == 0:
            print('Nenhum aluno(a) registrado!!')
        else:
            v = dados['matricula'].__len__()
            for i in range(0, v):
                print()
                print('Matricula:', dados['matricula'][i])
                print('Nome:', dados['nome'][i])
                print('Nota1:', dados['nota1'][i])
                print('Nota2:', dados['nota2'][i])
                print('Nota3:', dados['nota3'][i])
                print(30*'-')

    def Excluir():
        op = 's'
        while op == 's':
            ex = input('Digite a matricula do aluno(a) a ser excluido(a): ')
            if ex not in dados['matricula']:
                print('Nenhum aluno(a) encontrado(a) com esse numero de matricula!!')
            else:
                indice = dados['matricula'].index(ex)
                dados['matricula'].pop(indice)
                dados['nome'].pop(indice)
                dados['nota1'].pop(indice)
                dados['nota2'].pop(indice)
                dados['nota3'].pop(indice)
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
    else:
        Excluir()

    sair = input('Deseja voltar ao menu s/n ? ')
    if sair == 'n':
        break
