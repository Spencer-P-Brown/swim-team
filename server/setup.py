import os
if os.getenv('VBOX_MOUNTED'):
    del os.link

from setuptools import setup
from setuptools import find_packages

with open('README.md', 'r') as readmefile:
    README = readmefile.read()


setup(
    name='swimteam_training_app',
    version='0.1.0',
    # url='git@github.com:chamarthiraji/vehicles.git',
    description='Track injuries/training for swimming',
    long_description=README,
    packages=find_packages(exclude=['tests', 'build', 'dist', 'docs']),
    install_requires=[
        'flask',
        'flask_restless',
        'flask-cors',
        'Flask-Migrate',
        'Flask-SQLAlchemy',
        'PyMySQL',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'swimteam-run = swimteam_server.cmd.run:main',
            # 'vehicles-run-test = vehicles.cmd.run:main_test',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
