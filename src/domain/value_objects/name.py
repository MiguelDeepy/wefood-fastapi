from pydantic import BaseModel, field_validator
import re


class Name(BaseModel):
    value: str

    @field_validator('value')
    def validate_name(cls, v: str) -> str:
        clean_name = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', v)
        clean_name = ' '.join(clean_name.split())

        if len(clean_name) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        if len(clean_name) > 100:
            raise ValueError("Nome não pode ter mais de 100 caracteres")

        return clean_name

    def __str__(self) -> str:
        return self.value
