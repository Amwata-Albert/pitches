from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from config import config_options
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask import Flask, render_template, request



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_options[config_class])

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.main.routes import main
    from flaskblog.posts.routes import posts
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    # configure UploadSet
    configure_uploads(app, photos)
    #db.create_all()

    return app
