# Segunda Avaliação de Cálculo Numérico

# Aluno: Luís Guilherme Barbosa Custódio
# R.A.: 201905500

# Q3: Programar o código da fatoração de Cholesky e utilizá-lo para resolver o Exercício 33a do capítulo 3 do livro texto.

import numpy as np
from scipy.sparse import diags
from numpy.linalg import cholesky # p/ comparar com os resultados obtidos

# A=L*L^T.

def Cholesky(A):
    A = np.array(A, float)
    L = np.zeros_like(A)
    n, _ = np.shape(A)

    for i in range(n):
        L[i, i] = np.sqrt(A[i, i] - L[i, i] ** 2)
        sum = L[i, i - 1] * L[i - 1, i - 1] + L[i, i] * L[i - 1, i]
    return L

# Ax=B para retornar a solução x

def solucao(L, U, b):
    L = np.array(L, float)
    U = np.array(U, float)
    b = np.array(b, float)

    n, _ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # Realiza a subst. direta
    for i in range(n):
        sumj = 0
        for j in range(i):
            sumj += L[i, j] * y[j]
        y[i] = (b[i] - sumj) / L[i, i]

    # Realiza a subst. de baixo p/ cima
    for i in range(n - 1, -1, -1):
        sumj = 0
        for j in range(i + 1, n):
            sumj += U[i, j] * x[j]
        x[i] = (y[i] - sumj) / U[i, i]
    return x


a = [1 + i for i in range(2, 501)]
b = [1000 + i for i in range(1, 501)]
c = [1 + i for i in range(2, 501)]
deslocamento = [-1, 0, 1]
matriz = np.array([a, b, c], dtype=object)
A = diags(matriz, deslocamento).toarray() # diags recurso do scipy
B = [1 + i for i in range(1, 501)]
l = Cholesky(A)
U = np.transpose(l)
x = solucao(l, U, B)

A = ([[16,4,8,4], [4,10,8,4], [8,8,12,10], [4,4,10,12]])
B = ([[32],[26],[38],[30]])
L = cholesky(A)
U = np.transpose(L)
x = solucao(L, U, B)
print("Solução: ", x)