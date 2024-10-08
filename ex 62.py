inicio = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão da sua PA: '))
termo = inicio
contador = 1
total = 0
continuar = 10

print(f'{termo} - ', end='')

while continuar != 0:
    total = total + continuar #aqui o total fica valendo 10 / total = 0 + 10
    while contador <= total:
        termo += razao
        contador += 1
        print(f'{termo}', end='')
        print(' -> ' if contador < total + 1 else '.', end='')
    print(' Pausa...')
    continuar = int(input('Gostaria de ver mais quantos termos (digite 0 para sair): '))
print(f'A quantidade de termos foi {total}')

