from setuptools import setup

setup(
    name="init_venv",
    version="1.0",
    description="Install necessary for olymp-system modules.",
    install_requires=[
        'aiohttp',
        'aiohttp_cors',
        'aiopg',
        'alembic',
        'marshmallow',
        'pyyaml',
        'docker',
        'pyjwt',
        'bcrypt'
    ]
)
