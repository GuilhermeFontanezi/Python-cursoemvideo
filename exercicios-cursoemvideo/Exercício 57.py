sexo = input('Digite o seu sexo: [M|F]: ').lower().strip()
while sexo not in 'MmFf':
    sexo = input('Dados invalidos. Por favor digite um sexo valido: ').lower().strip()
print('obrigado, agora sei seu sexo {}!'.format(sexo))
