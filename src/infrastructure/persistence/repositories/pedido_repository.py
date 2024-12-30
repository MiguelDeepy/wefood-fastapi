from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.domain.entities.pedido import Pedido
from app.domain.ports.repository.models.pedidos import PedidoModel


class SqlAlchemyPedidoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def criar(self, pedido: Pedido) -> int:
        """Cria um novo pedido no banco de dados"""
        pedido_model = PedidoModel(
            cliente_id=pedido.cliente_id,
            status=pedido.status,
            valor_total=pedido.valor_total,
            itens=pedido.itens
        )
        self.session.add(pedido_model)
        await self.session.commit()
        await self.session.refresh(pedido_model)
        return pedido_model.id

    async def buscar_por_id(self, id: int) -> Optional[Pedido]:
        """Busca um pedido pelo ID"""
        query = select(PedidoModel).where(PedidoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def listar_todos(self, skip: int = 0, limit: int = 100) -> List[Pedido]:
        """Lista todos os pedidos com paginação"""
        query = select(PedidoModel).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return [self._to_entity(model) for model in result.scalars().all()]

    async def buscar_por_cliente(self, cliente_id: int) -> List[Pedido]:
        """Busca pedidos de um cliente específico"""
        query = select(PedidoModel).where(PedidoModel.cliente_id == cliente_id)
        result = await self.session.execute(query)
        return [self._to_entity(model) for model in result.scalars().all()]

    async def atualizar_status(self, id: int, novo_status: str) -> Optional[Pedido]:
        """Atualiza o status de um pedido"""
        query = select(PedidoModel).where(PedidoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()

        if model:
            model.status = novo_status
            await self.session.commit()
            await self.session.refresh(model)
            return self._to_entity(model)
        return None

    async def deletar(self, id: int) -> bool:
        """Remove um pedido do banco de dados"""
        query = select(PedidoModel).where(PedidoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()

        if model:
            await self.session.delete(model)
            await self.session.commit()
            return True
        return False

    async def buscar_por_status(self, status: str) -> List[Pedido]:
        """Busca pedidos por status"""
        query = select(PedidoModel).where(PedidoModel.status == status)
        result = await self.session.execute(query)
        return [self._to_entity(model) for model in result.scalars().all()]

    async def atualizar(self, id: int, pedido: Pedido) -> Optional[Pedido]:
        """Atualiza os dados de um pedido"""
        query = select(PedidoModel).where(PedidoModel.id == id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()

        if model:
            model.cliente_id = pedido.cliente_id
            model.status = pedido.status
            model.valor_total = pedido.valor_total
            model.itens = pedido.itens
            await self.session.commit()
            await self.session.refresh(model)
            return self._to_entity(model)
        return None

    def _to_entity(self, model: PedidoModel) -> Pedido:
        """Converte um modelo do banco de dados para entidade do domínio"""
        return Pedido(
            id=model.id,
            cliente_id=model.cliente_id,
            status=model.status,
            valor_total=model.valor_total,
            itens=model.itens
        )
