n1 = int(input('digite um numero inteiro: '))
n2 = int(input('digite outro numero inteiro: '))

if n1 > n2:
    print('o primeiro valor é maior que o segundo')
elif n2 > n1:
    print('o segundo valor é maior que o primeiro')
elif n1 == n2:
    print('não existe valor maior, os dois são iguais')
