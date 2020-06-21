import os
import unittest
import datetime
import time

from threading import Thread

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist, record, application, developer, function, favorites, contact

from app.main.process import dev_list_process, dev_info_app_list_process, app_info_process, app_plus_process, app_fnct_process
from app.main.process.dev_list_process import dev_list_process
from app.main.process.dev_info_app_list_process import dev_info_app_list_process
from app.main.process.app_info_process import app_info_process
from app.main.process.app_plus_process import app_plus_process
from app.main.process.app_fnct_process import app_fnct_process

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
        app.run(host='0.0.0.0')

@manager.command
def test():
        """ runs the unit tests """
        tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.wasSuccessful():
                return 0
        return 1

@manager.command
def data():
        """ automatic data update processing """
        while True:
                now = datetime.datetime.now()
                now = str(now)[11:19]
                if now == "00:00:00":
                        with app.app_context():
                                dev_list_process()
                                dev_info_app_list_process()
                                app_info_process()
                                app_plus_process()
                                app_fnct_process()
                else :
                        print(now)
                        time.sleep(0.5)

dpthread = Thread(target = data)
dpthread.daemon = True
dpthread.start()

if __name__ == '__main__':
        manager.run()
