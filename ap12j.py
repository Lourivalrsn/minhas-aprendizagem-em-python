from random import choice
jogador = str(input('digite se é pedra, papel ou tesoura: '))
jokepor = ('pedra', 'papel', 'tesoura')
sorteado = choice(jokepor)
if jogador == sorteado:
    print('empate', sorteado)
elif jogador == 'pedra' and sorteado == 'tesoura':
    print('você ganhou', sorteado)

elif jogador == 'papel' and sorteado == 'pedra':
    print('voce ganhou', sorteado)

elif jogador == 'tesoura' and sorteado == 'papel':
    print('voce ganhou', sorteado)

else:
    print('voce nao ganhou', sorteado)
