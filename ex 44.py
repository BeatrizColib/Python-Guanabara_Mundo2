preco_produto = float(input('Qual preço do produto: R$ '))
condicao_pagamento = int(input('''Qual forma de pagamento deseja: 
 1 - à vista: dinheiro/cheque - desconto 10%
 2 - à vista: no cartão -  desconto de 5%
 3 - em até 2x no cartão -  sem juros
 4 - 3x ou mais no cartão - 20% de juros
 Digite o número da opção desejada.'''))
if condicao_pagamento == 1:
    valor_final = preco_produto * 0.9
    status = valor_final
elif condicao_pagamento == 2:
    valor_final = preco_produto * 0.95
    status = valor_final
elif condicao_pagamento == 3:
    valor_final = preco_produto
    status = valor_final
else:
    valor_final = preco_produto * 1.2
    status = valor_final
print()
print(f'Você escolheu a condição de pagamento {condicao_pagamento}. Ficando um total de R$ {valor_final:.2f}')