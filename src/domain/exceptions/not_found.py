from .base_domain_exception import DomainException


class NotFoundException(DomainException):
    """Exceção para recursos não encontrados"""
    pass


class UserNotFoundException(NotFoundException):
    """Usuário não encontrado"""
    pass


class ProductNotFoundException(NotFoundException):
    """Produto não encontrado"""
    pass


class OrderNotFoundException(NotFoundException):
    """Pedido não encontrado"""
    pass
