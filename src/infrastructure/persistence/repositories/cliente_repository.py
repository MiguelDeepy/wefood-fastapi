from sqlalchemy.future import select
from typing import List, Optional
from app.domain.entities.clientes import Cliente
from app.domain.ports.repository.models.clientes import ClienteModel
from config.database import Database
from config.log import logger


class ClienteRepository:
    def __init__(self, db: Database):
        self.db = db

    async def criar(self, cliente: Cliente) -> int:
        async with self.db() as session:
            cliente_model = ClienteModel(
                nome=cliente.nome,
                email=cliente.email,
                cpf=cliente.cpf,
                telefone=cliente.telefone
            )
            session.add(cliente_model)
            await session.commit()
            await session.refresh(cliente_model)
            logger.info(f"Cliente ID: {cliente_model.id}, cadastrado.")
            return cliente_model

    async def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        async with self.db() as session:
            query = select(ClienteModel).where(ClienteModel.cpf == cpf)
            result = await session.execute(query)
            model = result.scalar_one_or_none()
            return self._to_entity(model) if model else None

    async def buscar_por_id(self, id: int) -> Optional[Cliente]:
        async with self.db() as session:
            query = select(ClienteModel).where(ClienteModel.id == id)
            result = await session.execute(query)
            model = result.scalar_one_or_none()
            return self._to_entity(model) if model else None

    async def listar_todos(self, skip: int = 0, limit: int = 100) -> List[Cliente]:
        async with self.db() as session:
            query = select(ClienteModel).offset(skip).limit(limit)
            result = await session.execute(query)
            return [self._to_entity(model) for model in result.scalars().all()]

    async def atualizar(self, id: int, cliente: Cliente) -> Optional[Cliente]:
        async with self.db() as session:
            query = select(ClienteModel).where(ClienteModel.id == id)
            result = await session.execute(query)
            model = result.scalar_one_or_none()

            if model:
                model.nome = cliente.nome
                model.email = cliente.email
                model.cpf = cliente.cpf
                await session.commit()
                await session.refresh(model)
                return self._to_entity(model)
            return None

    async def deletar(self, cpf: str) -> str:
        async with self.db() as session:
            query = select(ClienteModel).where(ClienteModel.cpf == cpf)
            result = await session.execute(query)
            model = result.scalar_one_or_none()

            if model:
                await session.delete(model)
                await session.commit()
                return "Customer deleted"
            return "Customer not deleted"

    async def buscar_por_email(self, email: str) -> Optional[Cliente]:
        async with self.db() as session:
            query = select(ClienteModel).where(ClienteModel.email == email)
            result = await session.execute(query)
            model = result.scalar_one_or_none()
            return self._to_entity(model) if model else None

    def _to_entity(self, model: ClienteModel) -> Cliente:
        return Cliente(
            id=model.id,
            nome=model.nome,
            email=model.email,
            cpf=model.cpf,
            telefone=model.telefone
        )
