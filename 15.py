contagem = 0
for i in range(10):
    numero = int(input("15. Digite um número: "))
    if 30 <= numero <= 90:
        contagem += 1

print(f"Quantidade de números entre 30 e 90: {contagem}")
