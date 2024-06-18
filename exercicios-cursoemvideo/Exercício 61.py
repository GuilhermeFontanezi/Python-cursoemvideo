termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = termo + 10 * razao
while termo != decimo_termo:
    termo = termo + razao
    print(termo)
