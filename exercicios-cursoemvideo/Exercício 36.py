cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'sublinhado': '\033[4m'}
casa = float(input('Qual o valor da {}{}casa:{} '.format(cores['verde'], cores['sublinhado'], cores['limpa'])))
salario = float(input('Qual é o seu {}{}salário?{}: '.format(cores['sublinhado'], cores['verde'], cores['limpa'])))
anos = float(input('Quantos {}{}anos{} vc pretende pagar?: '.format(cores['sublinhado'], cores['vermelho'], cores['limpa'])))
prestacao = casa / (anos * 12)

if prestacao >= salario * 30 / 100:
    print('{}Você não pode comprar essa casa{}, infelizmente 30% do seu salario é menor q a prestação'.format(cores['vermelho'],                                                                                            cores['limpa']))
    print('para pagar uma casa de {:.2f} em {} anos a prestação ira ficar: {}{} {:.2f}'.format(casa, anos, cores['vermelho'], cores['limpa'], prestacao))
else:
    print('{}Você pode comprar essa casa!{}'.format(cores['verde'], cores['limpa']))
    print('para pagar uma casa de {:.2f} em {} anos a prestação ira ficar {:.2f}'.format(casa, anos, prestacao))
