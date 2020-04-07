"""create contest, task, taskio and solution tables

Revision ID: 5972a93cea3b
Revises: 
Create Date: 2020-04-07 21:36:37.291679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5972a93cea3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contest',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('name', sa.Text, nullable=False)
    )
    op.create_table(
        'task',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column(
            'contest_id',
            sa.Integer,
            sa.ForeignKey('contest.id', onupdate="CASCADE", ondelete="CASCADE"),
            nullable=False
        ),
        sa.Column(
            'description', sa.Text, nullable=False
        ),
        sa.Column('max_cpu_time', sa.Integer, nullable=False),
        sa.Column('max_memory', sa.Integer, nullable=False)
    )

    op.create_table(
        'task_io',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column(
            'task_id',
            sa.Integer,
            sa.ForeignKey('task.id', onupdate="CASCADE", ondelete="CASCADE"),
            nullable=False
        ),
        sa.Column('input', sa.Text, nullable=False),
        sa.Column('output', sa.Text, nullable=False)
    )

    op.create_table(
        'solution',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column(
            'task_id',
            sa.Integer,
            sa.ForeignKey('task.id', onupdate="CASCADE", ondelete="CASCADE"),
            nullable=False
        ),
        sa.Column('path', sa.Text, nullable=False)
    )


def downgrade():
    op.drop_table('solution')
    op.drop_table('task_io')
    op.drop_table('task')
    op.drop_table('contest')
