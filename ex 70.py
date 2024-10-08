tot = acimamil = maisbarato = 0
maisbaratonome = ' '
cont = 0 #este contador é para saber quantos produtos foram e saber o mais em conta
while True:
    nome = str(input('Qual nome do produto: ')).capitalize().strip()
    preço = float(input('Qual preço: R$ '))
    tot += preço
    cont += 1
    if preço >= 1000:
        acimamil += 1
    if cont == 1 or preço < maisbarato: #ao inves de ter um if preço < mais barato, repetindo o mesmo bloco. Pode-se simplificar assim
        maisbarato = preço
        maisbaratonome = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? Sim ou Não: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{"Finalizando!":~^60}')
print(f'O total da compra foi: R$ {tot:10.2f}') #total de 10 casas, com duas decimais
print(f'Quantidade de produtos que custam a partir de R$ 1.000,00: {acimamil}')
print(f'O produto mais barato foi: {maisbaratonome} R$ {maisbarato}')