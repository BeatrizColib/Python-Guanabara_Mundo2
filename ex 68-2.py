print('\033[7:33mVamos jogar Par ou Ímpar!\033[m')
cont = 0
from random import randint
from time import sleep
while True:
    computador = randint(0,10)
    jogador_numero = int(input('Qual número de 0 a 10: '))
    jogador_pi = str(input('Você quer ser Par ou Ímpar: ')).strip().upper()[0]
    while jogador_pi not in 'PIÍ':
        jogador_pi = str(input('Digite uma opção válida! Par ou Ímpar: ')).strip().upper()[0]
    res_pre = (computador + jogador_numero) % 2
    if res_pre == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if jogador_pi == resultado:
        cont += 1
        sleep(1)
        print(f'Eu escolhi {computador}!')
        sleep(1)
        print(f'\033[7:35mVocê venceu! Vamos de novo! A soma foi: {jogador_numero + computador}, deu {"Par!" if resultado == "P" else "Ímpar!"}!\033[m')
    else:
        sleep(1)
        print(f'Eu escolhi {computador}!')
        sleep(1)
        print(f'\033[7:31mGAME OVER! Você perdeu! A soma foi: {jogador_numero + computador}, deu {"Par!" if resultado == "P" else "Ímpar!"}\033[m')
        break
    print('Vamos jogar novamente...')