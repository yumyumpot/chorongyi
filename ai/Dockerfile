FROM python:3.10

RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://pixi.sh/install.sh | bash && \
    /root/.pixi/bin/pixi --version

WORKDIR /app

COPY pixi.toml pixi.lock ./
RUN /root/.pixi/bin/pixi install

COPY . .

CMD ["/root/.pixi/bin/pixi", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]