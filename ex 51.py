inicio = int(input('Qual o primeiro número para a PA: '))
razão = int(input('Qual razão para a progressão aritmética: '))
ultimo = inicio + (10 - 1) * razão #(10 - 1) porque quer saber ate o decimo termo, colocando-se até o termo que se quer saber

print(f'''O primeiro termo é {inicio}, indo até o décimo termo com a razão de {razão}, chegamos a:''')
for c in range(inicio, ultimo + razão, razão):
    print(c, end="-")