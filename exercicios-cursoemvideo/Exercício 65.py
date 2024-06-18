resposta = str
numero = 0
media = 0
soma = 0
maior = 0
menor = 0
contador = 0
while resposta != 'n':
    numero = int(input('Digite um valor: '))
    resposta = input('DESEJA CONTINUAR [S|N]?')
    soma = soma + numero
    contador = contador + 1
    media = soma / contador
    if numero > maior:
        maior = numero
    elif menor < numero:
        menor = numero
print('O MAIOR NUMERO DIGITADO FOI {} E O MENOR FOI {}'.format(maior, menor))
print('O MEDIA DOS NUMEROS DIGITADOS FOI {}'.format(media))
