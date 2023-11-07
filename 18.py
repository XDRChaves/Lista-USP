preco_carro = float(input("Digite o valor do carro: "))

# Desconto de 20% para compra à vista
preco_vista = preco_carro * 0.8

parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

print("Preço Final | Quantidade de Parcelas | Valor da Parcela")
for parcela in parcelas:
    acrescimo = 0
    if parcela > 12:
        acrescimo = 0.1 * (parcela - 12)
    valor_parcela = (preco_carro * (1 + acrescimo)) / parcela
    print(f"R${preco_carro:.2f} | {parcela} | R${valor_parcela:.2f}")
