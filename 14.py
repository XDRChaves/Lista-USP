pessoas_superior_50_peso_60 = 0
idade_inferior_150 = []
olhos_azuis = 0
ruivas_sem_olhos_azuis = 0

for _ in range(20):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    olhos = input("Digite a cor dos olhos (A, P, V, C): ")
    cabelos = input("Digite a cor dos cabelos (P, C, L, R): ")

    if idade > 50 and peso < 60:
        pessoas_superior_50_peso_60 += 1
    if altura < 1.50:
        idade_inferior_150.append(idade)
    if olhos == 'A':
        olhos_azuis += 1
    if cabelos == 'R' and olhos != 'A':
        ruivas_sem_olhos_azuis += 1

media_idades_inferior_150 = sum(idade_inferior_150) / len(idade_inferior_150)
percentagem_olhos_azuis = (olhos_azuis / 20) * 100

print(f"Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos: {pessoas_superior_50_peso_60}")
print(f"Média das idades das pessoas com altura inferior a 1,50: {media_idades_inferior_150:.2f}")
print(f"Percentagem de pessoas com olhos azuis entre todas as pessoas analisadas: {percentagem_olhos_azuis:.2f}%")
print(f"Quantidade de pessoas ruivas e que não possuem olhos azuis: {ruivas_sem_olhos_azuis}")
