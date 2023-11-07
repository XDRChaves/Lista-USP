valores = []
while True:
    valor = int(input("Digite um valor inteiro positivo (ou 0 para encerrar): "))
    if valor == 0:
        break
    elif valor < 0:
        print("Valor negativo. Por favor, digite um valor positivo.")
        continue
    valores.append(valor)

if len(valores) > 0:
    maior = max(valores)
    menor = min(valores)
    print(f"O maior valor do conjunto é {maior}.")
    print(f"O menor valor do conjunto é {menor}.")
else:
    print("Nenhum valor positivo foi digitado.")
