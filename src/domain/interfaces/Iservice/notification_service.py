from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    async def send_notification(self, destinatario: str, assunto: str, mensagem: str):
        pass
