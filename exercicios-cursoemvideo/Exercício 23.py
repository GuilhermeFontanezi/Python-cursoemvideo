number = int(input('Digite um numero:'))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print('Analizando o numero {} ...'.format(number))
print('unidade:{}'.format(u))
print('Dezena: {} '.format(d))
print('Centena:{}'.format(c))
print('Milhar: {}'.format(m))
