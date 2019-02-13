offices = []
class Offices:
    def __init__(self,id,type,name):
        self.id=len(offices)+1
        self.type=type
        self.name=name

## creating a political office

    def createoffice(self):
        office={
            "id":self.id,
            "type":self.type,
            "name":self.name,

        }

        return offices.append(office)

<<<<<<< HEAD
    # def welcome(self):
    #     return "Welcome admin"
=======
    def welcome(self):
        return "Welcome user"
>>>>>>> ce30af00f9fc68e5c19dee6bf3e628fc358ad13b
