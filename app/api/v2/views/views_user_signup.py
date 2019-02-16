from flask import make_response, jsonify, Blueprint,request
from app.api.v2.models.models_user_signup import user, db
from app.database_config import create_tables
v2= Blueprint('api_v2', __name__, url_prefix='/api/v2')
import ast
import json

users = db()
@v2.route('/home', methods=['GET'])
def home():
    make_response(jsonify({
        "status": 200,
        "message": "Politico enables citizens give their mandate to the type of leaders they need "


    }), 200)

@v2.route('/users',methods=['GET'])
def getusers():
    users = db.getAllUsers()
    return make_response(jsonify(users), 200)





#
# @v2.route('/auth/signup', methods=['POST'])
# def adduser():
#     json_data = request.get_json(force=True)
#     data=json.dumps(json_data)
#     if (json_data['type'] is not "") and (json_data["name"] is not ""):
#         datadict=ast.literal_eval(data)
#         name=datadict['name']
#         type=datadict['type']
#         if isinstance(name,str) and isinstance(type,str):
#             id = len(user) + 1
#             firstname = json_data["firstname"]
#             lastname = json_data["lastname"]
#             lastname = json_data["lastname"]
#             othername = json_data["othername"]
#             email = json_data["email"]
#             phoneNumber= json_data["phoneNumber"]
#             passportUrl = json_data["passportUrl"]
#             isAdmin = json_data["isAdmin"]
#
#             new_user = {
#                 "id":id,
#                 "firstname":firstname,
#                 "lastname": lastname,
#                 "othername":othername,
#                 "email":email,
#                 "phoneNumber":phoneNumber,
#                 "passportUrl":passportUrl,
#                 "isAdmin":isAdmin
#             }
#
#             print(new_user)
#             user.append(new_user)
#
#             return make_response(jsonify({
#                 "status": 201,
#                 "data": [new_user]
#             }), 201)
#         else:
#             return jsonify({"status":404,"Message":"Enter valid data"})
#
#
#     return make_response(jsonify({
#         "status": 401,
#         "message": "Missing required fields"
#     }))
#
#
#
#
#
#

if __name__ == "__main__":
    v2.run(debug=True)
