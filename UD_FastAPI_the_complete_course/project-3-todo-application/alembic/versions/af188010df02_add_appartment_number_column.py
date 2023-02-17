"""add appartment number column

Revision ID: af188010df02
Revises: 730e7395e3a9
Create Date: 2023-02-13 11:56:57.589550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af188010df02'
down_revision = '730e7395e3a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
