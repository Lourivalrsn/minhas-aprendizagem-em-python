media = 0
maior = 0
velho = ""
menor = 0
for c in range(4):
    nome = input('Digite seu nome: ').upper().lower().strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()
    media = (media + idade)
    if sexo == 'M' and idade > maior:
     maior = idade
     velho = nome
    if sexo == 'F' and idade < 20:
        menor += 1

print('existe {} mulheres menores que 20'.format(menor))
print('o nome do homem mais velho é: {}'.format(velho))
print('a media de idade é {:.1f}'.format(media / 4))
