inicio = int(input('digite o inicio da sua PA: '))
razao = int(input('digite a razão da sua PA: '))
termo = inicio
contador = 1

#aqui é para progressão aritmética
'''while contador <= 10:
    print(f'{termo}', end='')
    print(' -> ' if contador < 10 else '.', end='')
    termo += razao
    contador += 1
print()'''

#aqui para prog geométrica
print(f'{termo} - ', end='') #imprimir o primeiro termo antes da sequencia
while contador <= 10:
    termo *= razao
    contador += 1
    print(f'{termo}', end='')
    print(' -> ' if contador < 11 else '.', end='')