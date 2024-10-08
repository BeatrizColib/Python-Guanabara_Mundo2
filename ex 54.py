import datetime
cont_menor = 0
cont_maioridade = 0
for c in range(1,8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {c} pessoa: '))
    idade = datetime.datetime.now().year - ano_nascimento
    if idade >= 21:
        cont_maioridade += 1
    else:
        cont_menor += 1
print(f'A quantidade de pessoas que não atingiu a maioridade são: {cont_menor}'
      f'\nA quantidade que atingiu foi: {cont_maioridade}')

######### outra forma para se calcular a idade atual
from datetime import date
atual = date.today().year
nascimento = int('ano de nascimento: ')
idade = atual - nascimento
