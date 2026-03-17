a = float(input('digite um numero da reta: '))
b = float(input('digite outro numero da reta: '))
c = float(input('digite outro numero da reta: '))
a1 = a + b
b1 = a + c
c1 = b + c
if a1 > c and b1 > b and c1 > a:
    print('é possivel fazer um triangulo')
else:
    print('não possivel fazer um triangulo')
