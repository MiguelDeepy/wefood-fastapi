from datetime import datetime
from app.domain.entities.pedido import StatusPedido
from app.domain.ports.repository.models.pedidos import PedidoModel


class CriarPedidoUseCase:
    def __init__(self, pedido_repository, produto_repository, cliente_repository):
        self.pedido_repository = pedido_repository
        self.produto_repository = produto_repository
        self.cliente_repository = cliente_repository

    async def execute(self, dados_pedido):
        # Validar cliente
        cliente = await self.cliente_repository.buscar_por_cpf(dados_pedido.cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado")

        # Validar produtos e calcular valor total
        valor_total = 0
        for item in dados_pedido.itens:
            produto = await self.produto_repository.buscar_por_id(item.produto_id)
            if not produto or not produto.disponivel:
                raise ValueError(f"Produto {item.produto_id} indisponível")
            valor_total += produto.preco * item.quantidade

        # Criar pedido
        pedido = PedidoModel(
            cliente_id=dados_pedido.cliente_id,
            status=StatusPedido.RECEBIDO,
            data_criacao=datetime.now(),
            valor_total=valor_total
        )
        return await self.pedido_repository.salvar(pedido)


class AtualizarStatusPedidoUseCase:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    async def execute(self, pedido_id: int, novo_status: StatusPedido):
        pedido = await self.pedido_repository.buscar_por_id(pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")

        return await self.pedido_repository.atualizar_status(pedido_id, novo_status)


class BuscarPedidoUseCase:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    async def execute(self, pedido_id: int):
        pedido = await self.pedido_repository.buscar_por_id(pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        return pedido


class ListarPedidosClienteUseCase:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    async def execute(self, cliente_id: str):
        return await self.pedido_repository.listar_por_cliente(cliente_id)
