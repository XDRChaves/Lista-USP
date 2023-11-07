grupos = []
print("Atribua valores para as letras abaixo:")
for x in range(5):
    grupo = [
             int(input("A: ")),
             int(input("B: ")),
             int(input("C: ")),
             int(input("D: "))
    ]
    grupos.append(grupo)

print("Ordem lida:")
for grupo in grupos:
    print(grupo)

print("Ordem crescente:")
grupos.sort()
for grupo in grupos:
    print(grupo)

print("Ordem decrescente:")
grupos.sort(reverse=True)
for grupo in grupos:
    print(grupo)
