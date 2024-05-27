"""Auto migration

Revision ID: 779f5aa95741
Revises: 7a94ff1446c0
Create Date: 2024-05-26 15:09:24.944005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '779f5aa95741'
down_revision: Union[str, None] = '7a94ff1446c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('language', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'language')
    # ### end Alembic commands ###