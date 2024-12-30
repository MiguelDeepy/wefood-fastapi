from enum import Enum
from typing import Optional
from pydantic import Field
from base import BaseEntity
from src.domain.value_objects import Name


class ProductCategory(Enum):
    LANCHE = "LANCHE"
    ACOMPANHAMENTO = "ACOMPANHAMENTO"
    BEBIDA = "BEBIDA"
    SOBREMESA = "SOBREMESA"


class Product(BaseEntity):
    id: Optional[int] = None
    name: Name
    description: str = Field(max_length=500)
    price: float = Field(gt=0)
    category: ProductCategory
    available: bool = True
    image_url: Optional[str] = None
    preparation_time_minutes: Optional[int] = Field(gt=0)

    def change_availability(self, available: bool) -> None:
        self.available = available

    def update_price(self, novo_preco: float) -> None:
        if novo_preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
        self.preco = novo_preco

    class Config:
        json_encoders = {
            Name: lambda n: str(n)
        }


class ProdutoCreate(Product):
    pass


class ProdutoResponse(Product):
    pass
