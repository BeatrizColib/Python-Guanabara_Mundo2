print('Olá, você chegou a calculadora de IMC, descubra qual o seu abaixo.')
peso = float(input('Qual seu peso em KG? '))
altura = float(input('Qual sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'abaixo do peso ideal'
elif 18.5 <= imc <25:
    status = 'no peso ideal'
elif 25 <= imc <=30:
    status = 'com sobrepeso'
elif 30 < imc <=40:
    status = 'com obesidade'
else:
    status = 'com obesidade mórbida'
print(f'Seu IMC é {imc:.2f} e você está {status}.')