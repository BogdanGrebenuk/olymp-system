import sqlalchemy as sa


metadata = sa.MetaData()


User = sa.Table(
    'user',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column('first_name', sa.Text, nullable=False),
    sa.Column('last_name', sa.Text, nullable=False),
    sa.Column('patronymic', sa.Text, nullable=False),
    sa.Column('email', sa.Text, nullable=False, unique=True),
    sa.Column('password', sa.Text, nullable=False),
    sa.Column('role', sa.Text, nullable=False)
)


Contest = sa.Table(
    'contest',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column('name', sa.Text, nullable=False),
    sa.Column('description', sa.Text, nullable=False),
    sa.Column('image_path', sa.Text),
    sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('max_teams', sa.Integer, nullable=True),
    sa.Column('max_participants_in_team', sa.Integer, nullable=False),
    sa.Column(
        'creator_id',
        sa.Text,
        sa.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
)


Team = sa.Table(
    'team',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column('name', sa.Text, nullable=False),
    sa.Column(
        'contest_id',
        sa.Text,
        sa.ForeignKey('contest.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    ),
    sa.Column(
        'trainer_id',
        sa.Text,
        sa.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
)


TeamMember = sa.Table(
    'team_member',
    metadata,
    sa.Column('id', sa.Text, primary_key=True),
    sa.Column(
        'user_id',
        sa.Text,
        sa.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    ),
    sa.Column(
        'team_id',
        sa.Text,
        sa.ForeignKey('team.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    ),
    sa.Column('status', sa.Text, nullable=False)
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
    sa.Column('name', sa.Text, nullable=False),
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
    sa.Column('is_passed', sa.Boolean, nullable=False, default=False),
    sa.Column(
        'user_id',
        sa.Text,
        sa.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    ),
    sa.Column(
        'team_id',
        sa.Text,
        sa.ForeignKey('team.id', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
)
