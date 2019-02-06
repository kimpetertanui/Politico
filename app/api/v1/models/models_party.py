parties=[]

class Parties:
    def __init__(self,partyID,party_name,hqAddress,logoUrl):
        self.parttyID=partyID
        self.party_name=party_name
        self.hqAddres=hqAddress
        self.logoUrl=logoUrl


    def createparty(self):
        party={
            "partyID":self.parttyID,
            "party_name":self.party_name,
            "hqAddress":self.hqAddres,
            "logoUrl":self.logoUrl,
        }

        return parties.append(party)