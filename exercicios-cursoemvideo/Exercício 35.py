cores = {'limpa': '\033[m', 'azul': '\033[34m', 'vermelho': '\033[31m', 'amarelo': '\033[33m'}
l1 = float(input('Digite o valor do primeiro {}segmento{}: '.format(cores['amarelo'], cores['limpa'])))
l2 = float(input('Digite o valor do segundo {}segmento{}: '.format(cores['amarelo'], cores['limpa'])))
l3 = float(input('Digite o valor de terceiro {}segmento{}: '.format(cores['amarelo'], cores['limpa'])))

if l1 < l2 + l3 and l2 < l3 + l2 and l3 < l2 + l1:
    print('{}Os segmentos acima podem formar um triangulo!{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}Os segumentos acima não podem transformar um triangulo!{}'.format(cores['vermelho'], cores['limpa']))
