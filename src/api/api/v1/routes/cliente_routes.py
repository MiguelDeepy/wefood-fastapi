from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.domain.entities.clientes import ClienteCreate, ClienteDeletedResponse, ClienteRequest, ClienteResponse
from app.application.user_cases.cliente_use_cases import (
    CriarClienteUseCase, BuscarClienteUseCase,
    AtualizarClienteUseCase, DeletarClienteUseCase,
    ListarClientesUseCase, ValidarClienteUseCase
)
from app.infrastructure.config.database import Database

router = APIRouter(prefix="/api/v1/customers")


async def get_database() -> Database:
    return Database()


# GET
@router.get("/", response_model=List[ClienteResponse])
async def listar_cliente(
    use_case=Depends(lambda: ListarClientesUseCase(Database))
):
    try:
        return await use_case.execute()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/search", response_model=ClienteResponse)
async def buscar_cliente(
    request: ClienteRequest,
    use_case=Depends(lambda: BuscarClienteUseCase(Database))
):
    try:
        return await use_case.execute(request.cpf)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/validate", response_model=ClienteResponse)
async def validar_cliente(
    request: ClienteRequest,
    use_case=Depends(lambda: ValidarClienteUseCase(Database))
):
    try:
        return await use_case.execute(request.cpf)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST
@router.post("/create", response_model=ClienteResponse)
async def criar_cliente(
    cliente_data: ClienteCreate,
    use_case=Depends(lambda: CriarClienteUseCase(Database))
):
    try:
        return await use_case.execute(cliente_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/update", response_model=ClienteResponse)
async def atualizar_cliente(
    cliente_data: ClienteCreate,
    use_case=Depends(lambda: AtualizarClienteUseCase(Database))
):
    try:
        return await use_case.execute(cliente_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/delete", response_model=ClienteDeletedResponse)
async def deletar_cliente(
    request: ClienteRequest,
    use_case=Depends(lambda: DeletarClienteUseCase(Database))
):
    try:
        return await use_case.execute(request.cpf)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
