import pytest
from src.domain.value_objects import Name


def test_name_greater_than():
    with pytest.raises(ValueError) as exc_info:
        Name(value="Mi")
    assert "Nome deve ter pelo menos 3 caracteres" in str(exc_info.value)


def test_name_less_than():
    with pytest.raises(ValueError) as exc_info:
        mock_name = "Mig" * 50
        Name(value=mock_name)
    assert "Nome não pode ter mais de 100 caracteres" in str(exc_info.value)


def test_many_spaces():
    name = Name(value="Mig    ")
    assert str(name) == "Mig"


def test_no_numbers():
    name = Name(value="Mig123")
    assert str(name) == "Mig"
