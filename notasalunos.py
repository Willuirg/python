def main():
    alunos = []

    while True:
        print("\n1 - Adicionar aluno")
        print("2 - Ver alunos e notas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            try:
                nota = float(input("Nota do aluno: "))
            except ValueError:
                print("Nota inválida. Digite um número.")
                continue

            alunos.append((nome, nota))
            print(f"Aluno {nome} adicionado com nota {nota}.")

        elif opcao == "2":
            if not alunos:
                print("Nenhum aluno cadastrado ainda.")
                continue

            print("\nLista de alunos e situação:")
            for nome, nota in alunos:
                situacao = "APROVADO" if nota >= 60 else "REPROVADO"
                print(f"{nome}: {nota:.2f} - {situacao}")

        elif opcao == "3":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
