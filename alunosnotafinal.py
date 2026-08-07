quantidade_alunos = int(input("Digite a quantidade de alunos da turma: "))

notas = []

for aluno in range(1, quantidade_alunos + 1):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {aluno} (de 0 a 10): "))
        except ValueError:
            print("Valor inválido! Digite uma nota numérica de 0 a 10.")
            continue

        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")

media = sum(notas) / len(notas)
aprovados = sum(1 for nota in notas if nota >= 7)
recuperacao = sum(1 for nota in notas if 5 < nota < 7)
reprovados = sum(1 for nota in notas if nota <= 5)
menor_nota = min(notas)
maior_nota = max(notas)

print("\nRESULTADOS DA TURMA")
print("=" * 30)
print(f"Média da turma: {media:.2f}")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos em recuperação: {recuperacao}")
print(f"Quantidade de alunos reprovados: {reprovados}")
print(f"Menor nota: {menor_nota:.1f}")
print(f"Maior nota: {maior_nota:.1f}")
