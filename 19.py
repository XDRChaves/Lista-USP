idades = []
while True:
    idade = int(input("Digite a idade (ou 0 para encerrar): "))
    if idade == 0:
        break
    idades.append(idade)

if len(idades) > 0:
    media_idades = sum(idades) / len(idades)
    print(f"Média das idades: {media_idades:.2f}")
else:
    print("Nenhuma idade foi digitada.")
