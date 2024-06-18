from datetime import date
maior_idade = 0
menor_idade = 0

for c in range(1, 8):
    print('''Cadastre 7 pessoas
----------------------------------''')
    nascimento = int(input('Em que ano você nasceu: '))
    if date.today().year - nascimento >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('Entre as sete pessoas {} eram maioridade e {} são menoridade'.format(maior_idade, menor_idade))
