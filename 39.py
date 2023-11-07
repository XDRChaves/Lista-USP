total_investido = 0
total_juros_pagos = 0

while True:
    codigo_cliente = int(input("Digite o código do cliente (ou código menor ou igual a 0 para encerrar): "))
    
    if codigo_cliente <= 0:
        break
    
    tipo_conta = int(input("Digite o tipo da conta (1 - Poupança, 2 - Poupança Plus, 3 - Fundos de Renda Fixa): "))
    valor_investido = float(input("Digite o valor investido: "))
    
    if tipo_conta == 1:
        rendimento_mensal = valor_investido * 0.015
    elif tipo_conta == 2:
        rendimento_mensal = valor_investido * 0.02
    elif tipo_conta == 3:
        rendimento_mensal = valor_investido * 0.04
    else:
        print("Tipo de conta inválido. Por favor, escolha 1, 2 ou 3.")
        continue
    
    total_investido += valor_investido
    total_juros_pagos += rendimento_mensal
    
    print(f"Rendimento mensal: R${rendimento_mensal:.2f}")
    
print(f"Total investido: R${total_investido:.2f}")
print(f"Total de juros pagos: R${total_juros_pagos:.2f}")
