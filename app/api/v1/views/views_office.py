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
    return jsonify({"data": offices, "status": 200}), 200


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
    if (json_data['type'] is not "") and (json_data["name"] is not ""):
        datadict=ast.literal_eval(data)
        name=datadict['name']
        type=datadict['type']
        id = len(offices) + 1
        office_type = json_data["type"]
        office_name = json_data["name"]
        if isinstance(name,str) and isinstance(type,str):
            for office in offices:
                if office['name'] !=name :
                    continue
                else:
                    return jsonify({
                        "error":"{} already exist".format(name),
                        "status":409
                    }),409


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

        else:
            return jsonify({"status":404,"Message":"Enter valid data"})


    return make_response(jsonify({
        "status": 401,
        "message": "Missing required fields"
    }))


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




if __name__ == "__main__":
    v1.run(debug=True)
