import sqlite3
from flask import jsonify, make_response
from .user_create import create_user
from .user_login import login_user
from .user_delete import delete_user
from .user_read import read_user
from .user_update import update_user

class user_model:
    def __init__(self):
        try:
            self.db_name = "geeky_macet.db"
            self.con = sqlite3.connect(self.db_name, check_same_thread=False)
            self.con.row_factory = sqlite3.Row
            self.cur = self.con.cursor()
            print("Sql Connection Estd")
        except Exception as e:
            print(f"Some Error occured {e}")

# Fahad's Side of the work Includes -> (Create and Delete)

    def create_c(self, data):
        return create_user(self.cur, self.con, data)

    def delete_d(self, id):
        return delete_user(self.cur, self.con, id)
    
# Extra Login Feature
    def login_l(self, data):  
        return login_user(self.cur, self.con, data)

    
# Nameera's side of the work includes READ and UPDATE
    def read_r(self):
        return read_user(self.cur, self.con)
    
    def update_u(self, data):
        return update_user(self.con, data)