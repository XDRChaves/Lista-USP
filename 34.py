candidatos = [0, 0, 0, 0]  # Inicializa a lista de votos para cada candidato
votos_nulos = 0
votos_em_branco = 0
total_votos = 0

while True:
    codigo_voto = int(input("Digite o código do voto (ou 0 para encerrar): "))
    if codigo_voto == 0:
        break
    elif codigo_voto >= 1 and codigo_voto <= 4:
        candidatos[codigo_voto - 1] += 1
    elif codigo_voto == 5:
        votos_nulos += 1
    elif codigo_voto == 6:
        votos_em_branco += 1
    else:
        print("Código de voto inválido. Por favor, digite 1 a 6 para votar ou 0 para encerrar.")

    total_votos += 1

percentagem_votos_nulos = (votos_nulos / total_votos) * 100
percentagem_votos_em_branco = (votos_em_branco / total_votos) * 100

print("Total de votos para cada candidato:")
for i, votos in enumerate(candidatos, 1):
    print(f"Candidato {i}: {votos} votos")

print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_em_branco}")
print(f"Percentagem de votos nulos sobre o total de votos: {percentagem_votos_nulos:.2f}%")
print(f"Percentagem de votos em branco sobre o total de votos: {percentagem_votos_em_branco:.2f}%")
