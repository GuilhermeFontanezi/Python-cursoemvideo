numero = int(input('Digite um numero: '))
c = numero
fatorial = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c = c - 1
print('{}'.format(fatorial))
