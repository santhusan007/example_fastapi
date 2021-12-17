"""add user table

Revision ID: de9f47c03c8b
Revises: baa3f6f89d73
Create Date: 2021-12-17 19:42:12.610897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de9f47c03c8b'
down_revision = 'baa3f6f89d73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table ('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                             server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email')
                    
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
