import numpy as np

funcao = int(input('\n\tMetodo da Falsa Posição\n1 - Exemplo 18: e^-x^2 - cos(x)\n2 - Exemplo 19: x^3 - x - 1\n3 - Exemplo 20: 4sen(x) - e^x\n4 - Exemplo 21: x.log(x) - 1\n\nInforme uma opção: '))

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
    a=2
    b=3
    tolerancia= 1e-7


iteracoes_max = 30


#iterações para calculo da raiz
for i in range (iteracoes_max):
    p=(a*f(b) - b*f(a))/(f(b)-f(a))
    if (abs(f(p))<tolerancia) or (abs(b-a)<tolerancia):

        print('\n- Resultado aproximado: ', p)

        print('- Quantidade de iterações realizadas: ', i+1)

        print('- Valor da função quando aplicado o x encontrado: ', f(p))

        break
    elif np.sign(f(a)) == np.sign(f(p)):
        a = p
    else:
        b = p
if i==iteracoes_max-1:
    print(f'O método chegou ao maximo de iterações ({iteracoes_max})! Resultado obtido: ', p)