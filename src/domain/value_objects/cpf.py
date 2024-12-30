from pydantic import BaseModel, field_validator
import re


class CPF(BaseModel):
    value: str

    @field_validator('value')
    def validate_cpf(cls, v):
        cpf = re.sub(r'\D', '', v)
        if len(cpf) != 11:
            raise ValueError("CPF deve ter 11 dígitos")

        # Adicione aqui a lógica de validação do CPF
        return cpf

    def __str__(self):
        return self.value
