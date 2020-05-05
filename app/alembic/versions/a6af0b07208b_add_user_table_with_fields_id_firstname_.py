"""add user table with fields: id, firstname, lastname, patronymic, salt, password

Revision ID: a6af0b07208b
Revises: a50b0a4fcf6a
Create Date: 2020-05-05 23:14:55.245048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6af0b07208b'
down_revision = 'a50b0a4fcf6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('firstname', sa.Text(), nullable=False),
    sa.Column('lastname', sa.Text(), nullable=False),
    sa.Column('patronymic', sa.Text(), nullable=False),
    sa.Column('salt', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
