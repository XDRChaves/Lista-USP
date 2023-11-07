alunos = []

for _ in range(10):
    matricula = int(input("Digite o número da matrícula: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    frequencia = int(input("Digite o número de aulas frequentadas: "))

    nota_final = (nota1 + nota2 + nota3) / 3
    aprovado = nota_final >= 6 and frequencia >= 40

    alunos.append((matricula, nota_final, aprovado))

maiores_notas = max(alunos, key=lambda x: x[1])
menores_notas = min(alunos, key=lambda x: x[1])
reprovados = sum(1 for aluno in alunos if not aluno[2])
percentagem_reprovados_freq_abaixo_minima = (reprovados / 10) * 100

print("Número da Matrícula | Nota Final | Mensagem")
for aluno in alunos:
    mensagem = "Aprovado" if aluno[2] else "Reprovado"
    print(f"{aluno[0]} | {aluno[1]:.2f} | {mensagem}")

print(f"Maior nota da turma: {maiores_notas[1]:.2f}")
print(f"Menor nota da turma: {menores_notas[1]:.2f}")
print(f"Total de alunos reprovados: {reprovados}")
print(f"Percentagem de alunos reprovados por frequência abaixo da mínima necessária: {percentagem_reprovados_freq_abaixo_minima:.2f}%")
