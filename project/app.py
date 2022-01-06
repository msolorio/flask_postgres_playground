from flask import Flask
from flask_migrate import Migrate
from .models import db
from .controllers.cats_bp import cats_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('project.config')

    db.init_app(app)

    migrate = Migrate(app, db)

    app.register_blueprint(cats_bp, url_prefix='/cats')

    @app.route('/')
    def index():
        return 'hello from index'


    return app