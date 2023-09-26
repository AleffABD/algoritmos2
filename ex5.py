v = []
m= []
r = []

for i in range(3):
    valor = int(input('Digite o valor para o vetor: '))
    v.append(valor)
print(f'O valor do vetor é:{v}')


for i in range(3):
    l = []
    for c in range(3):
        valor = int(input('informe os valores para a matriz: '))
        l.append(valor)
    m.append(l)
print(f'A matriz normal é:{m}')        


for i in range(3):
    r.append([0, 0, 0])

for i in range(3):
    for c in range(3):
        r[i][c] = v[i] * m[c][i]


print('A matriz resultado é:')
print(r)