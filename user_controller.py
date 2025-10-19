from flask import Blueprint, request, jsonify
from model.user_model import user_model

user_blueprint = Blueprint("user_blueprint", __name__)
obj = user_model()

# for read 
@user_blueprint.route("/user/getall", methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()

# for create 
@user_blueprint.route("/user/addone", methods=["POST"])
def user_addone_controller():
    name = request.form.get("name")
    email = request.form.get("email")

    print("Received name:", name)
    print("Received email:", email)
    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400

    success = obj.user_addone_model(name, email)
    if success:
        return jsonify({"message": "User added successfully!"}), 201
    else:
        return jsonify({"error": "Failed to add user"}), 500


# for update 
@user_blueprint.route("/user/update", methods=["PUT"])
def user_update_controller():
    user_id = request.form.get("id")
    name = request.form.get("name")
    email = request.form.get("email")

    print("Form data:", request.form.to_dict())

    if not user_id or not name or not email:
        return jsonify({"error": "Missing id, name, or email"}), 400

    data = {
        "id": user_id,
        "name": name,
        "email": email
    }

    return obj.user_update_model(data)




    

