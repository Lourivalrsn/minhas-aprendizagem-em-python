s = 0
contador = 0
for c in range(6):
    i = int(input('Digite um valor: '))
    if i % 2 == 0:
     s += i
     contador += 1
    else:
     print('valor desconsiderando')

print('você informou {} pares, a soma dos numeros pares que você digitou: {}'.format(contador, s))
