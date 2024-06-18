frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
frase_junta = ''.join(palavras)
inverso = ''
for letra in range(len(frase_junta) - 1, -1, -1):
    inverso += frase_junta[letra]
print(frase_junta, inverso)
if frase_junta == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
