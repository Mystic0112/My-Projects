#ano aqrquivo menu, importa para esse a
#funcao opções_menu

from menu import opçoes_menu
from estoque import adicionar_produto, visualizar_produto, consultar_produto

while True:
    opcao_escolhida = opçoes_menu()

    if opcao_escolhida == 1:
        descrição = input('Informe a descrição: ')
        quant = int(input('Informe a quantidade: '))
        valor = float(input('Informe o valor : '))
        #chama a função de add produto
        adicionar_produto(descrição,quant,valor)

    elif opcao_escolhida == 2:
        estoque = visualizar_produto()
        print(estoque)

    elif opcao_escolhida == 3:
        break

    elif opcao_escolhida == 4:
        descrição = input('informe a descrição: ')
        resultado = consultar_produto(descrição)
        print(resultado)

    else:
        print('opção invalida')


        