n = int(input('Digite um valor: '))
if n % 2 == 0:
    print('O número {} é {}par{}'.format(n, '\033[35m', '\033[m'))
else:
    print('O número {} é {}impar{}'.format(n, '\033[31m', '\033[m'))
