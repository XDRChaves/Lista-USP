soma_positivos = 0
soma_negativos = 0

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    if numero == 0:
        break
    if numero > 0:
        soma_positivos += numero
    else:
        soma_negativos += numero

soma_total = soma_positivos + soma_negativos

print(f"Soma dos números positivos: {soma_positivos}")
print(f"Soma dos números negativos: {soma_negativos}")
print(f"Soma das duas somas parciais: {soma_total}")
