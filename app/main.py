"""Точка входа FastAPI: приложение, маршруты, проверка работоспособности."""
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="СМД API",
    description=(
        "REST-интерфейс инструмента «Средство моделирования данных» (вариант № 23): "
        "проекты сравнения, сравнение схем БД, генерация скриптов миграции."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health", response_model=None, tags=["health"])
def health(db: Session = Depends(get_db)) -> JSONResponse:
    """Проверка работоспособности: доступность приложения и БД (для healthcheck)."""
    try:
        db.execute(text("SELECT 1"))
        database_status = "ok"
    except Exception:  # noqa: BLE001 - healthcheck обязан пережить недоступность БД
        database_status = "unavailable"
    status_code = 200 if database_status == "ok" else 503
    return JSONResponse(status_code=status_code, content={"status": "ok", "database": database_status})
