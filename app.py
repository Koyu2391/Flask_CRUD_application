from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Import and register the user blueprint
from controller.user_controller import user_blueprint
app.register_blueprint(user_blueprint)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/profile.html')
def userProf():
    return render_template("profile.html")

@app.route('/login.html')
def user_log():
    return render_template("login.html")

@app.route('/signup.html')
def user_sig():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=True)


