velocit = float(input('Qual era a velocidade do carro: km/h '))
mult = (velocit - 80) * 7
cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'sublhinhado': '\033[4m', 'amarelo': '\033[33m'}

if velocit <= 80:
    print('{}Velocidade no limite!'.format(cores['verde']))
else:
    print('{}Você foi multado!{} Você excedeu o limite que é de {}80Km/h{}'.format(cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa']))
    print('{}{}Você deve pagar uma multa de R${:.2f}!{} '.format(cores['sublhinhado'], cores['vermelho'], mult, cores['limpa']))
print('{}Tenha um bom dia e diriga com segurança'.format(cores['amarelo']))
