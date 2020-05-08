"""merge a6a and efc

Revision ID: d14a3fac17ff
Revises: b9ac368faaa3, 28901be7e869
Create Date: 2020-05-07 11:53:02.573522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd14a3fac17ff'
down_revision = ('b9ac368faaa3', '28901be7e869')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
