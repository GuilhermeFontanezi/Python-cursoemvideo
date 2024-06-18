lar = float(input('quantos metros tem a largura da parede: '))
a = float(input('quantos metros tem a altura da parede: '))
ar = lar * a
p = ar / 2
print('Sua parede tem a dimensão de {}x{} e a área é de {:.3f}m²'.format(lar, a, ar))
print('para pintar a parede, você precisará de {}L de tinta'.format(p))
