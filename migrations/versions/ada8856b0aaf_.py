"""empty message

Revision ID: ada8856b0aaf
Revises: 09fb2e238b73
Create Date: 2021-04-27 09:16:39.191411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ada8856b0aaf'
down_revision = '09fb2e238b73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image')
    op.drop_column('post', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
