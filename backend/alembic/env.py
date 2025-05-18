import os
import sys
from logging.config import fileConfig
from alembic import context

# 🔧 dotenv 로딩 추가
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# FastAPI 앱 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Base metadata 불러오기
from app.db.base import Base
from app.db.session import engine

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Alembic이 인식할 대상 metadata
target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
