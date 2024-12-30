class ProdutoService:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    async def validar_preco(self, preco: float) -> bool:
        # Validação de preço
        if not preco or preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
        return True

    async def validar_categoria(self, categoria: str) -> bool:
        categorias_validas = ["LANCHE", "ACOMPANHAMENTO", "BEBIDA", "SOBREMESA"]
        if categoria not in categorias_validas:
            raise ValueError("Categoria inválida")
        return True

    async def verificar_produto_existente(self, id: int) -> bool:
        produto = await self.produto_repository.buscar_por_id(id)
        return produto is not None

    async def validar_dados_produto(self, dados_produto: dict) -> bool:
        if not dados_produto.get("nome"):
            raise ValueError("Nome é obrigatório")

        if not await self.validar_preco(dados_produto.get("preco")):
            raise ValueError("Preço inválido")

        if not await self.validar_categoria(dados_produto.get("categoria")):
            raise ValueError("Categoria inválida")

        return True

    async def atualizar_estoque(self, id: int, quantidade: int):
        # Atualiza o estoque do produto
        produto = await self.produto_repository.buscar_por_id(id)
        if not produto:
            raise ValueError("Produto não encontrado")

        novo_estoque = produto.quantidade_estoque + quantidade
        if novo_estoque < 0:
            raise ValueError("Quantidade em estoque não pode ser negativa")

        return await self.produto_repository.atualizar_estoque(id, novo_estoque)

    async def verificar_disponibilidade(self, id: int, quantidade_requisitada: int) -> bool:
        # Verifica se há quantidade suficiente em estoque
        produto = await self.produto_repository.buscar_por_id(id)
        if not produto:
            raise ValueError("Produto não encontrado")

        return produto.quantidade_estoque >= quantidade_requisitada
