casa = float(input('Digite o valor da casa: '))
dinheiro = float(input('Digite o valor do dinheiro: '))
anos = float(input('Digite quantos anos vai pagar: '))
a = anos * 12
s = dinheiro * 0.30
v = casa / a
if v < s:
    print('você vai pagar R$ {:.2f}'.format(v))
    print('esses são os totais de meses que você vai pagar {:.0f}'.format(a))
elif v <= s:
    print('a compra dessa casa vai fica no limite')
    print('valor de pagamento: R$ {:.2f}'.format(v))
    print('esses são os totais de meses que você vai pagar: {:.0f}'.format(a))
else:
    print('infelismente foi negado a finaciar da compra dessa casa')
