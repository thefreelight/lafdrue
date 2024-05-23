from alembic import op
import sqlalchemy as sa

revision = '44319e1ab4e7'  # 替换为您想要的修订版本号
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('payment_methods', sa.Column('payment_method', sa.String(length=50), nullable=True))

def downgrade():
    op.drop_column('payment_methods', 'payment_method')
