respostas_sim = 0
respostas_nao = 0
mulheres_sim = 0
homens_sim = 0

for _ in range(10):
    sexo = input("Digite o sexo (M para homem, F para mulher): ")
    resposta = input("Digite a resposta (S - Sim, N - Não): ")
    
    if resposta == 'S':
        respostas_sim += 1
        if sexo == 'F':
            mulheres_sim += 1
        elif sexo == 'M':
            homens_sim += 1
    elif resposta == 'N':
        respostas_nao += 1

percentagem_homens_nao = (homens_sim / (homens_sim + (10 - respostas_sim))) * 100

print(f"Número de pessoas que respondeu sim: {respostas_sim}")
print(f"Número de pessoas que respondeu não: {respostas_nao}")
print(f"Número de mulheres que respondeu sim: {mulheres_sim}")
print(f"Percentagem de homens que respondeu não entre todos os homens analisados: {percentagem_homens_nao:.2f}%")
