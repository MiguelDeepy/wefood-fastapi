from abc import ABC, abstractmethod
from src.domain.entities.customer import Customer
from src.domain.value_objects import CPF


class ICustomerRepository(ABC):
    @abstractmethod
    async def search_with_cpf(self, cpf: CPF) -> Customer:
        pass

    @abstractmethod
    async def save(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    async def update(self, cpf: CPF, dados: dict) -> Customer:
        pass

    @abstractmethod
    async def delete(self, cpf: CPF) -> bool:
        pass
