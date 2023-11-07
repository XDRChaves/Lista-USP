while True:
    print("Menu de opções:")
    print("1. Novo salário")
    print("2. Férias")
    print("3. Décimo terceiro")
    print("4. Sair")
    
    opcao = input("Digite a opção desejada (1/2/3/4): ")
    
    if opcao == '4':
        break
    if opcao not in ['1', '2', '3']:
        print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")
        continue
    
    salario = float(input("Digite o salário do funcionário: "))
    
    if opcao == '1':
        if salario <= 350:
            novo_salario = salario * 1.15
        elif salario <= 600:
            novo_salario = salario * 1.1
        else:
            novo_salario = salario
        print(f"Novo salário: {novo_salario:.2f}")
    elif opcao == '2':
        valor_ferias = salario + (salario * 0.16)
        print(f"Valor das férias: {valor_ferias:.2f}")
    elif opcao == '3':
        meses_trabalho = int(input("Digite o número de meses de trabalho na empresa (máximo 12): "))
        if meses_trabalho > 12:
            meses_trabalho = 12
        decimo_terceiro = (salario * meses_trabalho) / 12
        print(f"Valor do décimo terceiro: {decimo_terceiro:.2f}")
