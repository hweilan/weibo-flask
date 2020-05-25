import os

from app import create_app, db
from app.models import User, Role, Post
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

CONFIGURE_MODE = os.environ.get('FLASK_MODE') or 'heroku'

app = create_app(CONFIGURE_MODE)
manager = Manager(app)
migrate = Migrate(app, db)

"""db:数据库,app:flask框架"""
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def deploy():
    from flask_migrate import upgrade
    upgrade()


if __name__ == "__main__":
    manager.run()
