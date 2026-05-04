c = 0
maior = 0
soma = 0
numeros = []
while True:
    num = int(input('Digite um numero: '))
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    c += 1
    numeros.append(num)
    soma += num
    maior = max(maior, num)
    menor = min(numeros)
    if escolha == 'S':
        print('ok digite o numero novamente')
    elif escolha == 'N':
        media = soma / c
        print('a media de todos os valores: {}'.format(media))
        print('o numero maior é: {}'.format(maior))
        print('o menor numero é: {}'.format(menor))
        break
