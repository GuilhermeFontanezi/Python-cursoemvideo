print('Boas vindas')
pergunta = ''
preco = 0
pedido = ''
while pergunta != 'n':
    sabor = input('Entre com o valor desejado (CP/AC): ').lower()
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').lower()
    if sabor not in 'cp' 'ac':
        print('O sabor está invalido. Tente novamente')
        sabor = input('Entre com o valor desejado (CP/AC): ').lower()
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').lower()
    if tamanho not in 'p' 'm' 'g':
        print('O tamanho está invalido. Tente novamente')
        sabor = input('Entre com o valor desejado (CP/AC): ').lower()
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').lower()
    if sabor == 'ac':
        if tamanho == 'p':
            pedido = 'açai'
            preco += 11
        elif tamanho == 'm':
            pedido = 'açai'
            preco += 16
        elif tamanho == 'g':
            pedido = 'açai'
            preco += 20
    if sabor == 'cp':
        if tamanho == 'p':
            pedido = 'cupuaçu'
            preco += 9
        elif tamanho == 'm':
            pedido = 'cupuaçu'
            preco += 14
        elif tamanho == 'g':
            pedido = 'cupuaçu'
            preco += 18
    # print(f'Você pediu um {pedido} no valor de {preco:.2f}')
    pergunta = input('Deseja mais alguma coisa? (s/n): ').lower()
print(f'O total a ser pago vai ser de {preco:.2f}')
