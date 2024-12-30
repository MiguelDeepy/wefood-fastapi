from abc import ABC, abstractmethod
from typing import Dict


class PaymentGateway(ABC):
    @abstractmethod
    async def create_payment(self, data_payment: Dict):
        pass
