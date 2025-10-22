from flask import make_response

def update_user(cur, con, data, id):
    try:
        cur.execute(
            "UPDATE user SET name=?, email=?, roll_batch=?, branch=? WHERE id=?",
            (
                data["name"],
                data["email"],
                data["roll_batch"],
                data.get("branch"),
                id,
            ),
        )
        con.commit()

        if cur.rowcount > 0:
            return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)
        else:
            return make_response({"message": "NOTHING_TO_UPDATE"}, 204)
    except Exception as e:
        return make_response({"message": "UPDATE_FAILED", "error": str(e)}, 500)
