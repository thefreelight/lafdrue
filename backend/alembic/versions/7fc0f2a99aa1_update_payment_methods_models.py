"""update payment_methods  models

Revision ID: 7fc0f2a99aa1
Revises: 44319e1ab4e7
Create Date: 2024-01-28 17:06:57.215780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '7fc0f2a99aa1'
down_revision: Union[str, None] = '44319e1ab4e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.add_column('payment_methods', sa.Column('payment_method', sa.String(length=50), nullable=True))

def downgrade():
    op.drop_column('payment_methods', 'payment_method')
