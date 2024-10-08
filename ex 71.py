print(f'\033[31m{" CAIXA ELETRÔNICO ":=^50}\033[m')
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula = 50 #começa com a maior disponível, no caso é a de 50
totalcedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else: #aqui o total passou a ser, ou é desde o inicio menor que a maior cedula que começou = 50.
        if totalcedulas > 0:
            print(f'total de {totalcedulas} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break
print('volte sempre...')

