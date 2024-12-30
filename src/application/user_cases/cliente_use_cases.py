from src.infrastructure.persistence.repositories.cliente_repository import ClienteRepository
from src.infrastructure.configuration.settings import REPORT
from src.infrastructure.configuration.database import Database
from src.infrastructure.configuration.log import logger


class CriarClienteUseCase:
    def __init__(self, db: Database):
        self.cliente_repository = ClienteRepository(db)

    async def execute(self, dados_cliente):
        if await self.cliente_repository.buscar_por_cpf(dados_cliente.cpf):
            logger.info(f"Client {dados_cliente.nome} exists, not registered")
            raise ValueError(REPORT['customer']['exists'])
        return await self.cliente_repository.criar(dados_cliente)


class AtualizarClienteUseCase:
    def __init__(self, db: Database):
        self.cliente_repository = ClienteRepository(db)

    async def execute(self, cpf, dados_atualizacao):
        cliente = await self.cliente_repository.buscar_por_cpf(cpf)
        if not cliente:
            logger.info(REPORT['customer']['not_found'])
            raise ValueError(REPORT['customer']['not_found'])
        return await self.cliente_repository.atualizar(cpf, dados_atualizacao)


class BuscarClienteUseCase:
    def __init__(self, db: Database):
        self.cliente_repository = ClienteRepository(db)

    async def execute(self, cpf):
        cliente = await self.cliente_repository.buscar_por_cpf(cpf)
        if not cliente:
            logger.info(REPORT['customer']['not_found'])
            raise ValueError(REPORT['customer']['not_found'])
        return cliente


class DeletarClienteUseCase:
    def __init__(self, db: Database):
        self.cliente_repository = ClienteRepository(db)

    async def execute(self, cpf):
        cliente = await self.cliente_repository.buscar_por_cpf(cpf)
        result = cliente.model_dump(mode='json')
        message = await self.cliente_repository.deletar(cpf)
        result['msg'] = message
        if not cliente:
            logger.info(REPORT['customer']['not_found'])
            raise ValueError(REPORT['customer']['not_found'])
        return result


class ListarClientesUseCase:
    def __init__(self, db: Database):
        self.cliente_repository = ClienteRepository(db)

    async def execute(self):
        list_cliente = await self.cliente_repository.listar_todos()
        if not list_cliente:
            logger.info("No customers")
            raise ValueError(REPORT['customer']['n_not_found'])
        return list_cliente


class ValidarClienteUseCase:
    def __init__(self, db: Database):
        self.cliente_repository = ClienteRepository(db)

    async def execute(self, cpf):
        cliente = await self.cliente_repository.buscar_por_cpf(cpf)
        if not cliente:
            return False
        return True
