from enum import Enum
from typing import List, Optional
from base import BaseEntity


class OrderStatus(Enum):
    RECEBIDO = "RECEBIDO"
    EM_PREPARACAO = "EM_PREPARACAO"
    PRONTO = "PRONTO"
    FINALIZADO = "FINALIZADO"


class OrderItem(BaseEntity):
    product_id: int
    amount: int
    unit_price: float
    observations: Optional[str] = None

    def calculate_subtotal(self) -> float:
        return self.amount * self.unit_price


class Order(BaseEntity):
    id: Optional[int] = None
    cliente_id: Optional[int]
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.RECEBIDO
    value_total: float = 0

    def calculate_total(self) -> float:
        self.value_total = sum(item.calculate_subtotal() for item in self.items)
        return self.value_total

    def update_status(self, new_status: OrderStatus) -> None:
        self.status = new_status
