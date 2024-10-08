soma = 0 #somador
cont = 0 #contador
print('Olá, digite seis números para saber o somatório dos números pares!')
for c in range(1,7):
    numero = int(input(f'Digite numero {c}: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'O somatório de todos os números pares é {soma}, num total de {cont} números pares no intervalo')