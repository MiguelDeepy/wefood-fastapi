from fastapi import APIRouter, Depends, HTTPException
from app.domain.entities.produto import ProdutoCreate, ProdutoResponse
from app.application.user_cases.produto_use_cases import CriarProdutoUseCase, BuscarProdutoUseCase

router = APIRouter(prefix="/api/v1/produtos")


@router.post("/", response_model=ProdutoResponse)
async def criar_produto(
    produto_data: ProdutoCreate,
    use_case: CriarProdutoUseCase = Depends()
):
    try:
        return await use_case.execute(produto_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id}", response_model=ProdutoResponse)
async def buscar_produto(
    id: int,
    use_case: BuscarProdutoUseCase = Depends()
):
    produto = await use_case.execute(id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
