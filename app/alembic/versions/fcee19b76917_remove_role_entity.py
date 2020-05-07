"""remove role entity

Revision ID: fcee19b76917
Revises: d14a3fac17ff
Create Date: 2020-05-07 12:09:38.530946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcee19b76917'
down_revision = 'd14a3fac17ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_role_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    op.drop_table('role')
    op.add_column('user', sa.Column('role', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
        sa.Column('id', sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column('role', sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='role_pkey')
    )
    op.add_column('user', sa.Column('role_id', sa.TEXT(), autoincrement=False, nullable=False))
    op.create_foreign_key('user_role_id_fkey', 'user', 'role', ['role_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('user', 'role')
    # ### end Alembic commands ###
