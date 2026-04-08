from random import randint
from time import sleep
num_aleatorio = randint(1, 10)
tentativas = 0
print('=x=' * 12)
print('Vou pensar em um numero entre 1 e 10')
print('=x=' * 12)
while True:
    chute = int(input('Digite um valor: '))
    tentativas += 1
    print('pensado...')
    sleep(1)
    if chute == num_aleatorio:
        print('parabens você acertou!')
        break
    else:
        print('tente novamente')

print('voce acertou com {} tentativas'.format(tentativas))



