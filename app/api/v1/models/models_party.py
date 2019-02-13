from flask import Flask,jsonify,request,make_response
parties=[]

class Parties:
    def __init__(self,id,party_name,hqAddress,logoUrl):
        self.id=len(parties)+1
        self.party_name=party_name
        self.hqAddres=hqAddress
        self.logoUrl=logoUrl


    def createparty(self):
        party={
            "id":self.id,
            "party_name":self.party_name,
            "hqAddress":self.hqAddres,
            "logoUrl":self.logoUrl,
        }

        return  make_response(jsonify({
            "satus":201,
            "message":"created successfully"
        }),201)

    # def getParty(self, id):
    #     for party in parties:
    #         if party['id'] == id:
    #             return party