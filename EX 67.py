print('\033[7:31mVocê chegou na Tabuada! Para sair digite qualquer número negativo!\033[m')

while True:
    n = int(input('Digite o número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('¨'*50)
print('\033[7:31mJá vai? Precisando, estou aqui! Bye Bye!\033[m')
print('¨'*50)