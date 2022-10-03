# Segunda Avaliação de Cálculo Numérico

# Aluno: Luís Guilherme Barbosa Custódio
# R.A.: 201905500

# Q2: Programar o código da decomposição LU e utilizá-lo para resolver o Exercício 11d do capítulo 3 do livro texto.

import numpy as np

    # realiza a decomposição da matriz em LU
def PLU(A):
    # obtem o numero de linhas do sistema
    n = A.shape[0]
    # aloca espaço para P, L, e U
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)
    # percorre as n linhas
    for i in range(n):
        for k in range(i, n):
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k+1]] = U[[k+1, k]]
            P[[k, k+1]] = P[[k+1, k]]
        fator = U[i+1:, i] / U[i, i]
        L[i+1:, i] = fator
        U[i+1:] -= fator[:, np.newaxis] * U[i]
    return P, L, U

def substituicaoInferior(U, y):
    # obtem o numero de linhas do sistema
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double);
    x[-1] = y[-1] / U[-1, -1]
    # solução de baixo para cima
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    return x

def substituicaoDireta(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double);
    # inicializa a substituição direta pela primeira linha
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
    return y

    # busca a invera da matriz A
def PLU_inversa(A):
    n = A.shape[0]
    b = np.eye(n)
    AInversa = np.zeros((n, n))
    P, L, U = PLU(A)
    for i in range(n):
        y = substituicaoDireta(L, np.dot(P, b[i, :]))
        AInversa[i, :] = substituicaoInferior(U, y)
    return AInversa

A = np.array([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]], dtype='float')
P, L, U = PLU(A)
print("Matriz inversa 11. D): \n\n", PLU_inversa(A))