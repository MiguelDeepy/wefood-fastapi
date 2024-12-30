import pytest
from decimal import Decimal
from src.domain.value_objects.money import Money


def test_money_addition():
    m1 = Money(amount=Decimal("10.00"), currency="BRL")
    m2 = Money(amount=Decimal("20.00"), currency="BRL")
    result = m1 + m2
    assert result.amount == Decimal("30.00")
    assert result.currency == "BRL"


def test_negative_amount():
    with pytest.raises(ValueError):
        Money(amount=Decimal("-10.00"))
