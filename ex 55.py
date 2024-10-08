menor_peso = 0
maior_peso = 0
for pessoa in range(1,6):
    peso = float(input(f'Digite o peso da {pessoa}: '))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso: #aqui nao pode ser else, pois tem duas variaveis, e assim não daria para ser exato no que se precisa. Pode ser if ou elif
            menor_peso = peso
print(f'O maior peso digitado foi {maior_peso} e o menor foi {menor_peso}')