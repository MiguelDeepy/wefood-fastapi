# flake8: noqa: E402
import os
import sys
import asyncio
sys.path.insert(0, os.getcwd())

from app.infrastructure.config.database import Base, Database
from app.domain.ports.repository.models.clientes import ClienteModel
from app.domain.ports.repository.models.pedidos import PedidoModel
from app.domain.ports.repository.models.produtos import ProdutoModel


if __name__ == "__main__":
    async def create_tables():
        async with Database()._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(create_tables())
