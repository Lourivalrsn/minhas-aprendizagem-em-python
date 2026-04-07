sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('dados invalidos. por favor digite novamante seu sexo: ')).strip().upper()
print('sexo {} resistrado com sucesso'.format(sexo))
