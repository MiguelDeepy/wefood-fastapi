from app.domain.entities.produto import CategoriaProduto


class CriarProdutoUseCase:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    async def execute(self, dados_produto):
        produto_existente = await self.produto_repository.buscar_por_id(dados_produto.id)
        if produto_existente:
            raise ValueError("Produto já existe")

        return await self.produto_repository.salvar(dados_produto)


class AtualizarProdutoUseCase:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    async def execute(self, id: int, dados_atualizacao):
        produto = await self.produto_repository.buscar_por_id(id)
        if not produto:
            raise ValueError("Produto não encontrado")

        return await self.produto_repository.atualizar(id, dados_atualizacao)


class BuscarProdutoUseCase:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    async def execute(self, id: int):
        produto = await self.produto_repository.buscar_por_id(id)
        if not produto:
            raise ValueError("Produto não encontrado")
        return produto


class ListarProdutosPorCategoriaUseCase:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    async def execute(self, categoria: CategoriaProduto):
        return await self.produto_repository.listar_por_categoria(categoria)


class AlterarDisponibilidadeProdutoUseCase:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    async def execute(self, id: int, disponivel: bool):
        produto = await self.produto_repository.buscar_por_id(id)
        if not produto:
            raise ValueError("Produto não encontrado")

        return await self.produto_repository.alterar_disponibilidade(id, disponivel)
