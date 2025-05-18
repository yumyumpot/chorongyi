FROM python:3.10-slim

WORKDIR /app

# 먼저 pyproject.toml과 poetry.lock만 복사 (의존성 설치를 위해)
COPY pyproject.toml poetry.lock /app/

# poetry 설치 및 의존성 설치
RUN pip install --upgrade pip && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# 이제 나머지 소스 코드 복사
COPY . /app

# PYTHONPATH 환경 변수 설정 (app 폴더를 패키지 경로로 인식)
ENV PYTHONPATH=/app

# uvicorn으로 앱 실행 (app.main:app가 아닌 main:app 사용하시는 경우 main:app)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
