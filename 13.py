pessoas_mais_90 = 0
idades = []

for _ in range(7):
    idade = int(input("13. Digite a idade: "))
    peso = float(input("Digite o peso: "))
    
    if peso > 90:
        pessoas_mais_90 += 1
    idades.append(idade)

media_idades = sum(idades) / len(idades)

print(f"Quantidade de pessoas com mais de 90 quilos: {pessoas_mais_90}")
print(f"Média das idades das sete pessoas: {media_idades:.2f}")
