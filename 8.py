faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for i in range(15):
    idade = int(input("Idade: "))
    if idade <= 15:
        faixa1 += 1
    if 16 <= idade <= 30:
        faixa2 += 1
    if 31 <= idade <= 54:
        faixa3 += 1
    if 46 <= idade <= 60:
        faixa4 += 1
    if idade > 61:
        faixa5 += 1

total = 15
parte1 = faixa1
parte5 = faixa5

porcentagem1 = (parte1/total) * 100
porcentagem5 = (parte5/total) * 100

print(f"{faixa1} pessoa(s) têm até 15 anos")
print(f"{faixa2} pessoa(s) têm de 16 a 30 anos")
print(f"{faixa3} pessoa(s) têm de 31 a 45 anos")
print(f"{faixa4} pessoa(s) têm de 46 a 60 anos")
print(f"{faixa5} pessoa(s) têm acima de 61 anos")

print(f"Porcentagem de pessoas na 1ª e na 5ª faixa etária será respectivamente:{porcentagem1}% e {porcentagem5}%")
