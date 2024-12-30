from pydantic import BaseModel, field_validator
from src.domain.exceptions.validation import ValidationException
import re


class Email(BaseModel):
    value: str

    @field_validator('value')
    def validate_empty(cls, v):
        if not v:
            raise ValidationException("Email não pode estar vazio")
        return v

    @field_validator('value')
    def validate_format(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValidationException("Formato de email inválido")
        return v

    def __str__(self):
        return self.value
