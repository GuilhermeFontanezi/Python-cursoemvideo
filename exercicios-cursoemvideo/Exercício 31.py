viagem = float(input('Quantos km vai ter sua viagem: Km '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45

print('O valor da sua passagem vai ser de {}R${}{}'.format('\033[32m', preco, '\033[m'))
