audiencia_canais = {'4': 0, '5': 0, '7': 0, '12': 0}

while True:
    canal = input("Digite o número do canal (4, 5, 7, 12, ou 0 para encerrar): ")
    if canal == '0':
        break
    pessoas_assistindo = int(input("Digite o número de pessoas assistindo: "))

    if canal in audiencia_canais:
        audiencia_canais[canal] += pessoas_assistindo

total_pessoas = sum(audiencia_canais.values())

print("Número do Canal | Percentagem de Audiência")
for canal, audiencia in audiencia_canais.items():
    percentagem = (audiencia / total_pessoas) * 100
    print(f"{canal} | {percentagem:.2f}%")
