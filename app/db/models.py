import sqlalchemy as sa


metadata = sa.MetaData()


Contest = sa.Table(
    'contest',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column('name', sa.Text, nullable=False),
    sa.Column('description', sa.Text, nullable=False)
)


Task = sa.Table(
    'task',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column(
        'contest_id',
        sa.Text,
        sa.ForeignKey('contest.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    ),
    sa.Column(
        'description', sa.Text, nullable=False
    ),
    sa.Column('max_cpu_time', sa.Integer, nullable=False),
    sa.Column('max_memory', sa.Integer, nullable=False)
)


TaskIO = sa.Table(
    'task_io',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column(
        'task_id',
        sa.Text,
        sa.ForeignKey('task.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    ),
    sa.Column('input', sa.Text, nullable=False),
    sa.Column('output', sa.Text, nullable=False)
)


Solution = sa.Table(
    'solution',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column(
        'task_id',
        sa.Text,
        sa.ForeignKey('task.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    ),
    sa.Column('path', sa.Text, nullable=False),
    sa.Column('language', sa.Text, nullable=False),
    sa.Column('is_passed', sa.Boolean, nullable=False, default=False)
)
