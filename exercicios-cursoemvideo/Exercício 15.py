dias = int(input('Com quantos dias o carro foi alugado: '))
km = float(input('quantos km o carro foi rodado: '))
st = (60 * dias) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(st))
