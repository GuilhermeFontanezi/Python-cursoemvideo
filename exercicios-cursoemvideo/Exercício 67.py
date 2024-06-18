numero = 0
contador = 1
while True:
    numero = int(input('Digite o valor da tabuada: '))
    if numero < 0:
        break
    print('-'*25)
    for c in range(1, 11):
        resultado = numero * contador
        print(f'{numero} x {contador} = {resultado}')
        contador = contador + 1
        if contador == 11:
            contador = 0
print('MINHA TABUADA ENCERRADA, CAMBIO DESLIGO')
