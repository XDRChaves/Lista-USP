numeros = []
inferiores_35 = 0
positivos = []
entre_50_100 = 0
menores_50 = 0
entre_10_20 = 0

while True:
    numero = float(input("Digite um número (ou um valor negativo para encerrar): "))
    if numero < 0:
        break
    numeros.append(numero)
    
    if numero < 35:
        inferiores_35 += 1
    if numero > 0:
        positivos.append(numero)
    if 50 <= numero <= 100:
        entre_50_100 += 1
    if numero < 50:
        menores_50 += 1
        if 10 <= numero <= 20:
            entre_10_20 += 1

media_positivos = sum(positivos) / len(positivos)
percentagem_entre_50_100 = (entre_50_100 / len(numeros)) * 100
percentagem_entre_10_20 = (entre_10_20 / menores_50) * 100

print(f"Quantidade de números inferiores a 35: {inferiores_35}")
print(f"Média dos números positivos: {media_positivos:.2f}")
print(f"Percentagem de números entre 50 e 100 entre todos os números digitados: {percentagem_entre_50_100:.2f}%")
print(f"Percentagem de números entre 10 e 20 entre os números menores que 50: {percentagem_entre_10_20:.2f}%")
