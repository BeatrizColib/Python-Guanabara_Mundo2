print('''Olá, você chegou a Confederação Nacional de Natação!
        Verifique qual a sua categoria a seguir...''')
ano_nascimento = int(input('Qual o ano do seu nascimento? '))
import datetime
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

if idade <=9:
    status = 'mirim'
elif idade >9 and idade <= 14:
    status = 'infantil'
elif idade >14 and idade <=19:
    status = 'junior'
elif idade >19 and idade <=20:
    status = 'sênior'
else:
    status = 'master'
print(f'Sua idade é {idade} e sua categoria é a {status}!')

"""outra forma
from datetime import date
atual = date.today().year
..."""