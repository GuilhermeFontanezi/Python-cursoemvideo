'''resp = 's'.strip().lower()
while resp == 's':
    nome = input('Digite qual é o seu nome: ')
    resp = str(input('Quer continuar? (s/n): '))'''

cp = 0
ci = 0
print('DIGITE "0" PARA FINALIZAR O PROGRAMA')
numero = 1
while numero != 0:
    numero = int(input('Digite um valor: '))
    if numero != 0:
        if numero % 2 == 0:
            cp = cp + 1
        else:
            ci = ci + 1
print('''Analizando os dados acima obtivemos um total de:
{} numeros pares;
{} numeros ímpares'''.format(cp, ci))
