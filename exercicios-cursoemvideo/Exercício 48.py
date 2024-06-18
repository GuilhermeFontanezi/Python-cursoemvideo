soma = 0
contador = 0
print('{}Soma dos numeros impares divisiveis por 3 de 1 a 500{}'.format('\033[33m', '\033[m'))
for c in range(0, 500):
    if c % 2 == 1 and c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print('a soma ficou dos numeros impares divisiveis por 3 de 0 a 500 ficou: {}'.format(soma))
print('a soma ficou com um total de {} numeros somados'.format(contador))
