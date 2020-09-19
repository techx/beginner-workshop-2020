import os

DEBUG=True

base = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False