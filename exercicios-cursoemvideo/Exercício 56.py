soma_idade = 0
idade_homemvelho = 0
nome_homem = ''
mulher_20 = 0

for c in range(1, 5):
    print('--------{}°Pessoa--------'.format(c))
    nome = input('Qual é o seu nome: ').strip().title()
    idade = int(input('Qual a sua idade: '))
    sexo = input('Sexo:[M/F]').strip().upper()
    soma_idade = soma_idade + idade
    if sexo == 'M' and idade > idade_homemvelho:
        nome_homem = nome
        idade_homemvelho = idade
    elif sexo == 'F' and idade < 20:
        mulher_20 = mulher_20 + 1
media = soma_idade / 4
print('''A média de idade do grupo é {}
O homem mais velho tem {} anos e se chama {}
Ao todo são {} mulheres com menos de 20 anos'''.format(media, idade_homemvelho, nome_homem, mulher_20))
