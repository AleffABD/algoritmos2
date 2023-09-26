p = []
n = []


for i in range(8):
    valor = int(input("Digite 8 valores positivos ou negativos: "))
    if valor > 0:
        p.append(valor)
    if valor < 0:
        n.append(valor) 

print(f'Os valores positivos são {p}')
print(f'Os valores negativos são {n}')
