import os

DEBUG=True
base = os.path.abspath(os.path.dirname(__file__))
# create a file called 'app.db' in your repo that holds the database
# delete this file to clear the database
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base, 'app.db') 
SQLALCHEMY_TRACK_MODIFICATIONS = False