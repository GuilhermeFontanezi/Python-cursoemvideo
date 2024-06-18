import random
print('-' * 25)
print('        JOKENPÔ       ')
print('-' * 25)

cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'sublinhado': '\033[7m'}

escolha = input('Escolha entre (\033[31mPEDRA/PAPEL/TESOURA\033[m): ').strip().lower()
jokenpo = ['pedra', 'papel', 'tesoura']
comp = random.choice(jokenpo)

if comp == 'papel' and escolha == 'papel':
    print('empate')
elif comp == 'papel' and escolha == 'tesoura':
    print('{}Você venceu!{} o computador escolheu papel'.format(cores['verde'], cores['limpa']))
elif comp == 'papel' and escolha == 'pedra':
    print('{}Você perdeu!{} o computador escolheu papel'.format(cores['vermelho'], cores['limpa']))
elif comp == 'pedra' and escolha == 'pedra':
    print('empate')
elif comp == 'pedra' and escolha == 'papel':
    print('{}Você venceu!{} o computador escolheu pedra'.format(cores['verde'], cores['limpa']))
elif comp == 'pedra' and escolha == 'tesoura':
    print('{}Você perdeu!{} o computador escolheu pedra'.format(cores['vermelho'], cores['limpa']))
elif comp == 'tesoura' and escolha == 'tesoura':
    print('empate')
elif comp == 'tesoura' and escolha == 'pedra':
    print('{}Você venceu!{} o computador escolheu tesoura'.format(cores['verde'], cores['limpa']))
elif comp == 'tesoura' and escolha == 'papel':
    print('{}Você perdeu!{} o computador escolheu tesoura'.format(cores['vermelho'], cores['limpa']))
#  futuramente eu quero melhorar isso!
