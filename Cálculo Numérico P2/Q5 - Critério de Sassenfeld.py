# Segunda Avaliação de Cálculo Numérico

# Aluno: Luís Guilherme Barbosa Custódio
# R.A.: 201905500

# Q5: Fazer um código que verifica se a matriz satisfaz o critério de Sassenfeld.
#       a) Teste o seu código na Matriz A=np.array([[-8.0,3,1],[2,-4,1],[2,3,5]]).
#       b) Use o seu código juntamente com o código do método de Gauss-Seidel para resolver,
#          caso possível, os sistemas do Exemplo 15 do capítulo 3 do livro texto. Teste os
#          códigos na letra a) e os dois casos da letra b). Verifique que o exemplo da letra c) não
#          satisfaz os critérios da linha e/ou Sassenfeld, mas mesmo assim aplique os métodos
#          de Jacobi e Gauss-Seidel e analise se os métodos convergem.

import numpy as np

def criterioSassenfeld(A):
    coeficientes =[]
    for i in range (len(A)):
        b=0
        for j in range(len(A)):
            if (i !=j and i== 0) or i < j:
                b+=A[i][j]
            elif i!=j and i!=0:
                b+=A[i][j]*coeficientes[j]
        b /= A[i][i]
        coeficientes.append(b)
    maiorCoeficiente = max (coeficientes)
    if maiorCoeficiente <1:
        print("A matriz satisfaz o critério de Sassenfeld!")
    else:
        print("O resultado é incerto para o critério de Sassenfeld!")

def gaussSeidel(A,b,vetorSolucao, iteracoes):
    iteracao =0
    while iteracao < iteracoes:
        for i in range (len(A)):
            x=b[i]
            for j in range(len(A)):
                if i!=j:
                    x -=A[i][j]*vetorSolucao[j]
            x /= A[i][i]
            vetorSolucao[i]=x
        iteracao +=1
    print(vetorSolucao)

A1 = np.array([[-8.0,3.0,1.0],[2.0,-4.0,1.0],[2.0,3.0,5.0]])

A2 = np.array([[1.0,0.5,-1.0,1.0],[0.2,1.0,-0.2,-0.1],[-0.1,-0.2,1.0,0.2],[0.1,0.3,0.2,1.0]])
B2 = np.array([[3.0,0.0,1.0],[1.0,-1.0,0.0],[3.0,1.0,2.0]])
C2 = np.array([[1.0,1.0],[1.0,-3.0]])

#       a) Teste o seu código na Matriz A=np.array([[-8.0,3,1],[2,-4,1],[2,3,5]]).
print("A) Verif. A:\n", A1)
criterioSassenfeld(A1)


#       b) Use o seu código juntamente com o código do método de Gauss-Seidel para resolver,
#          caso possível, os sistemas do Exemplo 15 do capítulo 3 do livro texto. Teste os
#          códigos na letra a) e os dois casos da letra b). Verifique que o exemplo da letra c) não
#          satisfaz os critérios da linha e/ou Sassenfeld, mas mesmo assim aplique os métodos
#          de Jacobi e Gauss-Seidel e analise se os métodos convergem.
print("\n\nB) Exemplo 15. A) :\n", A2)
SolA2 = np.array([0.2,-2.6,1.0,-2.5])
SolInicialA2 = np.array([0.0,0.0,0.0,0.0])

print("b =", SolA2)
criterioSassenfeld(A2)
print("Solução: ")
gaussSeidel(A2, SolA2, SolInicialA2, 25)


print("\nB) Exemplo 15. B) \n", B2)
SolB2 = np.array([3.0,1.0,9.0])
SolInicialB2= np.array([0.0,0.0,0.0])

print("b =", SolB2)
criterioSassenfeld(B2)
print("Solução: ")
gaussSeidel(B2, SolB2, SolInicialB2, 25)


print("\nB) Exemplo 15. C) \n", C2)
SolC2 = np.array([3.0,-3.0])
SolInicialC2 = np.array([0.0,0.0])

print("b =", SolC2)
criterioSassenfeld(C2),
print("Solução: ")
gaussSeidel(C2, SolC2, SolInicialC2, 25)