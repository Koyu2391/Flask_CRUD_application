from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile.html")
def userProf():
    return render_template("profile.html")


@app.route("/login.html")
def user_log():
    return render_template("login.html")


@app.route("/signup.html")
def user_sig():
    return render_template("signup.html")


from model.user_create import create_user
from model.user_delete import delete_user
from model.user_login import login_user
from model.user_update import update_user
from model.user_read import read_user
from controller import user_controller  


if __name__ == "__main__":
    app.run(debug=True)
