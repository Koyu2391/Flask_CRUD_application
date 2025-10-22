from flask import jsonify
import sqlite3

def read_user(db_name):
    con = sqlite3.connect(db_name)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    result = [dict(row) for row in rows]
    con.close()

    if result:
        return jsonify({"database": result})
    else:
        return jsonify({"message": "No data found"}), 404