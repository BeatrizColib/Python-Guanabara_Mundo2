lado1 = float(input('Digite um lado do triangulo: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado3 < lado1 + lado2 and lado2 < lado3 + lado1 and lado1 < lado3 + lado2:
    if lado1 == lado2 == lado3:
        status = 'forma-se um triângulo equilátero, o qual tem todos os seus lados do mesmo tamanho'
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3: '''ou elif lado1 != lado2 != lado3 != lado1:'''
        status = 'forma-se um triãngulo escaleno, o qual tem todos os lados de tamanhos diferentes'
    else:
        status = 'forma-se um triângulo isósceles, o qual tem dois lados iguais'
else:
    status = 'não é possível formar um triângulo'
print(f'Com as medidas {lado1},{lado2},{lado3}: {status}')