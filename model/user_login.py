from flask import make_response


def login_user(cur, con, data):
        UserId = data['email']
        password = data['pass']

        try: 
            query = "SELECT id, name, roll_batch, branch, email FROM user WHERE email = ? AND pass = ?"
            cur.execute(query, (UserId, password))
            user = cur.fetchone()
            
            if user:
                user_data = {
                    "id": user[0],
                    "name": user[1],
                    "roll_batch": user[2],
                    "branch": user[3],
                    "email": user[4]
                }
                return make_response({"message": "Login Successful", "user": user_data}, 200)
            else:
                return make_response({"message": "Invalid Credentials"}, 400)
        except Exception as e:
            return {"status": "error", "message": str(e)}