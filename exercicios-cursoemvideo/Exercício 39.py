from datetime import date
ano = int(input('digite o ano que você nasceu: '))

if date.today().year - ano < 18:
    print('{}Você ainda vai se alistar no exercito{}'.format('\033[32m', '\033[m'))
    print('Falta {} anos para vc se alistar'.format(18 - (date.today().year - ano)))
elif date.today().year - ano == 18:
    print('quem nasceu em {} tem {} anos em {}'.format(ano, date.today().year - ano, date.today().year))
    print('{}Você DEVE se alistar no exercito!{}'.format('\033[33m', '\033[m'))
elif date.today().year - ano > 18:
    print('{}Ja passou da hora de você se alistar! CORRE{}'.format('\033[31m', '\033[m'))
    print('Ja passou {} anos do momento de se alistar'.format(date.today().year - ano - 18))
