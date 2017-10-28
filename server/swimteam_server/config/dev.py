from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os

TESTING = False
DEBUG = True

DB_PASSWORD = os.environ.get('SWIMTEAM_DB_PASSWORD')
print(DB_PASSWORD)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://swimteam:{db_password}@localhost/swimteamdb'.format(db_password=DB_PASSWORD)
SQLALCHEMY_TRACK_MODIFICATIONS = True
