from datetime import datetime


class PedidoService:
    def __init__(self, pedido_repository, produto_repository):
        self.pedido_repository = pedido_repository
        self.produto_repository = produto_repository

    async def calcular_valor_total(self, itens):
        total = 0
        for item in itens:
            produto = await self.produto_repository.buscar_por_id(item.produto_id)
            total += produto.preco * item.quantidade
        return total

    async def verificar_disponibilidade_produtos(self, itens):
        for item in itens:
            produto = await self.produto_repository.buscar_por_id(item.produto_id)
            if not produto.disponivel:
                raise ValueError(f"Produto {produto.nome} não está disponível")

    async def validar_horario_funcionamento(self):
        # Verifica se o estabelecimento está em horário de funcionamento
        hora_atual = datetime.now().hour
        if not (10 <= hora_atual <= 22):  # exemplo: funcionamento das 10h às 22h
            raise ValueError("Fora do horário de funcionamento")

    async def calcular_tempo_preparo(self, itens):
        # Calcula o tempo estimado de preparo baseado nos itens
        tempo_total = 0
        for item in itens:
            produto = await self.produto_repository.buscar_por_id(item.produto_id)
            tempo_total += produto.tempo_preparo * item.quantidade
        return tempo_total

    async def aplicar_desconto(self, valor_total, tipo_desconto):
        # Aplica diferentes tipos de desconto (fidelidade, promocional, etc)
        descontos = {
            "FIDELIDADE": 0.1,  # 10% desconto
            "PRIMEIRA_COMPRA": 0.15,  # 15% desconto
            "PROMOCAO_DIA": 0.05  # 5% desconto
        }
        return valor_total * (1 - descontos.get(tipo_desconto, 0))

    async def verificar_limite_itens(self, itens):
        # Verifica se o pedido não excede um limite máximo de itens
        total_itens = sum(item.quantidade for item in itens)
        if total_itens > 20:  # exemplo: máximo de 20 itens por pedido
            raise ValueError("Quantidade de itens excede o limite permitido")

    async def validar_estoque(self, itens):
        # Verifica se há estoque suficiente para os itens
        for item in itens:
            produto = await self.produto_repository.buscar_por_id(item.produto_id)
            if produto.quantidade_estoque < item.quantidade:
                raise ValueError(f"Estoque insuficiente para o produto {produto.nome}")
