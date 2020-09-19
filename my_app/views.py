# Views at the end of Workshop 2

from my_app import app
from flask import render_template, request, redirect

name="Justin Yu"
facts = {"Birthday":"April 10th, 2000", "Favorite Color": "blue", "Favorite Hackathon": "HackMIT"}
posts = [{"title": "This is my 1st post!", "description": "this is my first description!"}]

name="Shirlyn"
facts = {"Birthday":"February 29, 1964", "Favorite Color": "blue", "Favorite Hackathon": "HackMIT"}
posts = [{"title": "This is my 1st post!", "description": "this is my first description!"}]

@app.route("/")
def index():
    return render_template("index.html", name=name, facts=facts, posts=posts)

@app.route("/change_name")
def change_name():
    global name
    new_name = request.args.get('name')
    name = new_name
    return redirect("/")

@app.route("/post", methods=["POST"])
def post():
    global posts
    if request.method == "POST":
        print(request)
        post_info = request.get_json()
        posts.append({"title": post_info["title"], "description": post_info["description"]})
    return redirect("/")
