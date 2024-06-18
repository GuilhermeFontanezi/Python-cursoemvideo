m = float(input('Uma distância em metros: '))
km = m/1000
hec = m / 100
dec = m / 10
decim = m * 10
c = m * 100
mm = m * 1000
print('A medida de {}m corresponde a'.format(m))
print('{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(km, hec, dec, decim, c, mm))
