n1 = float(input('digite a primeira nota do aluno: '))
n2 = float(input('digite a segunda nota do aluno: '))
s = (n1 + n2) / 2

if s < 5.0:
    print('sua nota é {:.1f}, você esta reprovado'.format(s))
elif s >= 5.0 and s < 6.9:
    print('sua nota é {:.1f}, você esta de recuperação'.format(s))
elif s >= 7.0:
    print('sua nota é {:.1f}, você esta aprovador parabens!'.format(s))
