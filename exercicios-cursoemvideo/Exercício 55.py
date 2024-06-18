maior_peso = 0
menor_peso = 0
nome_pesado = ''
nome_leve = ''

print('='*25)
print('O mais leve e o mais pesado')
print('='*25)
for c in range(1, 6):
    nome = input('Qual seu nome: ').strip().lower()
    peso = float(input('Qual é o seu peso?: '))
    print('--------------------')
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
            nome_pesado = nome
        elif peso < menor_peso:
            menor_peso = peso
            nome = nome_leve

print('A pessoa com o maior peso é o {} com {}Kg'.format(nome_pesado, maior_peso))
print('A pessoa com o menor peso é o {} com {}Kg'.format(nome_leve, menor_peso))
