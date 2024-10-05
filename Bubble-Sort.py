vetor = [1,3,4,2,9,8,7,6,5,10]

troca = True
aux = 0

while troca:
    troca = False
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux
            troca = True

print(vetor)