import numpy as np

funcao = int(input('\n\tMetodo da Secante\n1 - Exemplo 18: e^-x^2 - cos(x)\n2 - Exemplo 19: x^3 - x - 1\n3 - Exemplo 20: 4sen(x) - e^x\n4 - Exemplo 21: x.log(x) - 1\n\nInforme uma opção: '))

#define a função escolhida
def f(x):
    if funcao == 1:
        return np.exp(-x**2)-np.cos(x)
    elif funcao == 2:
        return x**3 - x - 1
    elif funcao == 3:
        return 4*np.sin(x) - np.exp(x)
    elif funcao == 4:
        return x*np.log10(x) - 1
    else:
        print('Opção Invalida!')
        sys.exit()


#define os valores dos pontos A, B e Tolerancia para a função escolhida
if funcao == 1:
    a=1
    b=2
    tolerancia= 1e-4
elif funcao == 2:
    a=1
    b=2
    tolerancia= 1e-6
elif funcao == 3:
    a=0
    b=1
    tolerancia= 1e-5
elif funcao == 4:
    a=2.3
    b=2.7
    tolerancia= 1e-7


iteracoes_max = 30

inter = lambda a, b, tolerancia: 1 + int((np.log(b - a) - np.log(tolerancia)) // np.log(2))

k = inter(a, b, tolerancia)

for i in range(k):

    x = b - f(b) * (a - b) / (f(a) - f(b))

    if np.abs((x - b) / b) < tolerancia:
        break

    a = b
    b = x

print('\n- Resultado aproximado: ', x)

print('- Quantidade de iterações realizadas: ', i)

print('- Valor da função quando aplicado o x encontrado: ', f(x))