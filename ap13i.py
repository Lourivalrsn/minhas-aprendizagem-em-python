from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = anoatual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('são {} pessoas que são maiores de idade'.format(maior))
print('são {} pessoas que são menores de idade'.format(menor))
