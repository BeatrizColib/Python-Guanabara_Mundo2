cont = 0
soma = 0
parada = 999
print('\033[7:31mDigite quantos números inteiros quiser, para parar digite 999!\033[m')
n = int(input('Digite o primeiro número: '))
while n != parada:
    if n != parada:
        soma += n
        cont += 1
        n = int(input(f'digite o {cont + 1}º: '))
print(f'\033[7:33mVocê digitou {cont} números e o somatório deles é {soma}!\033[m')
