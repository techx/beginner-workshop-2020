import os

DEBUG=True
base = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base, 'app.db') # create a file called 'app.db' in your repo that holds the database
SQLALCHEMY_TRACK_MODIFICATIONS = False