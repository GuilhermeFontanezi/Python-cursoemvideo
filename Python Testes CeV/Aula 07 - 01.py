n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1-n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n2 ** n2
mo = n1 % n2
print(' A soma vale {} \n A subtração vale {} \n'.format(s, sub), end=' ')
print('A divisão vale {:.3f} \n A Multiplicação vale {} \n'.format(d, m), end=' ')
print('A divisão inteira vale {} \n A potência vale {}\n O módulo vale {} \n '.format(di,e, mo))
