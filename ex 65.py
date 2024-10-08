print('\033[31:7mDigite quantos números inteiros quiser, para saber sua média e qual o maior e menor valor!\033[m')
soma = cont = media = 0 #equivalente a digitar um por linha "soma = 0" "conta = 0"...
continuar = 'S'
n = int(input('digite o primeiro valor: '))
maior = menor = n
while continuar == 'S':
    soma += n
    cont += 1
    continuar = str(input('Deseja continuar: S ou N: ')).upper().strip()[0]
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('digite uma opção válida: S ou N: ')).upper().strip()[0]
    if continuar == 'S':
        n = int(input('Digite outro valor: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = soma / cont
print(f'A média de todos os valores digitados foi {media:.2f}. Núm digitados: {cont}')
print(f'O maior número digitado foi: {maior} e o menor: {menor}')
