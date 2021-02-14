from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password): # used to check if the user exists and generate key /auth
    #user = username_table.get(username, None) # None is the default value 
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): # to compare strings with any encoding 
        return user

def identity(payload): # when end point is requested 
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
