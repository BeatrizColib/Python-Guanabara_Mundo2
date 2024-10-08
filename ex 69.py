maioridade = qnt_homem = qnt_mulhermenor20 = 0
while True:
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual sexo: F ou M: ')).strip().upper()[0] #poderia ser sexo = ' '
    print('-'*50)
    while sexo not in 'FM':
        sexo = str(input('Opção inválida. Digite F ou M: ')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo in 'M': #ou sexo == 'M':
        qnt_homem += 1
    if sexo in 'F' and idade < 20: #sexo == 'F' and idade < 20:
        qnt_mulhermenor20 += 1
    continuar = str(input('Deseja cadastrar mais pessoas? Sim ou Não: ')).upper().strip()[0] #ou continuar = ' '
    print('-' * 50)
    while continuar not in 'SN':
        continuar = str(input('Digite apenas Sim ou Não: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'\033[7:31mA quantidade de pessoas acima de 18 anos é: {maioridade}\033[m')
print(f'\033[7:32A quantidade de homens cadastrados foi: {qnt_homem}\033[m')
print(f'\033[7:35mA quantidade de mulheres abaixo de 20 anos foi: {qnt_mulhermenor20}\033[m')