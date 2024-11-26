from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from app.database import Base, DATABASE_URL
from app.models import Task

# Alembic Config object
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for autogenerate support
target_metadata = Base.metadata

# Convert async database URL to a synchronous one
SYNC_DATABASE_URL = DATABASE_URL.replace("asyncpg", "psycopg2")

def run_migrations_online():
    """Run migrations in online mode with a synchronous engine."""
    connectable = create_engine(SYNC_DATABASE_URL, echo=True)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,  # Enable batch mode for migrations
        )
        with context.begin_transaction():
            context.run_migrations()

# Entry point
if context.is_offline_mode():
    raise RuntimeError("Offline migrations are not supported with async engines")
else:
    run_migrations_online()
