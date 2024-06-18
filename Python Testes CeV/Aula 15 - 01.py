numero = 0
soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma = soma + numero
print(f'A soma vale {soma}')
# print('A soma vale {}'.format(soma))