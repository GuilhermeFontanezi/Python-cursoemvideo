import random
n1 = input('Digite seu nome para sortear qual vai ser a ordem de apresentação: ')
n2 = input('Digite seu nome para sortear qual vai ser a ordem de apresentação: ')
n3 = input('Digite seu nome para sortear qual vai ser a ordem de apresentação: ')
n4 = input('Digite seu nome para sortear qual vai ser a ordem de apresentação: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A sequência de apresentaçoes será a seguinte: {}'.format(lista))
