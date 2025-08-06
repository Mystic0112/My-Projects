#media da nota de aluno

Nota_1 = float(input('informe a primeira nota: '))
Nota_2 = float(input('informe a segunda nota: '))
Nota_3 = float(input('informe a terceira nota: '))
Nota_4 = float(input('informe a quarta nota: '))

#processamento das notas(somar todas e dividir por 4)

nota_total= Nota_1 + Nota_2 + Nota_3 + Nota_4

divisor_notas = 4

nota_final= nota_total / divisor_notas

print(f'A media final do aluno é {nota_final} ')