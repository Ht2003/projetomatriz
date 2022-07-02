import numpy as np
n = int(input('tamanho matriz:' ))

x = int(input('X = '))
numero = 0
linha = [0] * n
linha1 = [0] * n
matrizA = [linha] * n
matrizB = [linha1] * n

print(matrizA)

for i in range(n):  # pegando os algoritmos para matriz A
    linha = []
    for j in range(n):
        numero = int(input("Digite o numero que ficara armazenado na Matriz A {},{} : ".format(i, j)))
        linha.append(numero)
    matrizA[i] = linha

print()

print('Digite o numero que ficara armazenado na Matriz B:')
for k in range(n):  # pegando os Algoritmos para a B
    linha1 = []
    for l in range(n):
        numero = int(input("Matriz B {},{} : ".format(k, l)))
        linha1.append(numero)
    matrizB[k] = linha1

print('MATRIZ A')
for i in range(n):  # Exibir a Matriz A
    for j in range(n):
        print(f'{matrizA[i][j]:^5}', end=' ')
    print()
print('-='*30)
print('MATRIZ B:')
for k in range(n):  # Exibindo a matriz B
    for l in range(n):
        print(f'{matrizB[k][l]:^5}', end=' ')
    print()

print('MATRIZ AT:')
aT = []
for m in range(n):
    for o in range(n):
        aT.append(matrizA[o][m])
c = 0
for i in range(n):
    for j in range(n):
        print(f'{aT[c]:^5}', end=' ')
        c += 1
    print()

print('MATRIZ *AT:')
aT_vezes = []
for m in range(n):
    atx = [0] * n
    aT_vezes.append(atx)
    for o in range(n):
        aT_vezes[m][o] = (matrizA[o][m])
c = 0
for i in range(n):
    for j in range(n):
        print(f'{np.dot(aT_vezes, x)[i][j]:^5}', end=' ')
        aT_vezes[i][j] = np.dot(aT_vezes, x)[i][j]
        c += 1
    print()

print('MATRIZ B<TS>')
BsT = []
for i in range(n):
    BsTlinha = [0] * n
    BsT.append(BsTlinha)
for x in range(0, n):
    for y in range(x, n):
        BsT[x][y] = matrizB[x][y]


for x in range(0, n):
    for y in range(0, n):
        print(f'{BsT[x][y]:^5}', end=' ')
    print()


print('MATRIZ C')
c = 0
matrizC = []
for m in range(n):
    for o in range(n):
        matrizC.append(matrizA[o][m])
c = 0
for i in range(n):
    for j in range(n):
        print(f'{aT_vezes[i][j] + BsT[i][j]:^5}', end=' ')
        c += 1
    print()

