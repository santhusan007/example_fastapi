"""add last few columns to posts table

Revision ID: 776bfed932f1
Revises: adb94b4a6a0f
Create Date: 2021-12-18 04:01:38.351558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '776bfed932f1'
down_revision = 'adb94b4a6a0f'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column ('posts', sa.Column ('published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column ('posts',sa.Column ( 'created_at',sa.TIMESTAMP(timezone=True),nullable=False,
                             server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
