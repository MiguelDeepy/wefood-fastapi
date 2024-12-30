from sqlalchemy import Boolean, Column, Enum, Float, Integer, String

from app.domain.entities.produto import CategoriaProduto
from app.infrastructure.config.database import Base


class ProdutoModel(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500))
    preco = Column(Float, nullable=False)
    categoria = Column(Enum(CategoriaProduto))
    disponivel = Column(Boolean, default=True)
    imagem_url = Column(String(255))
    tempo_preparo_minutos = Column(Integer)
