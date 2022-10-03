import numpy as np

funcao = int(input('\n\tMetodo da Bissecção\n1 - Exemplo 18: e^-x^2 - cos(x)\n2 - Exemplo 19: x^3 - x - 1\n3 - Exemplo 20: 4sen(x) - e^x\n4 - Exemplo 21: x.log(x) - 1\n\nInforme uma opção: '))

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


if f(a)*f(b)>0:
    print("A função tem o mesmo sinal nos pontos a e b")
else:
    for i in range(iteracoes_max):
        p = (a+b)/2
        ne = (b-a)/2
        if f(p)==0 or ne < tolerancia:
            break
        else:
            if np.sign(f(a)) == np.sign(f(p)):
                a = p
            else:
                b = p

print('\n- Resultado aproximado: ', p)

print('- Quantidade de iterações realizadas: ',i+1)

print('- Valor da função quando aplicado o x encontrado: ', f(p))