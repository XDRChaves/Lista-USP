idade_otimo = []
quantidade_regular = 0
percentagem_bom = 0

for _ in range(15):
    idade = int(input("Digite a idade: "))
    opiniao = int(input("Digite a opinião (Ótimo - 3, Bom - 2, Regular - 1): "))
    
    if opiniao == 3:
        idade_otimo.append(idade)
    if opiniao == 1:
        quantidade_regular += 1
    if opiniao == 2:
        percentagem_bom += 1

media_idades_otimo = sum(idade_otimo) / len(idade_otimo)
percentagem_bom = (percentagem_bom / 15) * 100

print(f"Média das idades das pessoas que responderam ótimo: {media_idades_otimo:.2f}")
print(f"Quantidade de pessoas que respondeu regular: {quantidade_regular}")
print(f"Percentagem de pessoas que respondeu bom entre todos os espectadores: {percentagem_bom:.2f}%")
