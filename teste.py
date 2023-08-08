import numpy as np 

n = 10  

vetor = np.zeros(n)

for i in range(n):
    vetor[i]=float(input(f'Informe um valor para V[{i}]'))
    print(vetor)


