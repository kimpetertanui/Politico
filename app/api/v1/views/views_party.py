from flask import make_response, jsonify, Blueprint,request
from app.api.v1.models.models_party import parties
import random
# from app.api.v1.models.models_office import Office

b_party= Blueprint('parties', __name__, url_prefix='/api/v1')


@b_party.route('/Home', methods=['GET'])
def hello():
    return 'Flask API endpoint'


@b_party.route("/getAllParties",methods=['GET'])
def getAllParties():
    return make_response(jsonify(
        {"status":200},
        {"data":parties}))


@b_party.route("/getParty/<partyID>",methods=['GET'])
def getParty(partyID):
    for party in parties:
        if partyID == partyID:
            return make_response(jsonify(party), 200)
        else:
            return make_response(jsonify({
                "status": 404,
                "error": "Could not find party with id {}".format(partyID)
            }), 404)


@b_party.route("/addparty", methods=['POST'])
def addparty():
    json_data = request.get_json()

    partyID = random.randint(3, 10)
    party_name = json_data["party_name"]
    hqAddress = json_data["hqAddress"]
    logoUrl=json_data['logoUrl']

    new_party = {
        "partyID":partyID,
        "party_name":party_name,
        "hqAddress":hqAddress,
        "logoUrl":logoUrl,
    }

    parties.append(new_party)

    return make_response(jsonify({
        "status": 200,
        "data": [new_party]
    }), 200)


# @b_party.route("/deleteParty/<partyID>", methods=['DELETE'])
# def deleteParty(partyID):
#     for party in parties:
#         if party["partyID"] == int(partyID):
#             parties.remove(party)
#             return make_response(jsonify({
#                 "status": 200,
#                 "data": "deleted successfully"
#             }), 200)
#
#     return make_response(jsonify({
#         "status": 404,
#         "error": "could not find party with ID {}".format(partyID)
#     }), 404)


if __name__ == '__main__':
    b_party.run(debug=True)