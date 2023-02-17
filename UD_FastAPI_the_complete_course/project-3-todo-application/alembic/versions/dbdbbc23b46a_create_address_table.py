"""create address table

Revision ID: dbdbbc23b46a
Revises: c1ec163ffe47
Create Date: 2023-02-12 22:17:54.134992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbdbbc23b46a'
down_revision = 'c1ec163ffe47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'address',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('address1', sa.String(), nullable=False),
        sa.Column('address2', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String, nullable=False),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('postalcode', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('address')
