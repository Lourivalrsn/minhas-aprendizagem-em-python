frase = str(input('digite uma palavra: ')).upper().strip()
print('a letra A aparece {} '.format(frase.count('A')))
print('a primeira letra A aparece na posição {}'.format(frase.find('A')))
print('a ultima palavra A aparece {}'.format(frase.rfind('A')))
