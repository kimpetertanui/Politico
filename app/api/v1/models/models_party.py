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

        return parties.append(party)

    # def getParty(self, id):
    #     for party in parties:
    #         if party['id'] == id:
    #             return party