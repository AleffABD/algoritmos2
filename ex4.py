m = []

for i in range(6):
    l = []
    for c in range(6):
        valor = int(input("Informe os valores:"))
        l.append(valor)
    m.append(l)

print('Matriz sem as trocas especificas:')
for l in m:
    print(l)

m[0],m[3] =  m[3],m[0]

for i in range(6):
    m[i][2], m[i][4] = m[i][4],m[i][2]

print('A matriz resultante com as trocas especificas :')
for l in m:
    print(l)    
