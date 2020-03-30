from views.solution import verify_task


def setup_routes(app):
    app.router.add_post('/solution', verify_task)
