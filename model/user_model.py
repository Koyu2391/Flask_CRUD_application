import sqlite3
from flask import jsonify, make_response

class user_model:
    def __init__(self):
        self.db_name = "user.db"
        self._create_table()

    def _create_table(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                pass TEXT NOT NULL, 
                roll_batch NOT NULL,
                branch NOT NULL
                
            )
        """)
        con.commit()
        con.close()

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

    # CREATE
    def user_addone_model(self, name, email):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO user(name, email) VALUES(?, ?)", (name, email))
            con.commit()
            return True
        except Exception as e:
            print("Insert error:", e)
            return False
        finally:
            con.close()

    # UPDATE
    def user_update_model(self, data):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        try:
            cur.execute("UPDATE user SET name=?, email=? WHERE id=?", 
                        (data["name"], data["email"], data["id"]))
            con.commit()

            if cur.rowcount > 0:
                return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)
            else:
                return make_response({"message": "NOTHING_TO_UPDATE"}, 204)
        except Exception as e:
            print("Update error:", e)
            return make_response({"message": "UPDATE_FAILED"}, 500)
        finally:
            con.close()
