preco = float(input('digite o preço do produto: '))
print('opção de pagamento disponivel: a vista, a vista no cartão, 2x no cartão, 3x ou mais no cartão')
pagamento = input('digite a forma de pagamento pagamento: ')

if pagamento == 'a vista':
    print('na sua escolha a vista sera aplicado 10% de desconto')
    print('o preço era {:.2f} R$ agora é {:.2f} R$, obrigado pela compra, volte sempre'.format(preco, preco - (preco * 10 / 100)))

elif pagamento == 'a vista no cartão':
    print('a sua escolhar foi a vista no cartão sera aplicado 5% de desconto')
    print('o preço era {:.2f} R$ agora é {:.2f} R$, obrigado pela compra, volte sempre'.format(preco, preco - (preco * 5 / 100)))

elif pagamento == '2x no cartão':
    print('a sua escolhar foi 2x no cartão')
    print('o produto de {:.2f} R$ vai fica: {:.2f} R$ na parcela de 2x no cartão'.format(preco, preco - (preco / 2)))

elif pagamento == '3x ou mais no cartão':
    x = int(input('digite quantas vezes sera no cartão, tera um 20% de juros: '))
    juros = (preco * (1 + 0.20) / x)
    print('na sua escolhar de {:.0f}x o produto era {:.2f} R$ agora é {:.2f} R$ na parcela'.format(x, preco, juros))
