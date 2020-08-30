from setuptools import setup


setup(
    name="olymp-system",
    version="0.1",
    description="system for conducting olympiads",
    install_requires=[
        'aiohttp',
        'aiohttp_cors',
        'aiopg',
        'alembic',
        'marshmallow',
        'pyyaml',
        'docker',
        'pyjwt',
        'bcrypt',
        'sqlalchemy',
        'python-dateutil',
        'dependency-injector'
    ]
)
