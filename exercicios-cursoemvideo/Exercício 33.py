num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite o ultimo valor: '))

# maior numero das variveis
maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3

# Menor numero das variaveis
menor = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3

print('\033[31mO menor numero escolhido foi {}\033[m e o \033[36mmaior foi {}\033[m'.format(menor, maior))
