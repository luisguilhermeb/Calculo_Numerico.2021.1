# Segunda Avaliação de Cálculo Numérico

# Aluno: Luís Guilherme Barbosa Custódio
# R.A.: 201905500

# Q1: Programar o código de Eliminação de Gauss e utilizá-lo para resolver o Exercício 5 do capítulo 3 do livro texto.

def MetodoGauss(m):
    # Eliminação por colunas
    print("A: ", m)
    for coluna in range(len(m[0])):
        for fila in range(coluna + 1, len(m)):
            r = [(posicaoFila * (-(m[fila][coluna] / m[coluna][coluna]))) for posicaoFila in m[coluna]]
            m[fila] = [sum(pair) for pair in zip(m[fila], r)]
    # Resolver por substituição
    ans = []
    m.reverse()
    for sol in range(len(m)):
        if sol == 0:
            ans.append(m[sol][-1] / m[sol][-2])
        else:
            pos = 0
            # Substituir em todos os coeficientes conhecidos
            for x in range(sol):
                pos += (ans[x] * m[sol][-2 - x])
            # A equação está agora reduzida a ax + b = c
            # Resolve-se com (c - b) / a
            ans.append((m[sol][-1] - pos) / m[sol][-sol - 2])
    ans.reverse()
    return ans

print("Resultado: ", MetodoGauss([[2,2,1,1,7],[1,-1,2,-1,1],[3,2,-3,-2,4],[4,3,2,1,12]]))