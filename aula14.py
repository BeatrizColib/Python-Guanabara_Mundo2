for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

#flag - condição de parada, por exemplo, até ser digitado numero 0
n = 1
while n != 0:
    n = int(input('digite um valor: '))
print('fim')

#flag- condição de parada - até que o usuario diga nao
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('deseja continua: S ou N: ')).upper().strip()
print('Fim')

#para saber quantos numeros digitados sao impar/par
n = 1
par = impar = 0 #equivalente a par = 0 impar = 0
while n != 0: #quando o n for 0, ele para
    n = int(input('digite um numero: '))
    if n != 0: #esta linha serve para nao contar o 0 como numero par no final da contagem
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'voce digitou {par} numeros pares e {impar} numeros impares')