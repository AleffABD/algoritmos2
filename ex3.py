lista = []
somaimpar = 0
impar = 0
par = 0


for i in range(100):
    valor = int(input('Digite valores: '))
    lista.append(valor)
    if valor%2 == 0:
        par+=1
    else:
        somaimpar+=valor
        impar+=1


mediaimpares = somaimpar/impar

print(f'A quantidade de valores pares armazenados na lista é {par}')
print(f'A média dos valores impares armazenados na lista é {mediaimpares}')
