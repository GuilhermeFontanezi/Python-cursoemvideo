import random
from time import sleep
sorteador = random.randint(0, 5)    # Faz o computador sortear
print('-=-' * 25)
print('hmmmmm Estou pensando em um numero de 1 a 5, duvido vc acertar!')
print('-=-' * 25)
chute = int(input('Em que numero eu pensei? '))     # Jogador tenta advinhar
print('Processando...')
sleep(2)
if sorteador == chute:
    print('Parabens! Voce me vencer!')
else:
    print('O computador venceu! O numero escolhido era {}'.format(sorteador))
