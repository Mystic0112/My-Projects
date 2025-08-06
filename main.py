from pprint import pprint
from estoque2 import adicionar_produto, atualizar_estoque, exibir_produtos


while True:
    opcao = int(input('informe sua opção:\n (1-adicionar produto:\n 2-exibir produtos:\n 3-atualizar estoque:\n 4- Sair)'))
    if opcao == 1:
        descricao = input('informe a descrição: ')
        quantidade = int(input('Informe a quantidade: '))
        valor = float(input('Informe o valor unitario do produto: '))

        #organizar os dados em um dicionario
        produto = {
            'descricao': descricao,
            'quantidade': quantidade,
            'valor': valor
        }

        #chamar a função adicionar_produto passando o dicionario {produto}
        adicionar_produto(produto)

    elif opcao == 2:
        produto = input('descrição do produto a ser atualizado: ')
        pprint(produto)
    
    elif opcao == 3:
        descricao = input('descrição do produto a ser atualizado: ')
        quantidade = int(input('informe a quantidade a ser adicionado: '))

        status = atualizar_estoque(quantidade)

        if status: #sugerindo (true)
            print('Produto atualizado com sucesso')
        else:
            print('produto nao encontrado')
    elif opcao == 4:
        break

