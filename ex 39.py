ano_nascimento = int(input('em qual ano você nasceu? '))
import datetime
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print('Já é a hora de você se alistar para o serviço militar!')
elif idade < 18:
    espera = 18 - idade
    print(f'Ainda não é o momento de se alistar. Falta {espera} ano/s para seu alistamento')
else:
    atraso = idade - 18
    print(f'Já passou do tempo do seu alistamento! Você deveria ter se alistado há {atraso} ano/s!')

'''outra forma:
from datetime import date
atual = date.today().year
nasc = int(input('qual ano voce nasceu?')
idade = atual - nasc



'''