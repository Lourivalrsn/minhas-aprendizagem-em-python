primeiro = int(input('digite um numero: '))
razao = int(input('digite a razao: '))
contado = 1
termo = primeiro
while contado <= 10:
    print(termo, end = ' => ', )
    termo = termo + razao
    contado += 1
