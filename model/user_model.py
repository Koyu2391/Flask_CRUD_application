import sqlite3
from flask import jsonify, make_response
from .user_create import create_user
from .user_login import login_user
from .user_delete import delete_user


class user_model:
    def __init__(self):
        self.db_name = "user.db"
        self._create_table()  # -> Remove ORM -> (Assigned to @herenamescode)

    # Fahad's Side of the work Includes -> (Create and Delete)

    def create_c(self, data):
        return create_user(self.cur, self.con, data)

    def delete_d(self, id):
        return delete_user(self.cur, self.con, id)

    def login_l(self, data): # Extra Login Feature 
        return login_user(self.cur, self.con, data)

    # End of the specified Work

    # READ
    def user_getall_model(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("SELECT * FROM user")
        result = cur.fetchall()
        con.close()

        if result:
            return jsonify({"payload": result})
        else:
            return jsonify({"message": "No data found"}), 404

    # UPDATE
    def user_update_model(self, data):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        try:
            cur.execute(
                "UPDATE user SET name=?, email=?, password=?, roll_batch=?, branch=? WHERE id=?",
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
            import traceback

            print("Update error:", e)
            traceback.print_exc()
            return make_response({"message": "UPDATE_FAILED", "error": str(e)}, 500)
