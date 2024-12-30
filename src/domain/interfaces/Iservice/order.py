from abc import ABC, abstractmethod
from src.domain.entities.order import OrderStatus, Order


class IOrderRepository(ABC):
    @abstractmethod
    async def search_with_id(self, id: int) -> Order:
        pass

    @abstractmethod
    async def save(self, order: Order) -> Order:
        pass

    @abstractmethod
    async def update_status(self, id: int, status: OrderStatus) -> Order:
        pass

    @abstractmethod
    async def list_customer(self, customer_id: str) -> list[Order]:
        pass
