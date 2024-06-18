menu = str
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
while menu != '5':
    print('{}----------MENU----------{}'.format('\033[33m', '\033[m'))
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Qual é o maior
[ 4 ] Escolher outros numeros
[ 5 ] Sair''')
    print('--------------------------')
    menu = input('Qual sera sua escolha: ')
    if menu == '1':
        soma = numero1 + numero2
        print('a soma entre {} + {} é {}'.format(numero1, numero2, soma))
    elif menu == '2':
        vezes = numero1 * numero2
        print('A multiplicação entre {} x {} é {}'.format(numero1, numero2, vezes))
    elif menu == '3':
        if numero1 > numero2:
            print('O {} é maior'.format(numero1))
        else:
            print('O {} é maior'.format(numero2))
    elif menu == '4':
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção invalida')
    print('O programa nao irá fechar até você digitar 5')
    print('-----------------------------------------------------------')
print('Obrigado por usar o programa')
