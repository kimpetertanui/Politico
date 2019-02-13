from flask import make_response, jsonify, Blueprint,request
from app.api.v1.models.models_party import parties

b_party= Blueprint('parties', __name__, url_prefix='/api/v1')


@b_party.route('/index', methods=['GET'])
def index():
    return make_response(jsonify({
        "status":200,
        "message":"Politico enables citizens give their mandate to Leaders "

    }),200)



@b_party.route("/parties",methods=['GET'])
def getAllParties():

    return make_response(jsonify(
        {"status":200},
        {"data":parties}),200)


@b_party.route("/parties/<partyID>",methods=['GET'])
def getParty(partyID):
    try:
        id=int(partyID)
        for party in parties:
            print(type(party["id"]))

            if party["id"] == id:

                return make_response(jsonify({

                    "data": party,
                    "status": 200
                }),200)


        return make_response(jsonify({
            "status": 404,
            "message": "Could not find party with id {} kindly check it again".format(partyID)
        }), 404)
    except:
        return jsonify({"status":400},{"message":"You have entered invalid party ID"})


@b_party.route("/parties", methods=['POST'])
def addparty():


    json_data = request.get_json(force=True)
    id = len(parties)+1
    if json_data:
        if (json_data['party_name'] is not "") and (json_data["hqAddress"] is not "") and (json_data["logoUrl"] is not ""):
            print("##")
            print(json_data )
            party_name = json_data["party_name"]
            hqAddress = json_data["hqAddress"]
            logoUrl=json_data["logoUrl"]

            new_party = {
                "id":id,
                "party_name":party_name,
                "hqAddress":hqAddress,
                "logoUrl":logoUrl,
            }

            parties.append(new_party)

            return make_response(jsonify({
                "status": 201,
                "data": [new_party]
            }), 201)
        else:
            return make_response(jsonify({
                            "status":401,
                            "message":"Missing required fields"
                        }))


@b_party.route("/parties/<partyID>", methods=['DELETE'])
def deleteParty(partyID):
   try:
       for party in parties:
           if party["id"] == int(partyID):
               parties.remove(party)
               return make_response(jsonify({
                   "status": 200,
                   "data": "deleted successfully"
               }), 200)
           # elif not party:
           #     return "Please enter party ID to delete"
           # else:
               return make_response(jsonify({
                   "status": 404,
                   "msg": "could not find party with ID {}".format(partyID)
               }), 404)
   except:
       return jsonify({"status": 400}, {"message": "Please enter a valid party ID to delete"})

@b_party.route('parties/<partyID>',methods=['PATCH'])
def party_update(partyID):
    for party in parties:
        if party ['id']==int(partyID):

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