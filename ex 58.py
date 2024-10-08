'''from random import randint
numero = randint(1,10)
cont = 0
num = int(input('Pensei em um número de 1 a 10, qual seu palpite para adivinhar: '))
while numero != num:
    num = int(input('Humm, você errou. Tente de novo: '))
    cont += 1
print(f'O número que pensei foi {numero} e você acertou na {cont + 1}ª vez!')'''

#outra forma

print('Escolhi um número inteiro entre 1 e 10. Adivinhe!')
acertou = False
palpites = 0 #sera meu contador
from random import randint
computador = randint(1,10)
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpites += 1
    if jogador == computador:
       acertou = True
    else:
        if jogador > computador:
            print('Pensei num número menor!')
        else:
            print('Pensei num número maior!')
print(f'Isso! pensei em {computador} e você acertou na {palpites}ª vez!')