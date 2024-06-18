print('SOMA DOS NUMEROS PARES')
print('-'*15)
contador = 0
soma = 0
for c in range(1, 7):
    numero = int(input('Digite {}º valor: '.format(c)))
    if numero % 2 == 0:
        contador = contador + 1
        soma = soma + numero
print('Foi digitado o total de {} numeros pares, a soma entre eles ficaram {}'.format(contador, soma))
