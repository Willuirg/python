alunos = []
while(True):
    print("Cadastro e lista de alunos")
    print("Escolha uma das opções abaixo")
    print("1 - Cadastrar um aluno")
    print("2 - Ver lista de alunos cadastrados")
    print("3 - Sair")
    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)
        print("Aluno cadastrado.")
    elif escolha == 2:
        if len(alunos) == 0:
            print("Erro! Não há nenhum aluno cadastrado.")
        else:
            print("Lista de alunos:\n")
            for aluno in alunos:
                print(alunos)
    elif escolha == 3:
        print("Programa encerrado!")
        break
    else:
        print("Digite um número válido.")
