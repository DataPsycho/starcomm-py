from .resource import create_app


def run():
    app = create_app()
    app.run(host='0.0.0.0', port='8080')