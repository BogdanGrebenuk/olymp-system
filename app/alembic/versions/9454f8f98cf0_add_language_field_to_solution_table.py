"""add language field to solution table

Revision ID: 9454f8f98cf0
Revises: 5972a93cea3b
Create Date: 2020-04-20 01:55:37.428203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9454f8f98cf0'
down_revision = '5972a93cea3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('solution', sa.Column('language', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('solution', 'language')
    # ### end Alembic commands ###
