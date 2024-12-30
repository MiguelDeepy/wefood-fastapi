from typing import Optional
from base import BaseEntity
from src.domain.value_objects import Email, CPF, Name


class Customer(BaseEntity):
    id: Optional[int] = None
    name: Name
    email: Email
    cpf: CPF
    phone_number: Optional[str] = None

    class Config:
        json_encoders = {
            Name: lambda n: str(n),
            Email: lambda e: str(e),
            CPF: lambda c: str(c)
        }


class CustomerCreate(Customer):
    pass


class CustomerResponse(Customer):
    pass


class CustomerDeletedResponse(Customer):
    msg: str


class CustomerRequest(BaseEntity):
    cpf: str
