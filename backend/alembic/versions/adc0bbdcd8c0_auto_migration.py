"""Auto migration

Revision ID: adc0bbdcd8c0
Revises: 2d4fde8b6e22
Create Date: 2024-05-24 16:11:16.555922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adc0bbdcd8c0'
down_revision: Union[str, None] = '2d4fde8b6e22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###