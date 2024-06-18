s = 0
print('''Escolha oque você quer rever no comando \033[31mfor\033[m?
[ 1 ] contar de 1 até 10
[ 2 ] contar de 10 até 1
[ 3 ] contar de 10 até 0 contando de 2 em 2
[ 4 ] Escolha do usuario
[ 5 ] Somatorio de 5 numeros''')
sua_escolha = input('Resposta: ')

if sua_escolha == '1':
    for c in range(1, 11):
        print(c)
elif sua_escolha == '2':
    for c in range(10, 0, -1):
        print(c)
elif sua_escolha == '3':
    for c in range(0, 11, 2):
        print(c)
elif sua_escolha == '4':
    inicio = int(input('você deseja começar a conta a partir de que numero :'))
    fim = int(input('Em que número você quer parar a conta: '))
    passo = int(input('Tem algum passo de preferencia?: '))
    for c in range(inicio, fim+1, passo):
        print(c)
elif sua_escolha == '5':  # para conseguir fazer esse somatório eu precisei declarar a variavel (s = 0) no começo do codigo
    for c in range(1, 6):
        numero = int(input('Digite 5 numeros para somar: '))
        s += numero  # esse += serve como se fosse um (s = s + numero)
    print('a soma entre os numeros foi de: ', s)
else:
    print('Comando invalido...')
    print('tente novamente')
