"""Auto migration

Revision ID: 7a94ff1446c0
Revises: 1ad48e4458ed
Create Date: 2024-05-26 11:08:33.718038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a94ff1446c0'
down_revision: Union[str, None] = '1ad48e4458ed'
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
