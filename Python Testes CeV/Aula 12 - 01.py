nome = input('Qual seu nome: ').strip()

if nome.lower() == 'Guizinho':
    print('Mais que nome belo!')
elif nome.lower() == 'boletos':
    print('Mais que grande merda, seu bosta!')  # Odeio eles )<:
elif nome.lower() == 'Pedro' or nome.lower() == 'Maria' or nome.lower() == 'João':
    print('Seu nome é bem popular no Brasil!')
else:
    print('que nome comum!')

if nome.lower() != 'boletos':
    print('Tenha um bom dia {}'.format(nome))
else:
    print('vai morrer nunca nao?')
