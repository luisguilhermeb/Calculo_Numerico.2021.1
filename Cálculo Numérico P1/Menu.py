Menu = input('\n1 - Bissecção\n2 - Falsa Posição\n3 - Ponto Fixo\n4 - Newton\n5 - Secante\n\nInforme uma opção: ')

if Menu == '1':
    import Bissecção
elif Menu == '2':
    import FalsaPosição
elif Menu == '3':
    import MPF
elif Menu == '4':
    import Newton
elif Menu == '5':
    import Secante
else:
    print ("Valor invalido")