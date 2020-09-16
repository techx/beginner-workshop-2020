import os
from flask import Flask, session, request

app = Flask(__name__)

#load main config
app.config.from_pyfile('../config.py') 


import my_app.views