from datetime import date
nascimento = int(input('Em que ano você nasceu: '))
idade = date.today().year - nascimento

print('sua idade: ', idade)

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação:JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
