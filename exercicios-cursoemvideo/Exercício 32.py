from datetime import date
ano = int(input('Qual ano estamos? '))

cores = {'limpa': '\033[m', 'sublinhado': '\033[4m', 'vermelho': '\033[31m', 'verde': '\033[32m'}

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é {}{}bissexto{}'.format(ano, cores['sublinhado'], cores['verde'], cores['limpa']))
else:
    print('O ano {} não é {}{}bissexto{}'.format(ano, cores['sublinhado'], cores['vermelho'], cores['limpa']))
