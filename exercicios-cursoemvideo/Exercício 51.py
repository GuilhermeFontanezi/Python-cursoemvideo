termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = termo + (10 - 1) * razao
for c in range(termo, decimo_termo, razao):
    print(c, end='⇥ ')
    