from datetime import date
ano = int(input('digite o ano de nascimento: '))
n1 = date.today().year
alistamento = n1 - ano
if alistamento == 18:
    print('ja é hora de se alistar')

elif alistamento < 18:
    print('voce ainda vai se alistar ao execito')
    print('falta {} ano para se alistar '.format((ano + 18) - n1))
    print('seu alistamento sera em {}'.format(ano + 18))

elif alistamento > 18:
    print('você ja passou do tempo de alistamento')
