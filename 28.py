salarios = []
num_filhos = []
total_salario = 0
total_filhos = 0
maior_salario = -1
pessoas_ate_150 = 0

while True:
    salario = float(input("Digite o salário (ou um valor negativo para encerrar): "))
    if salario < 0:
        break
    num_filho = int(input("Digite o número de filhos: "))
    
    total_salario += salario
    total_filhos += num_filho
    salarios.append(salario)
    num_filhos.append(num_filho)
    
    if salario <= 150:
        pessoas_ate_150 += 1
    if salario > maior_salario:
        maior_salario = salario

media_salario = total_salario / len(salarios)
media_filhos = total_filhos / len(num_filhos)
percentagem_ate_150 = (pessoas_ate_150 / len(salarios)) * 100

print(f"Média do salário da população: R${media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário: R${maior_salario:.2f}")
print(f"Percentagem de pessoas com salários até R$ 150,00: {percentagem_ate_150:.2f}%")
