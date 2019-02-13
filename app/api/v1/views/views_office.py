from flask import make_response, jsonify, Blueprint,request
from app.api.v1.models.models_office import offices
v1= Blueprint('api_v1', __name__, url_prefix='/api/v1')
import ast
import json

@v1.route('/home', methods=['GET'])
def home():
    make_response(jsonify({
        "status": 200,
        "message": "Politico enables citizens give their mandate to the type of leaders they need "


    }), 200)

@v1.route("/offices",methods=['GET'])
def getAllOffices():
    return make_response(jsonify(offices), 200)


@v1.route("/offices/<officeID>",methods=['GET'])
## this is a method to get a specific office
def getOffice(officeID):
    try:
        for office in offices:
            print(type(office["id"]))
            if office["id"] == int(officeID):
                return make_response(jsonify(office), 200)

        return make_response(jsonify({
            "code": 404,
            "message": "Could not find office with id {} kindly check it again".format(officeID)
        }), 404)
    except:
        return jsonify({"status": 400}, {"message": "You have entered invalid office ID"})




@v1.route("/offices", methods=['POST'])
def addOffice():
    json_data = request.get_json(force=True)
    data=json.dumps(json_data)
    datadict=ast.literal_eval(data)
    print (type(datadict))
    print(datadict)


    id = len(offices)+1
    office_type = json_data["type"]
    office_name = json_data["name"]

    new_office = {
        "id": id,
        "type": office_type,
        "name": office_name
    
    }

    print(new_office)
    offices.append(new_office)

    return make_response(jsonify({
        "status": 201,
        "data": [new_office]
    }), 201)


@v1.route("/offices/<officeID>", methods=['DELETE'])
def deleteOffice(officeID):
    # print(offices)
    # print(type(officeID))
    for office in offices:
        if office["id"] == int(officeID):
            offices.remove(office)
            return make_response(jsonify({
                "status": 200,
                "data": "the office has been deleted successfully"
            }), 200)

    return make_response(jsonify({
        "status": 404,
        "error": "could not find office with ID {}".format(officeID)
    }),404)
# @v1.route('/offices/<officeID>',methods=['PATCH'])
# def party_update(officeID):
#     for office in offices:
#         if office['id'] == int(officeID):
#             data = request.get_json()
#             # new_name = data['name']
#             print(data)
#             office['name'] = data['name']
#             return make_response(jsonify({
#                 "status": 200,
#                 "data": "updated  the party with office ID {} ".format(officeID)
#             }), 200)
#         elif office in offices:
#             return "Office Already exist"
#         else:
#             update_office = {
#                 "name": office['name']
#
#             }
#             office.append(update_office)
#             return make_response(jsonify({
#                 "status": 200,
#                 "data": [update_office]
#             }), 200)



if __name__ == "__main__":
    v1.run(debug=True)
