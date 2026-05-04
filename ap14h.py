c = 0
soma = 0
while True:
  n = int(input('digite um numero (999 para o programa): '))
  if n == 999:
   print('programa finalizado')
   break
  else:
      c += 1
      soma += n
print('foram digitados {} numeros'.format(c))
print('a soma dos numeros digitados:',soma)

