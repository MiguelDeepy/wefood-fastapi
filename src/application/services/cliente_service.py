class ClienteService:
    def __init__(self, cliente_repository):
        self.cliente_repository = cliente_repository

    async def validar_cpf(self, cpf: str) -> bool:
        if not cpf or len(cpf) != 11:
            return False
        return True

    async def validar_email(self, email: str) -> bool:
        if not email or '@' not in email:
            return False
        return True

    async def verificar_cliente_existente(self, cpf: str) -> bool:
        cliente = await self.cliente_repository.buscar_por_cpf(cpf)
        return cliente is not None

    async def formatar_dados_cliente(self, dados_cliente: dict) -> dict:
        return {
            "nome": dados_cliente.get("nome", "").strip().upper(),
            "email": dados_cliente.get("email", "").lower().strip(),
            "cpf": dados_cliente.get("cpf", "").replace(".", "").replace("-", "")
        }

    async def validar_dados_cliente(self, dados_cliente: dict) -> bool:
        if not dados_cliente.get("nome"):
            raise ValueError("Nome é obrigatório")

        if not await self.validar_cpf(dados_cliente.get("cpf")):
            raise ValueError("CPF inválido")

        if not await self.validar_email(dados_cliente.get("email")):
            raise ValueError("Email inválido")

        return True
