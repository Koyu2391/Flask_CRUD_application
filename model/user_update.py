from flask import make_response
import sqlite3
    
def update_user(con, data, id):
        cur = con.cursor()
        try:
            cur.execute(
                f"UPDATE user SET name=?, email=?, password=?, roll_batch=?, branch=? WHERE id={id}",
                (
                    data["name"],
                    data["email"],
                    data["password"],
                    data["roll_batch"],
                    data.get("branch"),
                    data["id"],
                ),
            )
            con.commit()

            if cur.rowcount > 0:
                return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)
            else:
                return make_response({"message": "NOTHING_TO_UPDATE"}, 204)
        except Exception as e:
            return make_response({"message": "UPDATE_FAILED", "error": str(e)}, 500)