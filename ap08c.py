from random import choices
a = str(input('Digite o  nome do primeiro aluno: '))
b = str(input('Digite o  nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
g = choices(list(map(str, [a,b,c,d])))
print(f'O nome do aluno sorteado foi: {g}')
