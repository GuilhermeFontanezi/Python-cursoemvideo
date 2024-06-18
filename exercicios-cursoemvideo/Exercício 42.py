l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acimas formar um triangulo normal')
    if l1 == l2 and l2 == l3:
        print('EQUILATERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('ISÓCELES')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('ESCALENO')
else:
    print('Os segmentos acimas não formam um triangulo')
