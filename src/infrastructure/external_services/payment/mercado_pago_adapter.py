import mercadopago
from typing import Dict
from app.domain.ports.payment_gateway import PaymentGateway


class MercadoPagoAdapter(PaymentGateway):
    def __init__(self, access_token: str):
        self.sdk = mercadopago.SDK(access_token)

    async def criar_pagamento(self, dados_pagamento: Dict):
        try:
            payment_data = {
                "transaction_amount": float(dados_pagamento["valor"]),
                "description": dados_pagamento["descricao"],
                "payment_method_id": dados_pagamento["metodo"],
                "payer": dados_pagamento["pagador"]
            }

            resultado = self.sdk.payment().create(payment_data)
            return resultado["response"]
        except Exception as e:
            raise Exception(f"Erro ao processar pagamento: {str(e)}")
