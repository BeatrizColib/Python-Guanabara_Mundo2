valor = float(input('Qual o valor da casa que você deseja comprar? '))
salario = float(input(' Qual seu salário mensal? '))
anos = int(input('Em quantos anos você pretende pagar? '))

parcela_mensal = valor / (anos*12)
if parcela_mensal >= 0.3 * salario:
    print('A parcela ficou acima de 30% do seu salário. Financiamento negado!')
else:
    quantidade_parcelas = anos * 12
    print(f'''A parcela é R${parcela_mensal:.3f} e ficou abaixo do equivalente a 30% do seu salário que é R${salario}.'
          Financiamento liberado!
          Você pagará um total de {quantidade_parcelas} parcelas mensais, equivalente a {anos} anos.''')