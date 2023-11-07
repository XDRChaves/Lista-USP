vista = 0
prazo = 0

for i in range(15):
    codigo = input("Código (V para à vista, P para prazo): ")
    valor = float(input("Valor da transação: "))
    
    if codigo == 'V':
        vista += valor
    elif codigo == 'P':
        prazo += valor

total = vista + prazo
primeira_prestacao = prazo / 3

print(f"Valor total das compras à vista: R${vista:.2f}")
print(f"Valor total das compras a prazo: R${prazo:.2f}")
print(f"Valor total das compras efetuadas: R${total:.2f}")
print(f"Valor da primeira prestação das compras a prazo: R${primeira_prestacao:.2f}")
