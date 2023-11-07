pessoas_superior_50 = 0
alturas_10_20 = []
peso_inferior_40 = 0

for _ in range(25):
    idade = int(input("12. Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    
    if idade > 50:
        pessoas_superior_50 += 1
    if 10 <= idade <= 20:
        alturas_10_20.append(altura)
    if peso < 40:
        peso_inferior_40 += 1

media_alturas_10_20 = sum(alturas_10_20) / len(alturas_10_20)
percentagem_peso_inferior_40 = (peso_inferior_40 / 25) * 100

print(f"Quantidade de pessoas com idade superior a 50 anos: {pessoas_superior_50}")
print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {media_alturas_10_20:.2f} cm")
print(f"Percentagem de pessoas com peso inferior a 40 quilos: {percentagem_peso_inferior_40:.2f}%")
