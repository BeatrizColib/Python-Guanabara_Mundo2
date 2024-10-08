soma = 0 #acumulador - soma todos os numeros
cont = 0 #contador - irá contar quantos números estão dentro da minha condição a ser especificado (ex "ah, achei mais um numero assim..")
cont_geral = 0
for c in range(1,501,2):
    print(c, end="-")
    if c % 3 == 0:
        soma +=c #ou soma = soma + c
        cont += 1 #ou cont = cont +1 - ele soma so 1 ao contador e nao o valor de c como na soma
    cont_geral += 1 #ou cont_geral= cont_geral + 1
print()
print()
print(f'A soma de todos os valores impares divisiveis por 3 é {soma}, foram achados/somados {cont} números')
print(f'A quantidade de todos os numeros do intervalo descrito foi {cont_geral}')