from application import generate_application, MIGRATE
from flask_migrate import MigrateCommand
from flask_script import Manager

# if you want to upgrade to new flask CLI over this stuff
#   https://blog.miguelgrinberg.com/post/migrating-from-flask-script-to-the-new-flask-cli

MANAGER = Manager(generate_application())
MANAGER.add_option("-c", "--config", dest="config_module", required=False)
MANAGER.add_command('db', MigrateCommand)
MANAGER.run()
