
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
virtualenv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python server.py
