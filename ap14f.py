primeiro = int(input('digite um numero: '))
razao = int(input('digite uma razao: '))
contador = 1
termo = primeiro
total = 11
while contador <= total:
    print(termo, end=' ')
    termo += razao
    contador += 1

    if contador == total:
     print('''
[1]adicionar mais termos')
[2]fechar programa''')
     escolha = int(input('digite sua escolha: '))
     if escolha == 1:
      vezes = int(input('digite quantos termos deseja: '))
      total += vezes
     else:
      print('fechado programa')
      break
