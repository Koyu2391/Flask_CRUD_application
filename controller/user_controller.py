from flask import request, jsonify
from model.user_model import user_model
from app import app


obj = user_model()

# for Create -> fahad
@app.route("/sign_up", methods=["POST"])
def create():
    return obj.create_c(request.get_json())

# for read -> nameera 
@app.route("/user/getall", methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()

#for update -> nameera 
@app.route("/user/update/<id>", methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(id)

#for Delete -> Fahad   
@app.route("/delete_user/<id>", methods=["DELETE"])
def delete(id):
    return obj.delete_d(id)

# Additional Feature For user login 
@app.route('/log_in', methods = ["POST"])
def user_login():
    return obj.login_l(request.get_json())