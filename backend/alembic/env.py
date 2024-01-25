from logging.config import fileConfig
from sqlalchemy import create_engine,engine_from_config
from sqlalchemy import pool
from sqlalchemy_utils import database_exists, create_database
from alembic import context
import sys
from pathlib import Path
import os
# 现在可以使用绝对导入

# 这是一个很重要的步骤，它告诉 Alembic 去哪里找到模型
sys.path.append(str(Path(__file__).resolve().parents[2]))
from backend.app.dependencies.database import Base


# 从配置中获取 URL
config = context.config
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))
url = config.get_main_option("sqlalchemy.url")

# 创建引擎并创建数据库（如果不存在）
engine = create_engine(url)
if not database_exists(engine.url):
    create_database(engine.url)

# 如果存在ini文件，则为Python日志配置
if config.config_file_name is not None:
    fileConfig(config.config_file_name)



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
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
