# СМД API — Средство моделирования данных (вариант № 23)

REST-интерфейс инструмента сравнения схем БД и генерации миграционных скриптов.
ЛР № 3 по дисциплине «Технологии разработки программных средств» (МГТУ «СТАНКИН»).

Стек: Python 3.10+, FastAPI, SQLAlchemy 2.x, PostgreSQL 16, Docker, GitHub Actions.

## Запуск

```bash
docker compose up --build
# Swagger UI: http://localhost:8000/docs
# Healthcheck: http://localhost:8000/api/health
```

Без Docker (нужен PostgreSQL, переменная `DATABASE_URL`):

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Тесты

```bash
pip install -r requirements-dev.txt
pytest
```
