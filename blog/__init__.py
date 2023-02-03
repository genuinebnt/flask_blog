from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite')  # store db file in instance path
    )

    # flask doesn't create instance_path automatically. It is required since db file will be stored there
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return "Hello to index page"

    from . import db
    db.init_app(app)

    return app
