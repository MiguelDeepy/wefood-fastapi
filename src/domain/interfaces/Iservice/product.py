from abc import ABC, abstractmethod
from src.domain.entities.product import ProductCategory, Product


class IProductRepository(ABC):
    @abstractmethod
    async def search_with_id(self, id: int) -> Product:
        pass

    @abstractmethod
    async def list_category(self, category: ProductCategory) -> list[Product]:
        pass

    @abstractmethod
    async def save(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def update(self, id: int, datas: dict) -> Product:
        pass

    @abstractmethod
    async def change_availability(self, id: int, available: bool) -> Product:
        pass
