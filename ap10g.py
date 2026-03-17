salario = float(input('digite seu salario: R$'))
a = salario * 1.10
b = salario * 1.15
if salario >= 1250:
    print('seu salario teve um aumento de 10% agora é:R$ {:.2f}'.format(a))
else:
    print('seu salario teve um aumento de 15% agora é:R$ {:.2f}'.format(b))
