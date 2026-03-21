peso = int(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

imc = peso / (altura ** 2)
if imc < 18.5:
    print('abaixo do peso')
    print('seu imc: {:.1f}'.format(imc))
elif  18.5 <= imc < 25:
    print('esta no peso ideal')
    print('seu imc: {:.1f}'.format(imc))
elif  25 <= imc < 30:
    print('você esta sobrepeso')
    print('seu imc: {:.1f}'.format(imc))
elif  30 <= imc < 40:
    print('você esta em obesidade')
    print('seu imc: {:.1f}'.format(imc))
elif imc >= 40:
    print('você esta em obesidade mórbida')
    print('seu imc: {:.1f}'.format(imc))
