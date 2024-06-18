import random
from time import sleep
sorteador = random.randint(1, 10)
chute = int
print('Estou pensando em um numero...')
sleep(1)
print('Duvido você acertar hehe')
while chute != sorteador:
    chute = int(input('Qual é o seu chute?: '))
    print('------------------')
    if chute > sorteador:
        print('você errou!')
        print('eu pensei em um numero menor')
    elif chute < sorteador:
        print('você errou!')
        print('eu pensei em um numero maior')
print('parabens, você me venceu!')
