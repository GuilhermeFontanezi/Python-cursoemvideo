sal = float(input('Digite o seu Salário atual: R$'))
aum = sal + (sal * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber RS{:.2f}'.format(sal, aum))
