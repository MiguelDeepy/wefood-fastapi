from pydantic import BaseModel, field_validator
from decimal import Decimal


class Money(BaseModel):
    amount: Decimal
    currency: str = "BRL"

    @field_validator('amount')
    def validate_amount(cls, v):
        if v < 0:
            raise ValueError("Valor não pode ser negativo")
        return v

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Moedas diferentes não podem ser somadas")
        return Money(amount=self.amount + other.amount, currency=self.currency)
