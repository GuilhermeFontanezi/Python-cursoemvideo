import random
no1 = input('Digite seu nome para o sorteio (1/4):')
no2 = input('Digite seu nome para o sorteio (2/4):')
no3 = input('Digite seu nome para o sorteio (3/4):')
no4 = input('Digite seu nome para o sorteio (4/4):')
lista = [no1, no2, no3, no4]
escolhido = random.choice(lista)
print('o escolhido para apagar o quadro foi {}'.format(escolhido))
