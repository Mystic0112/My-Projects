#função tera print e input para simular um menu interativo com o usuario, nao representativo
#assim uma regra de negocio de algoritimo

def opçoes_menu():
    print('-' * 20)
    print('Sistema de estoque')
    print('-' * 20)

    print('1 - Adicionar um novo produto')
    print('2 - Visualizar estoque')
    print('3 - Sair')
    print('4 - Consultar Produto')

    print('-' * 20)
    opçao = int(input(' Informe sua opção: '))

    return opçao



