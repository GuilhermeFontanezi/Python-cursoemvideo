peso = float(input('Digite seu peso em Kg:'))
altura = float(input('Digite sua altura em metros:'))
imc = peso / altura**2

print('{:.1f}'.format(imc))

if imc < 18.5:
    print('{}Abaixo do peso{}'.format('\033[34m', '\033[m'))
elif 18.5 <= imc <= 25:
    print('{}Peso ideal{}'.format('\033[32m', '\033[m'))
elif 25 <= imc < 30:
    print('{}Sobrepeso{}'.format('\033[31m', '\033[m'))
elif 30 <= imc < 40:
    print('{}{}Obesidade{}'.format('\033[36m', '\033[7m', '\033[m'))
elif peso > 40:
    print('{}{}Obesidade mórbida{}'.format('\033[7m', '\033[41m', '\033[m'))
