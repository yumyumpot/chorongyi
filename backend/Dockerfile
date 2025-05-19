FROM python:3.10-slim

WORKDIR /app

# pyproject.toml 먼저 복사해서 의존성 설치
COPY pyproject.toml poetry.lock /app/

# poetry 설치 및 의존성 설치
RUN pip install --upgrade pip && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# 나머지 소스 복사
COPY . /app

# PYTHONPATH 설정
ENV PYTHONPATH=/app

# 환경 변수로 dev/prod 구분 (기본값 prod)
ARG APP_ENV=prod
ENV APP_ENV=${APP_ENV}

# dev면 reload 실행, 아니면 prod 실행
CMD ["/bin/sh", "-c", "if [ \"$APP_ENV\" = \"dev\" ]; then uvicorn main:app --host 0.0.0.0 --port 8000 --reload; else uvicorn main:app --host 0.0.0.0 --port 8000; fi"]
