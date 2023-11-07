lucros = []
acoes_com_lucro_superior_1000 = 0
acoes_com_lucro_inferior_200 = 0
lucro_total = 0

while True:
    tipo_acao = input("Digite o tipo da ação (ou 'F' para encerrar): ")
    if tipo_acao == 'F':
        break
    preco_compra = float(input("Digite o preço de compra da ação: "))
    preco_venda = float(input("Digite o preço de venda da ação: "))
    
    lucro = preco_venda - preco_compra
    lucros.append(lucro)
    
    if lucro > 1000:
        acoes_com_lucro_superior_1000 += 1
    if lucro < 200:
        acoes_com_lucro_inferior_200 += 1
    
    lucro_total += lucro

for i, lucro in enumerate(lucros, 1):
    print(f"Ação {i}: Lucro = R${lucro:.2f}")

print(f"Quantidade de ações com lucro superior a R$ 1.000,00: {acoes_com_lucro_superior_1000}")
print(f"Quantidade de ações com lucro inferior a R$ 200,00: {acoes_com_lucro_inferior_200}")
print(f"Lucro total da empresa: R${lucro_total:.2f}")
