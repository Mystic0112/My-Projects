# criar uma lista para guardar todos os produtos
lista_produtos = []

#função para adicionar produtos ao estoque
def adicionar_produto(descrição,quant,valor):
    #colocando os valores em uma lista

    novo_produto = [descrição,quant,valor]
    #adicionando essa lista de produto, na lista
    # do estoque geral
    lista_produtos.append(novo_produto)

#Função para exibir os produtos do estoque
def visualizar_produto():
    return lista_produtos

def consultar_produto(descricao):
    for produto in lista_produtos:
         if produto [0] == descricao:
             return produto
    print('produto não cadastrado')
    return None



