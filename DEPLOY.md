# **DEPLOYMENT INSTRUCTIONS**

**Requirements:**

- python3.7
- postgres10


- Make sure there is UTC timezone in your db.

    - edit  `/etc/postgresql/10/main/postgresql.conf` file and place `timezone='UTC'`
    - restart postgresql service: `sudo service postgresql restart` 

- In the project's root (olymp-system) create venv and activate it:

    `python3.7 -m venv venv`

    `source venv/bin/activate`

- Create folders:

    - `olymp-system/public`

    - `olymp-system/var/logs`

- Install packages (in `olymp-system`): `pip install .`

- Init db (in `olymp-system`): `PYTHONPATH='.' python app/console/init_db.py`

- Run migrations (in `olymp-system/app`): `PYTHONPATH='..' alembic upgrade head`

- Run server (in `olymp-system`): `python -m app`
