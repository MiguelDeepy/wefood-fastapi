import pytest
from src.domain.value_objects import CPF


def test_valid_cpf():
    cpf = CPF(value='12334512525')
    assert str(cpf) == '12334512525'


def test_invalid_eleven_digits():
    with pytest.raises(ValueError) as exc_info:
        CPF(value='1233451252')
    assert "CPF deve ter 11 dígitos" in str(exc_info)


def test_clean_digits():
    cpf = CPF(value='12334=51%25-25')
    assert str(cpf) == '12334512525'
