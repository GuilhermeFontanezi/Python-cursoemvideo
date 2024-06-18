preco = float(input('Digite o valor do produto: '))
print('='*20)
print('FORMA DE PAGAMENTO:')
print('='*20)
print('A vista ({}DINHEIRO/CHEQUE{}) desconto de 10%'.format('\033[32m', '\033[m'))
print('A vista no ({}CARTÃO{}) desconto de 5%'.format('\033[32m', '\033[m'))
print('({}2x{}) no cartão'.format('\033[32m', '\033[m'))
print('({}3x{}) no cartão'.format('\033[32m', '\033[m'))
pagamento = input('Digite a forma de pagamento (a parte azul):').strip().lower()

if pagamento == 'dinheiro' or pagamento == 'cheque':
    print('Você ira pagar a vista, o valor do produto ficou R${:.2f}'.format(preco - (10 * preco / 100)))
elif pagamento == 'cartão':
    print('Você ira pagar a vista no cartao, o valor do produto ficou R${:.2f}'.format(preco - (5 * preco / 100)))
elif pagamento == '2x':
    print('Você ira pagar em duas vezes, cada parcela ficou R${:.2f}'.format(preco / 2))
elif pagamento == '3x':
    print('Você ira pagar em três vezes com 20% de juros, cada parcela ficou R${:.2f}'.format((20 * preco / 100 + preco) / 2))
