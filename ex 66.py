soma = cont = 0
n = 0
print('Digite valores para somar e saber sua média. Digite 999 para parar!')
while True:
    n = int(input('Digite um número: '))
    if n == 999: #verifica antes se o número é 999, para não somá-lo e parar
        break
    soma += n #a soma e o cont depois do break, o 999 não será somado, nem contado
    cont += 1
media = soma / cont
print(f'A soma dos valores é: {soma}, a média: {media:.2f}, quantidade de valores digitados foi: {cont}')