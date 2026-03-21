a = float(input('digite o primeiro lado: '))
b = float(input('digite o segundo lado: '))
c = float(input('digite o terceiro lado: '))

if a < b + c and b < a + c and c < a + b:

  if a == b == c:
    print('é um triagulo Equilaterio')

  elif a == b or a == c or b == c:
    print('é um triagulo isosceles')

  else:
    print('é um triagulo escaleno')
else:
    print('não da para fazer um triagulo')
