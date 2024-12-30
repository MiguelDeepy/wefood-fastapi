from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.domain.entities.produto import Produto
from app.domain.ports.repository.models.produtos import ProdutoModel


class SqlAlchemyProdutoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def criar(self, produto: Produto) -> int:
        """Cria um novo produto no banco de dados"""
        produto_model = ProdutoModel(
            nome=produto.nome,
            preco=produto.preco,
            categoria=produto.categoria,
            descricao=produto.descricao,
            disponivel=produto.disponivel,
            quantidade_estoque=produto.quantidade_estoque
        )
        self.session.add(produto_model)
        await self.session.commit()
        await self.session.refresh(produto_model)
        return produto_model.id

    async def buscar_por_id(self, id: int) -> Optional[Produto]:
        """Busca um produto pelo ID"""
        query = select(ProdutoModel).where(ProdutoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def listar_todos(self, skip: int = 0, limit: int = 100) -> List[Produto]:
        """Lista todos os produtos com paginação"""
        query = select(ProdutoModel).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return [self._to_entity(model) for model in result.scalars().all()]

    async def buscar_por_categoria(self, categoria: str) -> List[Produto]:
        """Busca produtos por categoria"""
        query = select(ProdutoModel).where(ProdutoModel.categoria == categoria)
        result = await self.session.execute(query)
        return [self._to_entity(model) for model in result.scalars().all()]

    async def atualizar(self, id: int, produto: Produto) -> Optional[Produto]:
        """Atualiza os dados de um produto"""
        query = select(ProdutoModel).where(ProdutoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()

        if model:
            model.nome = produto.nome
            model.preco = produto.preco
            model.categoria = produto.categoria
            model.descricao = produto.descricao
            model.disponivel = produto.disponivel
            model.quantidade_estoque = produto.quantidade_estoque
            await self.session.commit()
            await self.session.refresh(model)
            return self._to_entity(model)
        return None

    async def deletar(self, id: int) -> bool:
        """Remove um produto do banco de dados"""
        query = select(ProdutoModel).where(ProdutoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()

        if model:
            await self.session.delete(model)
            await self.session.commit()
            return True
        return False

    async def atualizar_estoque(self, id: int, quantidade: int) -> Optional[Produto]:
        """Atualiza a quantidade em estoque de um produto"""
        query = select(ProdutoModel).where(ProdutoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()

        if model:
            model.quantidade_estoque = quantidade
            await self.session.commit()
            await self.session.refresh(model)
            return self._to_entity(model)
        return None

    async def buscar_disponiveis(self) -> List[Produto]:
        """Lista todos os produtos disponíveis"""
        query = select(ProdutoModel).where(ProdutoModel.disponivel is True)
        result = await self.session.execute(query)
        return [self._to_entity(model) for model in result.scalars().all()]

    def _to_entity(self, model: ProdutoModel) -> Produto:
        """Converte um modelo do banco de dados para entidade do domínio"""
        return Produto(
            id=model.id,
            nome=model.nome,
            preco=model.preco,
            categoria=model.categoria,
            descricao=model.descricao,
            disponivel=model.disponivel,
            quantidade_estoque=model.quantidade_estoque
        )
