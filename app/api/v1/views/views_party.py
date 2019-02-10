from flask import make_response, jsonify, Blueprint,request
from app.api.v1.models.models_party import parties
import random
# from app.api.v1.models.models_office import Office

b_party= Blueprint('parties', __name__, url_prefix='/api/v1')


@b_party.route('/index', methods=['GET'])
def index():
    return make_response(jsonify({
        "status":200,
        "message":"Politico nables citizens give their mandate to Leaders "

    }),200)



@b_party.route("/parties",methods=['GET'])
def getAllParties():
    return make_response(jsonify(
        {"status":200},
        {"data":parties}),200)


@b_party.route("/parties/<partyID>",methods=['GET'])
def getParty(partyID):
    for party in parties:
        if partyID == partyID:
            return make_response(jsonify(party), 200)
        else:
            return make_response(jsonify({
                "status": 404,
                "error": "Could not find party with id {}".format(partyID)
            }), 404)

@b_party.route("/parties", methods=['POST'])
def addparty():
    json_data = request.get_json(force=True)
    partyID = len(parties)+1
    print("##")
    print(json_data )
    party_name = json_data["party_name"]
    hqAddress = json_data["hqAddress"]
    logoUrl=json_data["logoUrl"]

    new_party = {
        "partyID":partyID,
        "party_name":party_name,
        "hqAddress":hqAddress,
        "logoUrl":logoUrl,
    }

    parties.append(new_party)

    return make_response(jsonify({
        "status": 201,
        "data": [new_party]
    }), 201)


@b_party.route("/parties/<partyID>", methods=['DELETE'])
def deleteParty(partyID):
    for party in parties:
        if party["partyID"]==int(partyID):
            parties.remove(party)
            return make_response(jsonify({
                "status": 200,
                "data": "deleted successfully"
            }), 200)
        elif not party :
            return "Please enter party ID to delete"
        else:
            return make_response(jsonify({
                "status": 404,
                "error": "could not find party with ID {}".format(partyID)
            }), 404)

@b_party.route('parties/<partyID>',methods=['PATCH'])
def party_update(partyID):
    for party in parties:
        if party ['partyID']==int(partyID):
            data=request.get_json()
            new_name=data['party_name']
            party['party_name']=data['party_name']
            return make_response(jsonify({
                "status":200,
                 "data":"updated  the party with party ID {} ".format(partyID)
            }),200)
        elif party in parties:
            return "Party Already exist"
        else:
            update_party = {
                "party_name": party['party_name']

            }
            parties.append(update_party)
            return make_response(jsonify({
                "status": 200,
                "data": [update_party]
            }), 200)



if __name__ == '__main__':
    b_party.run(debug=True)