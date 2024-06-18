n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2

if m < 5:
    print('{}REPROVADO{}'.format('\033[31m', '\033[m'))
elif 5 >= m < 7:
    print('{}RECUPERAÇÃO{}'.format('\033[33m', '\033[m'))
elif m >= 7:
    print('{}Aprovado!'.format('\033[32m'))
