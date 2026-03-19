from datetime import date
anos = int(input('Qual é seu ano de nascimento? '))
n1 = date.today().year
idade = n1 - anos

if idade <= 9:
    print('o atleta tem {} anos!'.format(idade))
    print('o atleta é MIRIM')
elif idade >= 10 and idade <= 14:
    print('o atleta tem {} anos!'.format(idade))
    print('o atleta é infantil')

elif idade >= 15 and idade <= 19:
    print('o atleta tem {} anos!'.format(idade))
    print('o atleta é JUNIOR')

elif idade >= 20:
    print('o atleta tem {} anos!'.format(idade))
    print('o atleta é MASTER')
