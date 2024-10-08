print('\033[7:31:40m Olá, você chegou a calculadora de conversão de bases! \033[m')
operacao = int(input('''Bases para conversão:
1- Converter para binário
2- Converter para octal
3- Converter para hexadecimal
Escolha uma das opções: '''))
num = int(input('Qual número deseja converter? '))
print()
if operacao == 1:
    print(f'O número {num} convertido para \033[1:36m BINÁRIO \033[m é {bin(num)[2:]}')
elif operacao == 2:
    print(f'O número {num} convertido para \033[1:36m OCTAL \033[m é {oct(num)[2:]}')
elif operacao == 3:
    print(f'O número {num} convertido para \033[1:36m HEXADECIMAL \033[m é {hex(num)[2:]}')
else:
    print('Escolha uma opção válida!')
