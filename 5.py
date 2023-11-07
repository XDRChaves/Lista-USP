for i in range(15):
    n = input("Nome do cliente: ")
    comp = float(input("Valor das compras no ano passado: "))
    if comp < 1000:
        bonus = 0.10 * comp
    else:
        bonus = 0.15 * comp
    print(f"{n} tem direito a um bônus de R${bonus:.2f}")