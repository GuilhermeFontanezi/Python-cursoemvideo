print('='*30)
print('{:^30}'.format('BANCO GUI'))
print('='*30)
valor_sacado = int(input('Quantos reais você ira sacar? R$: '))
total = valor_sacado
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f' Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
