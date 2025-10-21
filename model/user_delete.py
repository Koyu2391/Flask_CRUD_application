from flask import make_response


def delete_user(cur, con, id):
    try:
        cur.execute(f"DELETE FROM user WHERE id = {id}")
        con.commit()
    except Exception as e:
        return make_response({"message": f"Query Failed: {e}"}, 400)

    if cur.rowcount > 0:
        return make_response({"message": "User Deleted Succesfully"}, 200)
    else:
        return make_response({"message": "Nothing to Delete"})
