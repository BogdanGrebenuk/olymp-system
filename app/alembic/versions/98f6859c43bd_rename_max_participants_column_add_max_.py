"""rename max_participants column, add max_teams column

Revision ID: 98f6859c43bd
Revises: 2bb738f60f10
Create Date: 2020-05-09 03:20:55.518319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98f6859c43bd'
down_revision = '2bb738f60f10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contest', sa.Column('max_participants_in_team', sa.Integer(), nullable=False))
    op.add_column('contest', sa.Column('max_teams', sa.Integer(), nullable=True))
    op.drop_column('contest', 'max_participants')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contest', sa.Column('max_participants', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('contest', 'max_teams')
    op.drop_column('contest', 'max_participants_in_team')
    # ### end Alembic commands ###