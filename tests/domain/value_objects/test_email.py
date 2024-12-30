import pytest
from src.domain.value_objects import Email
from src.domain.exceptions.validation import ValidationException


def test_valid_email():
    email = Email(value="user@example.com")
    assert str(email) == "user@example.com"
    assert email.value == "user@example.com"


def test_invalid_email_format():
    with pytest.raises(ValidationException) as exc_info:
        Email(value="invalid-email")
    assert "Formato de email inválido" in str(exc_info.value)


def test_invalid_email_domain():
    with pytest.raises(ValidationException) as exc_info:
        Email(value="user@")
    assert "Formato de email inválido" in str(exc_info.value)


def test_empty_email():
    with pytest.raises(ValidationException) as exc_info:
        Email(value="")
    assert "Email não pode estar vazio" in str(exc_info.value)
