# Views at the end of Workshop 2

from my_app import app, db
from flask import render_template, request, redirect
from my_app.models import Fact, Post

name="My Name"
facts = {"Birthday":"September 18th, 2020", "Favorite Color": "blue", "Favorite Hackathon": "HackMIT"}
posts = []

@app.route("/")
def index():
    """
    [GET]: 
        - args: none
        - return: index.html
    """

    db_facts = Fact.query.all()

    # if nothing in the db, populate it
    if len(db_facts) == 0: 
        global facts 
        for fact in facts:
            new_fact = Fact(name=fact, value=facts[fact])
            db.session.add(new_fact)
        db.session.commit()
        db_facts = Fact.query.all()

    fact_dict = {fact.name: fact.value for fact in db_facts}

    db_posts = Post.query.all()
    post_list = [{"title": post.title, "description": post.description} for post in db_posts]

    return render_template("index.html", name=name, facts=fact_dict, posts=post_list)

@app.route("/change_name")
def change_name():
    """
    [GET]: 
        - args: name=<str>
        - return: index.html
    """
    global name
    new_name = request.args.get('name')
    name = new_name
    return redirect("/")

@app.route("/post", methods=["POST"])
def post():
    """
    [POST]: 
        - args: none
        - body: 
            {"title": <str>, "description":<str> }
        - return: index.html
    """
    if request.method == "POST":
        print(request)
        post_info = request.get_json()
        new_post = Post(title=post_info['title'], description=post_info['description'])
        db.session.add(new_post)
        db.session.commit()
    return redirect("/")

@app.route("/change_facts", methods=["POST"])
def change_facts():
    """
    [POST]: 
        - args: none
        - body: 
            {"fact_name": <str>, "fact_name2":<str> ... }
        - return: index.html
    """
    if request.method == "POST":
        change_facts = request.get_json()
        for key, value in change_facts.items():
            if Fact.query.filter(Fact.name == key).first() is None:
                new_fact = Fact(name=key, value=value)
                db.session.add(new_fact)
        db.session.commit()
    return redirect("/")
