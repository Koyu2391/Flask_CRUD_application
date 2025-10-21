from flask import Blueprint, request, jsonify
from model.user_model import user_model

user_blueprint = Blueprint("user_blueprint", __name__)
obj = user_model()

# for read 
@user_blueprint.route("/user/getall", methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()

    #for Create -> fahad
    
    #for Delete -> Fahad


# for update 
@user_blueprint.route("/user/update", methods=["PUT"])
def user_update_controller():
    user_id = request.form.get("id")
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    roll_batch = request.form.get("roll_batch")
    branch = request.form.get("branch") 

    print("Form data:", request.form.to_dict()) 

    if not user_id or not name or not email or not password or not roll_batch:
        return jsonify({"error": "Missing id, name, email, password, or roll_batch"}), 400
    
    data = {
        "id": user_id,
        "name": name,
        "email": email,
        "password": password,
        "roll_batch": roll_batch,
        "branch": branch  
    }

    return obj.user_update_model(data)



