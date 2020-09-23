
from flask_script import Manager,Server
from flaskblog.models import Users
from flask_migrate import Migrate, MigrateCommand
from flaskblog import create_app,db

app = create_app("development")

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)



manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = Users)

if __name__ == '__main__':
    manager.run()
