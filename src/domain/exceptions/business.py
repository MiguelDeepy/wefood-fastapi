from .base_domain_exception import DomainException


class BusinessRuleException(DomainException):
    """Exceção para violações de regras de negócio"""
    pass


class InsufficientStockException(BusinessRuleException):
    """Estoque insuficiente"""
    pass


class OrderAlreadyCancelledException(BusinessRuleException):
    """Pedido já cancelado"""
    pass


class UserNotActiveException(BusinessRuleException):
    """Usuário inativo"""
    pass
