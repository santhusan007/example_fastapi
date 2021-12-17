"""add content column to post table

Revision ID: baa3f6f89d73
Revises: a05a2f921c91
Create Date: 2021-12-17 19:35:59.634970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baa3f6f89d73'
down_revision = 'a05a2f921c91'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column("posts",'content')
    pass
