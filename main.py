from app.presentation.routers import flow_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(flow_router.router)
