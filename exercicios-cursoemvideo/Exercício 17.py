import math
cateo = float(input('qual o cumprimento do cateto oposto: '))
catea = float(input('qual é o cumprimento do cateto adjancente: '))
h1 = math.hypot(cateo, catea)
print('O valor da hipotenusa vai ser: {:.2f}'.format(h1))
