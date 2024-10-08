print('Digite um número para saber se ele é primo ou não!')
numero = int(input('Qual número: '))
total = 0
for c in range(1, numero +1):
    if numero % c == 0:
        print('\033[36m', end='-')
        total += 1
    else:
        print('\033[31m', end='-')
    print(f'{c}', end='')
print(f'\nO número {numero} foi divisível {total} vezes.')
if total == 2:
    print('Por isso o número é primo!')
else:
    print('Por isso o número não é primo!')