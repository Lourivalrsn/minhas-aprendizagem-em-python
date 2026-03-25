a = int(input('Digite primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = a + (10 - 1) * r
for c in range(a, decimo + r, r):
    print('{}'.format(c), end=' =>')
print('FIM')
