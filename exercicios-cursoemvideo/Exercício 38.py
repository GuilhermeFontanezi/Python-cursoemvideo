num = int(input('{}Digite o primeiro número: '.format('\033[33m')))
num2 = int(input('Digite o segundo número:{} '.format('\033[m')))

if num > num2:
    print('O {}primeiro{} numero é maior!'.format('\033[31m', '\033[m'))
elif num2 > num:
    print('O {}segundo{} numero é maior!'.format('\033[34m', '\033[m'))
elif num == num2:
    print('{}Os dois numeros são iguais!'.format('\033[33m'))
