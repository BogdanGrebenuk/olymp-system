from views.solution import verify_task
from views.contest import (
    create_contest,
    get_contests
)
from views.task import (
    create_task,
    get_tasks,
    get_task
)


def setup_routes(app):
    app.router.add_get('/api/contests', get_contests)
    app.router.add_post('/api/contests', create_contest)

    app.router.add_get('/api/contests/{contest_id}/tasks', get_tasks)
    app.router.add_get('/api/contests/{contest_id}/tasks/{task_id}', get_task)
    app.router.add_post('/api/tasks', create_task)

    app.router.add_post('/api/solutions', verify_task)

