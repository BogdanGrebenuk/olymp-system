from views.solution import verify_task
from views.contest import create_contest
from views.task import create_task


def setup_routes(app):
    app.router.add_post('/contest', create_contest)
    app.router.add_post('/solution', verify_task)
    app.router.add_post('/task', create_task)
