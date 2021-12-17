"""add foreign key to post table

Revision ID: adb94b4a6a0f
Revises: de9f47c03c8b
Create Date: 2021-12-17 19:54:21.313981

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import false


# revision identifiers, used by Alembic.
revision = 'adb94b4a6a0f'
down_revision = 'de9f47c03c8b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key  (
                            'post_users_fk',source_table="posts",
                            referent_table="users",local_cols=['owner_id'],
                            remote_cols=['id'],ondelete='CASCADE'
                            )
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','ownert_id')
