sexo = str(input('Digite o sexo: F ou M: ')).upper().strip()[0] #maiuscula, retirar espaços vazios, considerar apenas primeiro digito
while sexo not in 'FM': #enquanto nao for "FM"
    sexo = str(input('digite uma opção válida: apenas F ou M: ')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso!')