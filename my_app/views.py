from my_app import app
from flask import render_template, request, redirect
import requests

@app.route("/")
def index():
    return "Hello world!"