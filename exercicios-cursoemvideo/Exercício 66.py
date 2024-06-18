soma = 0
contador = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    contador = contador + 1
    soma = soma + numero
print(f'''FIM
COM OS DADOS OBTIDOS CONSEGUIMOS:
A soma de todos os numeros digitados: {soma}
Quantos numero foram contados {contador}''')
