"""create address_id to users

Revision ID: 730e7395e3a9
Revises: dbdbbc23b46a
Create Date: 2023-02-12 22:29:19.034795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '730e7395e3a9'
down_revision = 'dbdbbc23b46a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'address_users_fk',
        source_table='users',
        referent_table='address',
        local_cols=['address_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name='users')
    op.drop_column('users', 'address_id')
