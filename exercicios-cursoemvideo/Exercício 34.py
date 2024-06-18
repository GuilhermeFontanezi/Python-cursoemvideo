sal = float(input('Informe o valor do seu salarío: R$'))

if sal >= 1250.00:
    nsal = sal + (10 * sal / 100)
else:
    nsal = sal + (15 * sal / 100)
print('Quem {}ganhava{} R${:.2f} passou a {}ganhar{} \033[31mR${:.2f}\033[m'.format('\033[32m', '\033[m', sal, '\033[32m', '\033[m', nsal))
