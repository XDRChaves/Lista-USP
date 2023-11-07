def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


n = int(input("Digite um valor inteiro para calcular o fatorial: "))
resultado = fatorial(n)
print(f"{n}! = {resultado}")
