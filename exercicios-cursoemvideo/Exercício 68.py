import random
contador = 0
print('=-'*13)
print('VAMOS JOGAR PAR OU IMPAR?')
print('-='*13)
while True:
    escolha_pc = random.randint(0, 10)
    sua_escolha = int(input('Digite um numero de 0 á 10: '))
    total = escolha_pc + sua_escolha
    par_impar = input('Par ou Impar (I/P)').strip().lower()[0]
    while par_impar not in 'PpIi':
        par_impar = input('Par ou Impar (I/P)').strip().lower()[0]
    print(f'Você jogou {sua_escolha} o computador jogou {escolha_pc} e o total deu {total}')
    if par_impar == 'p':
        if total % 2 == 0:
            print('Você ganhou!')
            contador += 1
        else:
            print('Você perdeu!')
            break
    elif par_impar == 'i':
        if total % 2 == 1:
            print('Você ganhou!')
            contador += 1
        else:
            print('Você perdeu!')
            break
    print('Vamo jogar novamente...')
print(f'Winstreak: {contador}')
