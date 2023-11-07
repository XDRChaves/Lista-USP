while True:
    print("Menu de opções:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    opcao = input("Escolha a operação desejada (1/2/3/4/5): ")
    
    if opcao == '5':
        break
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida. Por favor, escolha 1, 2, 3, 4 ou 5.")
        continue
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == '1':
        resultado = num1 + num2
        print(f"Resultado da adição: {resultado}")
    elif opcao == '2':
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    elif opcao == '3':
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao == '4':
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
