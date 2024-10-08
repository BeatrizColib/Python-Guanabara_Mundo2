'''numero = int(input('digite um numero: '))
from math import factorial
fatorial = factorial(numero)
print(fatorial)'''

numero = int(input('Digite um número para saber seu factorial: '))
c = numero
f = 1 #aqui é 1 porque com multiplicação a base neutra é 1. Na soma a base neutra é 0, como é no contador
print(f'Calculando {numero}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c #equivalente a f = f * c
    c -= 1 #equivalente a c = c-1 / começará com o numero, e vai subtraindo um a um.
print(f'{f}')

#com for
n = int(input('digite o numero: '))
factorial = 1
for c in range(n, 0, -1):
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    factorial *= c
print(f'{factorial}')
