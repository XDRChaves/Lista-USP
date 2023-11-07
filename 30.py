codigos = []
precos_custo = []
precos_novos = []
total_precos_custo = 0
total_precos_novos = 0

while True:
    codigo = int(input("Digite o código do produto (ou um valor negativo para encerrar): "))
    if codigo < 0:
        break
    preco_custo = float(input("Digite o preço de custo do produto: "))
    
    preco_novo = preco_custo * 1.2
    codigos.append(codigo)
    precos_custo.append(preco_custo)
    precos_novos.append(preco_novo)
    total_precos_custo += preco_custo
    total_precos_novos += preco_novo

for i in range(len(codigos)):
    print(f"Código do produto: {codigos[i]}, Novo preço: R${precos_novos[i]:.2f}")

media_precos_custo = total_precos_custo / len(codigos)
media_precos_novos = total_precos_novos / len(codigos)

print(f"Média dos preços de custo: R${media_precos_custo:.2f}")
print(f"Média dos novos preços: R${media_precos_novos:.2f}")
