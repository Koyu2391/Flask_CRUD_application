from flask import Flask

app = Flask(__name__)

# Import and register the user blueprint
from controller.user_controller import user_blueprint
app.register_blueprint(user_blueprint)

@app.route('/')
def home():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)


