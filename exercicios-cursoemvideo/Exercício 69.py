resp = str
homem18 = 0
h_cadastrado = 0
mulher20 = 0
while resp != 'n':
    sexo = input('DIGITE SEU SEXO (M/F): ').strip().lower()
    idade = int(input('DIGITE A SUA IDADE: '))
    if sexo == 'm' and idade > 18:
        homem18 = homem18 + 1
    elif sexo == 'f' and idade < 20:
        mulher20 += 1

    if sexo == 'm':
        h_cadastrado += 1
    resp = input('DESEJA CONTINUAR? (S/N): ').strip().lower()
print(f'''HOMENS COM MAIS DE 18 ANOS {homem18}
QUANTIDADE DE HOMENS CADASTRADOS {h_cadastrado}
MULHERES COM MENOS DE 20 ANOS {mulher20}''')
