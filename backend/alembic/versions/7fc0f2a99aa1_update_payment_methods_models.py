"""Auto-generate migration scripts

Revision ID: 7fc0f2a99aa1
Revises: 44319e1ab4e7
Create Date: 2024-05-24 01:18:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = '7fc0f2a99aa1'
down_revision = '44319e1ab4e7'
branch_labels = None
depends_on = None


def upgrade():
    # 获取数据库连接
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)

    # 检查列是否存在
    columns = [col['name'] for col in inspector.get_columns('categories')]
    if 'is_active' not in columns:
        op.add_column('categories', sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.true()))


def downgrade():
    op.drop_column('categories', 'is_active')
