valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
sair = False
while not sair:  #outra forma: while opçao != 5:
    opçao = int(input('''Menu:
     1 - somar
     2 - multiplicar
     3 - saber qual maior
     4 - novos números
     5 - sair do programa
     Qual opção você deseja: '''))
    if opçao == 1:
        resultado = valor1 + valor2
        print(f'\033[7:31mos valores foram {valor1} e {valor2}, o resultado foi {resultado}\033[m')
    elif opçao == 2:
        resultado = valor1 * valor2
        print(f'\033[7:32mos valores foram {valor1} e {valor2}, o resultado foi {resultado}\033[m')
    elif opçao == 3:
        if valor1 > valor2: #outra forma( if valor1 > valor2: maior = valor1 else: maior = valor2
            print('\033[7:33mO primeiro valor é maior\033[m')
        elif valor2 > valor1:
            print('\033[7:33mO segundo valor é maior!\033[m')
        else:
            print('\033[7:33mOs valores são iguais!\033[m')
    elif opçao == 4:
        print('\033[36mdigite novos números\033[m')
        valor1 = int(input('\033[36mQual o primeiro: \033[m'))
        valor2 = int(input('\033[36mQual o segundo: \033[m'))
    elif opçao == 5:
        sair = True  #se la em cima for opcao != 5, aqui fica print("finalizando")
    else:
        print('\033[7mDigite uma opção válida!\033[m')
    print('*-'*25)
print('\033[31mAté breve!\033[m')