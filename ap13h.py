invertido = str(input('Digite uma frase: ')).strip().upper()
frase = invertido.split()
junto = ''.join(frase)
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('é um palindromo')
else:
    print('não é um palindromo')
