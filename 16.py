idades = []
peso_mais_90_altura_150 = 0
idade_10_30_altura_190 = 0

for _ in range(10):
    idade = int(input("16. Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    
    idades.append(idade)
    if peso > 90 and altura < 1.50:
        peso_mais_90_altura_150 += 1
    if 10 <= idade <= 30 and altura > 1.90:
        idade_10_30_altura_190 += 1

media_idades = sum(idades) / len(idades)
percentagem_peso_mais_90_altura_150 = (peso_mais_90_altura_150 / 10) * 100
percentagem_idade_10_30_altura_190 = (idade_10_30_altura_190 / 10) * 100

print(f"Média das idades das dez pessoas: {media_idades:.2f}")
print(f"Quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50: {peso_mais_90_altura_150}")
print(f"Percentagem de pessoas com idade entre 10 e 30 anos e altura superior a 1,90: {percentagem_idade_10_30_altura_190:.2f}%")
