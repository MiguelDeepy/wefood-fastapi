from .base_domain_exception import DomainException


class ValidationException(DomainException):
    """Exceção para erros de validação"""
    pass


class InvalidEmailException(ValidationException):
    """Email inválido"""
    pass


class InvalidPhoneException(ValidationException):
    """Número de telefone inválido"""
    pass


class InvalidCPFException(ValidationException):
    """CPF inválido"""
    pass
