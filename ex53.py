print('Saiba se a frase é um palíndromo')
frase = str(input('Digite a frase: ')).strip().upper() #eliminar espaços externos
palavras = frase.split()  #quebra em splits #separou num vetor/lista
junto = ''.join(palavras) #retira os espaços internos
inverso = ''

for letra in range(len(junto) -1, -1, -1): #len(junto) - 1 é p/ começar contando da última letra / -1 é pq a primeira letra é 0, mas ele tem que ir até um a menos / -1 pq ele estará retroagindo
    #print(f'{letra}') #assim printará os números equivalentes as casas decimais
    #print(f'{junto[letra]}') #assim printará com as respectivas letras
    inverso += junto[letra] #outra forma da linha 9
if junto == inverso:
    print(f'\nA frase {junto} tem seu inverso como {inverso}, e são palíndromos!')
else:
    print(f'A frase {junto} tem seu inverso como {inverso} e nâo são palíndromos!')

####################################outra forma############

fras = str(input('Enter a sentence: ')).upper().strip()
words = fras.split()
together = ''.join(fras)
reverse = together[::-1] #: vai começar no inicio / : vai terminar no fim / -1 porque será de trás pra frente
print(f'A frase {together} tem seu inverso como {reverse}')
if together == reverse:
    print('é um palíndromo')
else:
    print('Não é um palíndromo')