# **DEPLOYMENT INSTRUCTIONS**

**Requirements:**

- python3.7
- postgres10

Make sure there is UTC timezone in your db.

Edit  `/etc/postgresql/10/main/postgresql.conf` file and place `timezone='UTC'`, then restart postgresql service

`sudo service postgresql restart` 

In the project root create venv and activate it:

`python3.7 -m venv venv`

`source venv/bin/activate`

Install packages:

`pip install .`

Init db:

`python app/init_db.py`


Run migrations (set `PYTHONPATH='.'` before ):

`alembic upgrade head`

Run server:

`cd app`

`python main.py`