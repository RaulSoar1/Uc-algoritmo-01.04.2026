#SISTEMA DE GESTÃO DE BIBLIOTECA

#dicionario p/ armazenar os livros
emprestimosAtivos = {}
historico = []

#lista p/ armazenar o historico de transição
catalogo = {}


# função: adicionar livro


def adicionarlivro(codigo, título, autor, quantidade):
    if codigo in catalogo:
        print(f"erro: livro com codigo{codigo} já existe")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }


    print(f"livro'{titulo}' adicionando com sucesso")
    return True

adicionarlivro("l001", "codigo limpo", "robert martin", 2)