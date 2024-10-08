print('='*30)
titulo = 'Sequência de Fibonacci'
print(f'{titulo:=^30}')
termos = int(input('Quantos termos você quer saber? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} ->', end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    cont += 1
    t1 = t2 #aqui ele vai "andando" com os termos, para continuar somando dois termos, gerando o t3 e assim por diante
    t2 = t3
    print(f'{t3} ->', end='')
print('Fim')
