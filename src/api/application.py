from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from app.infrastructure.web.api.v1.routes import cliente_routes
from app.infrastructure.web.middleware.error_handler import validation_exception_handler, generic_exception_handler


app = FastAPI(title="FastFood API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(cliente_routes.router, tags=["Clientes"])
# app.include_router(produto_routes.router, tags=["Produtos"])
# app.include_router(pedido_routes.router, tags=["Pedidos"])


app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
