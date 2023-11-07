faixas_etarias = {'0-10': [], '11-20': [], '21-30': [], '31+': []}

for _ in range(15):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    
    if idade >= 0 and idade <= 10:
        faixas_etarias['0-10'].append(peso)
    elif idade >= 11 and idade <= 20:
        faixas_etarias['11-20'].append(peso)
    elif idade >= 21 and idade <= 30:
        faixas_etarias['21-30'].append(peso)
    else:
        faixas_etarias['31+'].append(peso)

for faixa, pesos in faixas_etarias.items():
    if len(pesos) > 0:
        media = sum(pesos) / len(pesos)
        print(f"Média de pesos na faixa etária {faixa}: {media:.2f}")
