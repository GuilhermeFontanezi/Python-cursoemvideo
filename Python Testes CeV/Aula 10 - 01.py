n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2

print('A sua média foi {:.1f}'.format(m))

if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')



# Explicação do if e esle

# nome = str(input('Qual seu nome? ')).strip()
# if nome == 'Guilherme':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tao normal *-*')
# print('É um prazer te conhecer {}'.format(nome))
