#receber o numero do usuario inteiro 
print(' Se você quer decompor escreva um numero, mas se não, escreva qualquer numero e pule para a proxima etapa')
n1 = int(input('informe 1 numero: '))


#iniciando o fator decomposição em 2

fator_decomposição = 2

#repetição para decompor o n~umero ate 1

while n1 > 1:
    if n1 % fator_decomposição == 0:
        print(f'{n1: 4.0f} | {fator_decomposição}')
        #o mesmo que: numero = numero / fator_decomposição
        n1 /= fator_decomposição
    else:
        fator_decomposição += 1

print(f'{n1}')      

















