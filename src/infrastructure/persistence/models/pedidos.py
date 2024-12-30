from sqlalchemy import (
    Column, DateTime, Enum, Float, ForeignKey, Integer, String
)

from app.domain.entities.pedido import StatusPedido
from app.infrastructure.config.database import Base


class PedidoModel(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    status = Column(Enum(StatusPedido))
    data_criacao = Column(DateTime)
    valor_total = Column(Float)
