numero = int(input('digite um número para saber sua tabuada: '))

for c in range(1, 11):
    resultado = c * numero
    print(f'{numero} x {c} = {resultado}')
