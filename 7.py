contagem = 0
for i in range(10):
    idade = int(input("Idade: "))
    if idade >= 18:
        contagem += 1

print(f"{contagem} pessoas têm 18 anos ou mais.")