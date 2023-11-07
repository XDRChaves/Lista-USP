idade_media_grupo = 0
idade_media_mulheres = 0
idade_media_homens = 0
mulheres = 0
homens = 0

for _ in range(7):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M para Masculino, F para Feminino): ")
    
    idade_media_grupo += idade
    if sexo == 'F':
        idade_media_mulheres += idade
        mulheres += 1
    else:
        idade_media_homens += idade
        homens += 1

idade_media_grupo /= 7
if mulheres > 0:
    idade_media_mulheres /= mulheres
if homens > 0:
    idade_media_homens /= homens

print(f"Idade média do grupo: {idade_media_grupo:.2f}")
print(f"Idade média das mulheres: {idade_media_mulheres:.2f}")
print(f"Idade média dos homens: {idade_media_homens:.2f}")
