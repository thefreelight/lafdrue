from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
from pathlib import Path
import os

# 添加模型路径
sys.path.append(str(Path(__file__).resolve().parents[2]))

# 导入 Base 和所有模型
from backend.app.dependencies.database import Base
from backend.app.models import *

# Alembic 配置
config = context.config

# 设置数据库URL
database_url = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:123456@db:3306/lafdrue')
config.set_main_option('sqlalchemy.url', database_url)

# Python 日志配置
if config.config_file_name:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
