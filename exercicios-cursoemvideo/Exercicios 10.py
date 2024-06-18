r = float(input('quantos reais vc tem: R$'))
d = r / 4.97
e = r / 5.36
print('com R${:.2f} você pode comprar US${:.2f} dolares'.format(r, d))
print('com R${:.2f} você pode comprar €{:.2f} Euros'.format(r, e))
