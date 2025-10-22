from flask import Blueprint, request, jsonify
from model.user_model import user_model
from app import app

user_blueprint = Blueprint("user_blueprint", __name__)
obj = user_model()

# for Create -> fahad
@app.route("/sign_up", methods=["POST"])
def create():
    return obj.create_c(request.get_json())

# for read -> nameera 
@user_blueprint.route("/user/getall", methods=["GET"])
def user_getall_controller():
    data = request.json
    return obj.read_r(data)

#for update -> nameera 
@user_blueprint.route("/user/update", methods=["PUT"])
def user_update_controller():
    data = request.json
    return obj.update_u(data)

#for Delete -> Fahad   
@app.route("/delete_user/<id>", methods=["DELETE"])
def delete(id):
    return obj.delete_d(id)

# Additional Feature For user login 
@app.route('/log_in', methods = ["POST"])
def user_login():
    return obj.login_l(request.get_json())