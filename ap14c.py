from time import sleep
while True:
    num = int(input('DIGITE UM NUMERO: '))
    num3 = int(input('DIGITE OUTRO NUMERO: '))
    print('''Escolha a operação:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA ''')
    escolha = int(input('digite sua escolha: '))
    if escolha == 1:
        print('A SOMAR DE {} + {} = {}'.format(num, num3, num + num3))

    elif escolha == 2:
        print('A MULTIPICAÇÃO DE {} x {} = {}'.format(num, num3, num * num3))

    elif escolha == 3:
        print('O MAIOR NUMERO É {}'.format(max(num3, num)))

    elif escolha == 4:
        print('OK, ENTÃO DIGITE SEUS NOVOS NUMEROS:')
    elif escolha == 5:
        print('FECHANDO PROGRAMA...')
        sleep(2)
        break
    elif escolha > 5:
        print('\033[0;31;40mERRO, escolha invalida\033[m')
