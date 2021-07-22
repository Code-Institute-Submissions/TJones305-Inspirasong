import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get("MONGO_DBNAME")
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # CHECK IF USERNAME ALREADY EXSISTS IN DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists please choose another")
            return redirect(url_for("register"))

        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # PUT THE NEW USER INTO 'SESSION' COOKIE
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # CHECK IF USERNAME ALREADY EXSISTS IN DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ENSURED HASH PASSWORD MATCHES USER INPUT
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # INVALID PASSWORD
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # USERNAME DOESN'T EXIST
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # GET THE SESSION USER'S USERNAME FROM DB
    user = mongo.db.users.find_one({"username": session["user"]})
    print(user)
    username = user["username"]
    firstname = user["firstname"].capitalize()
    lastname = user["lastname"].capitalize()
    image = user["image"]

    if session["user"] == "adminuser":
        posts = list(mongo.db.posts.find
                     ().sort("id", 1))
        return render_template(
            "profile.html", username=username, posts=posts, image=image,
            firstname=firstname, lastname=lastname)

    elif session["user"]:
        posts = list(mongo.db.posts.find
                     ({"created_by": session["user"]}).sort("id", 1))

        return render_template(
            "profile.html", username=username, posts=posts, image=image,
            firstname=firstname, lastname=lastname)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # REMOVE USER FROM SESSION COOKIES
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("base"))


@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":

        post = {
            "song_name": request.form.get("song_name"),
            "artist_name": request.form.get("artist_name"),
            "albulm_name": request.form.get("albulm_name"),
            "genre_name": request.form.get("genre_name"),
            "sub_genre": request.form.get("sub_genre"),
            "post_description": request.form.get("post_description"),
            "post_date": request.form.get("post_date"),
            "created_by": session["user"]
        }
        mongo.db.posts.insert_one(post)
        flash("Post Successfully Created")
        return redirect(url_for("base"))

    genres = list(mongo.db.genre.find().sort("genre_name", 1))
    return render_template("create_post.html", genres=genres)


@app.route("/rock", methods=["GET", "POST"])
def rock():
    posts = list(mongo.db.posts.find({"genre_name": "Rock"}).sort("id", 1))
    return render_template("rock.html", posts=posts)


@app.route("/pop", methods=["GET", "POST"])
def pop():
    posts = list(mongo.db.posts.find({"genre_name": "Pop"}).sort("id", 1))
    return render_template("pop.html", posts=posts)


@app.route("/rap", methods=["GET", "POST"])
def rap():
    posts = list(mongo.db.posts.find({"genre_name": "Rap"}).sort("id", 1))
    return render_template("rap.html", posts=posts)


@app.route("/dance", methods=["GET", "POST"])
def dance():
    posts = list(mongo.db.posts.find({"genre_name": "Dance"}).sort("id", 1))
    return render_template("dance.html", posts=posts)


@app.route("/other", methods=["GET", "POST"])
def other():
    posts = list(mongo.db.posts.find({"genre_name": "Other"}).sort("id", 1))
    return render_template("other.html", posts=posts)


@app.route("/edit/<post_id>", methods=["GET", "POST"])
def edit(post_id):
    if request.method == "POST":
        submit = {
            "song_name": request.form.get("song_name"),
            "artist_name": request.form.get("artist_name"),
            "albulm_name": request.form.get("albulm_name"),
            "genre_name": request.form.get("genre_name"),
            "sub_genre": request.form.get("sub_genre"),
            "post_description": request.form.get("post_description"),
            "post_date": request.form.get("post_date"),
            "created_by": session["user"]
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
        flash("Post Has Been Updated")

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id,)})
    genres = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("edit.html", post=post, genres=genres)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id,)})
    flash("Post has been Removed")
    return redirect(url_for("profile"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(403)
def forbidden_page(e):
    return render_template("403.html"), 403


@app.errorhandler(410)
def page_not_exsist(e):
    return render_template("410.html"), 410


#   @app.errorhandler(Exception)
#   def handle_exception(e):
    # pass through HTTP errors
    #   if isinstance(e, HTTPException):
    #   return e
    # now you're handling non-HTTP exceptions only
    #   return render_template("500.html", e=e), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
