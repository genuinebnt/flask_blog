from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return "Hello to index page"

    return app
