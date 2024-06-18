print('TABUADA')
print('-'*20)

numero = int(input('Escolha um numero para a tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(numero, c, numero * c))
