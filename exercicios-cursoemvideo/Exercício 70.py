resp = str
somatotal = 0
preco_1000 = 0
barato = 0
nome = str
while resp != 'n':
    nome_produto = input('Qual é o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: '))
    somatotal = somatotal + preco_produto
    if preco_produto >= 1000:
        preco_1000 += 1

    if barato < preco_produto:
        barato = preco_produto
        nome = nome_produto
    resp = input('deseja continuar? [S|N]: ')
print('-'*25)
print(f'''TOTAL GASTO NA COMPRA {somatotal:.2f}
PRODUTOS COM MAIS DE 1000 REAIS {preco_1000}
NOME DO PRODUTO MAIS BARATO {nome}''')
