from sqlalchemy import Column, Integer, String

from app.infrastructure.config.database import Base


class ClienteModel(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(11))
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telefone = Column(String(20))
