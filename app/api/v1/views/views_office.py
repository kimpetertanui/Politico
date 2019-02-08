from flask import make_response, jsonify, Blueprint,request
from app.api.v1.models.models_office import offices
import random

v1= Blueprint('api_v1', __name__, url_prefix='/api/v1')


@v1.route('/index', methods=['GET'])
def hello():
    return 'POLITICO '


@v1.route("/offices",methods=['GET'])
def getAllOffices():
    return make_response(jsonify(offices), 200)


@v1.route("/offices/<officeID>",methods=['GET'])
def getOffice(officeID):
    for office in offices:
        if office["id"] == int(officeID):
            return make_response(jsonify(office), 200)

    return make_response(jsonify({
        "code": 404,
        "error": "Could not find office with id {}".format(officeID)
    }), 404)


@v1.route("/offices", methods=['POST'])
def addOffice():
    json_data = request.get_json(force=True)

    id = random.randint(3, 10)
    office_type = json_data["type"]
    office_name = json_data["name"]

    new_office = {
        "id": id,
        "type": office_type,
        "name": office_name
    
    }

    offices.append(new_office)

    return make_response(jsonify({
        "status": 200,
        "data": [new_office]
    }), 200)


@v1.route("/offices/<officeID>", methods=['DELETE'])
def deleteOffice(officeID):
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
@v1.route('/offices/<officeID>',methods=['PATCH'])
def party_update(officeID):
    for office in offices:
        if office ['officeID']==int(officeID):
            data=request.get_json()
            new_name=data['office_name']
            office['office_name']=data['office_name']


            return make_response(jsonify({
                "status":200,
                 "data":"updated  the office with officeID {} ".format(officeID)
            }),200)
        elif office['officeID']==None:
            return "Enter an ID to make update"
        else:
            update_office = {
                "office_name": office['office_name']

            }
            offices.append(update_office)
            return make_response(jsonify({
                "status": 200,
                "data": [update_office]
            }), 200)



if __name__ == "__main__":
    v1.run(debug=True)