numero = int(input('Digite um numero para converter: '))
print('''[ 1 ] para converter para BINARIO
[ 2 ] para converter OCTAL
[ 3 ] para converter para HEXADECIMAL''')

sua_opcao = input('Sua opção: ')

if sua_opcao == '1':
    print('{} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif sua_opcao == '2':
    print('{} convertido para octal é {}'.format(numero, oct(numero)[2:]))
elif sua_opcao == '3':
    print('{} convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('''Opção Invalida...
    você digitou {}, é para digitar apenas as opções acima'''.format(sua_opcao))
