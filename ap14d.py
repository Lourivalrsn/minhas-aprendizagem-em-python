valor = int(input('Digite um numero: '))
resultado = 1
guardado = valor
while valor > 1:
    print('o fatorial de {} x {} é {}'.format(resultado, valor, resultado * valor ))
    resultado *= valor
    valor -= 1
print('fatorial é', resultado)
