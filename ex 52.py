import math

numero = int(input('Digite o número para saber se ele é primo ou não: '))

for c in range(2, int(math.sqrt(numero)) + 1):
    print(end="")
if numero % c == 0:
    print(f'O número {numero} não é primo, pois ele tem mais '
            f'divisor além dele próprio e 1')
else:
    print(f'O número {numero} é primo, pois só é divisível por ele próprio e 1.')

