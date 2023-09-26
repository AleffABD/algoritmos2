l = []
r = []


for i in range(5):
    valor = int(input("Digite alguns valores: "))
    l.append(valor)

for valor in l[::-1]:
    r.append(-valor)

print(f'O resultado da lista invertida é {r}')
