print('\033[7;31;40m Olá, você chegou ao JOKENPÔ! Vamos jogar juntos! \033[m')
jogador_pessoa = int(input('''Qual sua escolha?
 1 - Pedra
 2 - Papel
 3 - Tesoura
  Digite o número da sua opção: '''))
import random
jogador_pc = random.randint(1,3)

if jogador_pc == jogador_pessoa:
    status = 'empate! ninguém ganhou!'
elif jogador_pc == 1 and jogador_pessoa == 2:
    status = 'Você ganhou! O papel ganha da pedra'
elif jogador_pc == 2 and jogador_pessoa == 1:
    status = 'Você perdeu! O papel ganha da pedra'
elif jogador_pc == 3 and jogador_pessoa == 1:
    status = 'Você ganhou! A Pedra ganha da tesoura'
elif jogador_pc == 1 and jogador_pessoa == 3:
    status = 'Você perdeu! A Pedra ganha da tesoura'
elif jogador_pc == 2 and jogador_pessoa == 3:
    status = 'Você ganhou! A tesoura ganha do papel'
elif jogador_pc == 3 and jogador_pessoa == 2:
    status = 'Você perdeu! A tesoura ganha do papel'
elif jogador_pessoa != 1 and jogador_pessoa != 2 and jogador_pessoa != 3:
    status = 'Você escolheu uma opção que não existe. Escolha uma opção válida!'
print(f'''
 Você escolheu {jogador_pessoa}.
 Eu escolhi {jogador_pc}. 
 O resultado foi: \033[7;31;40m {status}! \033[m''')