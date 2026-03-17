base = int(input('digite um numero inteiro: '))
escolhei = input('em qual base sera essa conversão ex:binario, octal, hexadecimal: ')

if escolhei == 'binario':
    print('a sua escolha foi \033[32;40mbinario\033[m')
    print('o seu resultado é {}'.format(f'{base:b}'))

elif escolhei == 'octal':
    print('a sua escolha foi \033[34;40moctal\033[m')
    print('o resultado foi: {}'.format(f"{base:o}"))

elif escolhei == 'hexadecimal':
    print('a sua escolhar é \033[36;40mhexadecimal\033[m')
    print('o resultado é: {}'.format(f"{base:x}"))
else:
    print('\033[31;40merro!!!, por favor informe a base de conversão correta\033[m')
