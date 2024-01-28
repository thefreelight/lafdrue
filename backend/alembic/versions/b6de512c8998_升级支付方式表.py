"""update order models

Revision ID: 44319e1ab4e7
Revises: b6de512c8998
Create Date: 2024-01-28 06:29:46.681344

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import ENUM

# revision identifiers, used by Alembic.
revision = '44319e1ab4e7'
down_revision = 'b6de512c8998'
branch_labels = None
depends_on = None


def upgrade():
    # 修改 orders 表结构
    with op.batch_alter_table('orders') as batch_op:
        batch_op.add_column(sa.Column('card_info', sa.Text(), nullable=True))

    # 修改 order_items 表结构
    with op.batch_alter_table('order_items') as batch_op:
        batch_op.add_column(sa.Column('product_name', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('shipping_method', sa.String(length=50), nullable=True))


def downgrade():
    # 撤销 orders 表的修改
    with op.batch_alter_table('orders') as batch_op:
        batch_op.drop_column('card_info')
        batch_op.drop_column('handling_fee')
        batch_op.drop_column('shipping_status')
        batch_op.drop_column('payment_status')
        batch_op.drop_column('client_ip')
        batch_op.drop_column('payment_method')
        batch_op.drop_column('role')
        batch_op.drop_column('order_number')

    # 撤销 order_items 表的修改
    with op.batch_alter_table('order_items') as batch_op:
        batch_op.drop_column('shipping_method')
        batch_op.drop_column('product_name')
