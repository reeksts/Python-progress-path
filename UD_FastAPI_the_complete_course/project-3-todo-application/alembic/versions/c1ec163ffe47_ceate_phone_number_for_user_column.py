"""ceate phone number for user column

Revision ID: c1ec163ffe47
Revises: 
Create Date: 2023-02-12 21:45:19.360096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1ec163ffe47'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
