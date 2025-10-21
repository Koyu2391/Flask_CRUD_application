from flask import make_response


def create_user(cur, con, data):
        try:
            cur.execute(
                f"""INSERT INTO user (name, email, pass, roll_batch, branch)
                VALUES ('{data['name']}', '{data['email']}', '{data['pass']}', '{data['roll_batch']}', '{data['branch']}')"""
            )
            con.commit()
            return make_response(
                {"message": f"{data['name']} as user added succesfully"}, 200
            )
        except Exception as e:
            return make_response({"message": f"Query Failed: {e}"}, 400)