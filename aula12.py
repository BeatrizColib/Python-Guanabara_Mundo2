for c in range(0,5):
    print('Oi!')
print('Fim')

for c in range(1,7):
    print(c)
print('Fim')

for c in range(7,-5,-1): #o -1 dirá o que irá acontecer, ele irá contar subtraindo -1 de cada contador
    print(c)
print('Fim')

for c in range(0,10,2): #contará pulando de 2 em 2
    print(c)
print("fim")

n = int(input('Digite um número: '))
for c in range(1, n +1, 1 + 1):
#adicionou o +1 para realmente contar até o numero escolhido, pois no for in range,ele desconsidera o último número
# 1 + 1 é para contar no intervalo apenas considerando os ímpares
    print(c)
print('acabou')

#pode-se usar as variáveis com input para compor o laço, exemplo:
inicio = int(input('digite o inicio '))
fim = int(input('digite o final'))
passo = int(input('digite o passo'))
for c in range(inicio, fim +1, passo):
    print(c)
print('fim')

#usando for para repetir uma pergunta
for c in range(0,3):
    n = int(input(' digite a nota: '))
print('fim')

#para pedir numeros algumas vezes e somar todos eles
s = 0 #somatorio começa sendo 0
for c in range(0,4):
    n = int(input('digite um numero: '))
    s += n #equivalente a s = s + n
print(f'o somatório de todos os numeros foi {s}')