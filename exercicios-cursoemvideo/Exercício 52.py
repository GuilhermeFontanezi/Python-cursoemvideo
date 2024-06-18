numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO {} foi divisível {} vezes'.format(numero, total))

if total == 2:
    print('Por isso ele é primo')
elif total > 2:
    print('Por isso ele não é primo')
