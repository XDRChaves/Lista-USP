salarios = []
idades = []
maior_idade = -1
menor_idade = 999
mulheres_ate_200 = 0
menor_salario = float('inf')
idade_menor_salario = 0
sexo_menor_salario = ''

while True:
    idade = int(input("Digite a idade (ou um valor negativo para encerrar): "))
    if idade < 0:
        break
    sexo = input("Digite o sexo (M/F): ")
    salario = float(input("Digite o salário: "))
    
    idades.append(idade)
    salarios.append(salario)
    
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if sexo == 'F' and salario <= 200:
        mulheres_ate_200 += 1
    if salario < menor_salario:
        menor_salario = salario
        idade_menor_salario = idade
        sexo_menor_salario = sexo

media_salarios = sum(salarios) / len(salarios)

print(f"Média dos salários do grupo: R${media_salarios:.2f}")
print(f"Maior idade do grupo: {maior_idade}")
print(f"Menor idade do grupo: {menor_idade}")
print(f"Quantidade de mulheres com salário até R$ 200,00: {mulheres_ate_200}")
print(f"Idade e sexo da pessoa com o menor salário: Idade {idade_menor_salario}, Sexo {sexo_menor_salario}")
