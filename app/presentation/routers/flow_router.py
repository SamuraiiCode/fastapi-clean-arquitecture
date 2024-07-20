from fastapi import APIRouter
from app.application.dtos.flow_dto import FlowDto

router = APIRouter(prefix="/CreateFlow")


@router.get("/")
def read_root():
    return {"Hello": "Routers"}

@router.post("/")
def read_root(request : FlowDto):
    return request
