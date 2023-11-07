alturas = []
while True:
    idade = int(input("Digite a idade (ou uma idade menor ou igual a zero para encerrar): "))
    if idade <= 0:
        break
    altura = float(input("Digite a altura: "))
    
    if idade > 50:
        alturas.append(altura)

if alturas:
    media_alturas = sum(alturas) / len(alturas)
    print(f"Média das alturas das pessoas com mais de 50 anos: {media_alturas:.2f}")
else:
    print("Nenhuma altura foi registrada para pessoas com mais de 50 anos.")
