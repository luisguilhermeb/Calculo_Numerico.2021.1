# Segunda Avaliação de Cálculo Numérico

# Aluno: Luís Guilherme Barbosa Custódio
# R.A.: 201905500

# Q4: Fazer um código que verifica se uma matriz é diagonal dominante, ou equivalentemente, se satisfaz o critério das linhas.
#       a) Teste o seu código na Matriz A=np.array([[-8.0,3,1],[2,-4,1],[2,3,5]]).
#       b) Teste o seu código juntamente com o código do método de Jacobi para resolver o sistema 22b).

from numpy import array, zeros, diag, diagflat, dot
import math

def criterioLinhas(A):
    coeficientes =[]
    for i in range(len(A)):
        somaCoef=0
        for j in range(len(A)):
            if i != j:
                somaCoef += math.fabs(A[i][j])
        somaCoef /= math.fabs(A[i][i])
        coeficientes.append(somaCoef)

    maiorCoef = max(coeficientes)
    if maiorCoef < 1:
        print("A matriz satisfaz o critério das linhas!")
    else:
        print("O resultado é incerto para o critério das linhas!")

def jacobi(A,b,N=25,x=None):
    # Ax=b pelo metodo de Jacobi
    if x is None:
        x = zeros(len(A[0]))
    # Obtem o vetor dos elementos diagonais da matriz
    # Elem. diagonais-A
    D = diag(A)
    R = A - diagflat(D)
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([[-8.0,3,1],[2,-4,1],[2,3,5]])

# A) Teste o seu código na Matriz A=np.array([[-8.0,3,1],[2,-4,1],[2,3,5]]).
print("A) Verif. A:")
criterioLinhas(A)


#b) Teste o seu código juntamente com o código do método de Jacobi para resolver o sistema 22b).

#22 b1)
A1 = array([[10.0,1.0,1.0],[1.0,10.0,1.0],[1.0,1.0,10.0]])
b1 = array([12,12,12])
guess1 = array([1.0,1.0,1.0])

print ("\n\nB) Solução 22. B1) : ")

criterioLinhas(A1)
sol1= jacobi(A1,b1,N=25,x=guess1)

print ("A:\n", A1)
#pprint(A)

print ("B:", b1)
#pprint(b)

print ("X:", sol1)
#pprint(sol)



#22 b2)
A2 = array([[4.0,-1.0,0.0,0.0],[-1.0,4.0,-1.0,0.0],[0.0,-1.0,4.0,-1.0],[0.0,0.0,-1.0,4.0]])
b2 = array([1.0, 1.0,1.0,1.0])
guess2 = array([1.0,1.0,1.0,1.0])

print ("\nB) Solução 22. B2) : ")

criterioLinhas(A2)
sol2= jacobi(A2,b2,N=25,x=guess2)

print ("A:\n", A2)
#pprint(A2)

print ("B:", b2)
#pprint(b2)

print ("X:", sol2)
#pprint(sol2)