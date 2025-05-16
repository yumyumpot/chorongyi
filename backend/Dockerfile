FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY ./app /app/app

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
