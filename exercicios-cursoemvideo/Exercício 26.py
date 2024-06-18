frase = input('Digite uma frase: ').strip().upper()
print('quants letras ´a´ tem na frase: {}'.format(frase.count('A')))
print('Localização da primeira letra ´a´ da frase: {}'.format(frase.find('A') + 1))
print('Localização da ultima letra ´a´ da frase: {}'.format(frase.rfind('A') + 1))
