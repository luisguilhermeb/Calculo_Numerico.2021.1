import numpy as np

funcao = int(input('\n\tMetodo de Newton\n1 - Exemplo 18: e^-x^2 - cos(x)\n2 - Exemplo 19: x^3 - x - 1\n3 - Exemplo 20: 4sen(x) - e^x\n4 - Exemplo 21: x.log(x) - 1\n\nInforme uma opção: '))

#define a função escolhida
def f(x):
    if funcao == 1:
        return np.exp(-x**2)-np.cos(x)
    elif funcao == 2:
        return x**3 - x -1
    elif funcao == 3:
        return 4*np.sin(x) - np.exp(x)
    elif funcao == 4:
        return x*np.log10(x) - 1
    else:
        print('Opção Invalida!')
        sys.exit()


#define a derivada da função escolhida
def df(x):
    if funcao == 1:
        return -2*np.exp(-x**2) * x + np.sin(x)
    elif funcao == 2:
        return 3*(x**2)-1
    elif funcao == 3:
        return 4*np.cos(x) - np.exp(x)
    elif funcao == 4:
        return np.log10(x)+(1/np.log(10))


#define os valores dos pontos A, B e Tolerancia para a função escolhida
if funcao == 1:
    a=1
    b=2
    aproxInicial= 1.5
    tolerancia= 1e-5
elif funcao == 2:
    a=1
    b=2
    aproxInicial= 0
    tolerancia= 1e-6
elif funcao == 3:
    a=0
    b=1
    aproxInicial = 0.5
    tolerancia= 1e-5
elif funcao == 4:
    a=2
    b=3
    aproxInicial = 2.5
    tolerancia= 1e-7


iteracoes_max = 30


for i in range(iteracoes_max):
    p= aproxInicial - (f(aproxInicial)/df(aproxInicial))
    if abs(p-aproxInicial)<tolerancia:
        print('\n- Resultado aproximado: ', p)
        print('- Quantidade de iterações realizadas: ', i)
        print('- Valor da função quando aplicado o x encontrado: ', f(p))
        break
    aproxInicial=p
if i==iteracoes_max-1:
    print("O número máximo de iterações foi atingido, obtendo a solução aproximada de : ", p)