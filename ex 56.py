soma_idade = 0
media_idade_geral = 0
maior_idade_homem = 0
nome_homem_maisvelho = ''
menor_20_mulheres = 0
for pessoa in range(1, 5):
    print(f'_______ {pessoa}ª PESSOA______')
    nome = str(input('Qual nome: ')).strip().capitalize()
    idade = int(input('Qual idade: '))
    sexo = str(input('Qual sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mn':
        maior_idade_homem = idade
        nome_homem_maisvelho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        menor_20_mulheres += 1
media_idade_geral = soma_idade / 4
print(f'A média da idade de todo o grupo é {media_idade_geral}.')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_homem_maisvelho}.')
print(f'Tem {menor_20_mulheres} mulheres abaixo de 20 anos')