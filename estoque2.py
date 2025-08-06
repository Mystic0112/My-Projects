#lista que vai guardar todos os produtos
estoque = []

def adicionar_produto(novo_produto : dict) -> None:
    '''
        função para adicionar produto na lista de estqoue \n
        função sugere que um dicionario (novo_produto) seja \n
        informado no parametro, e a função retorna none (nada) \n    
    '''
    estoque.append(novo_produto)


def exibir_produtos() -> list:
        '''
            Função que retorna uma lista (estoque), contendo todos os produtos adicionados
        '''

        return estoque
    
def atualizar_estoque(descricao: str,quantidade: int) -> bool:
    '''
        Descrição: Função que atualiza a quantiade de um produto no estoque
        parametro: {descrição: str}para indentificiar o produto; e {quantidade: int}
                    para adicionar estoque atual. /n
        retorno: {bool}sendo true se o produto estiver no estoque, ou false se o produto
                    nao estiver cadastrado.
    '''
    #repetir para percorrer toda a lista do {estoque}, olhando a descrição de todoso os produtos
    for produto in estoque:
        if produto['descricao'] == descricao:
            produto['quantidade'] += quantidade
            return True
    else:
        return False
    
