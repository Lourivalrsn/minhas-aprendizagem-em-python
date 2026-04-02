maior = 0
menor = 0
for c in range(5):
    peso = float(input('digite o peso das pessoa:'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('os pesos maior é: {} '.format(maior))
print('os pesos menor é: {} '.format(menor))
