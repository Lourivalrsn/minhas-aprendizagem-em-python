num = int(input('digite um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
       print('\033[32m', end='')
       total += 1
    else:
       print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[32m\no numero {} foi divisivel {} vezes\033[m'.format(num, total))
if total == 2:
    print('\033[32mentão ele é primo\033[m')
else:
    print('\033[31mentão ele não é primo\033[m')
