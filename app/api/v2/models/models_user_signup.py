user = []
class Offices:
    def __init__(self,id,firstname,lastname,othername,email,phoneNumber,passportUrl,isAdmin):
        self.id=len(user)+1
        self.firstname=firstname
        self.lastname=lastname
        self.othername=othername
        self.email=email
        self.phoneNumber=phoneNumber
        self.passportUrl=passportUrl
        self.isAdmin=isAdmin

## creating a user

    def createuser(self):
        new_user={
            "id":self.id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "othername":self.othername,
            "email":self.email,
            "phoneNumber":self.phoneNumber,
            "passportUrl":self.passportUrl,
            "isAdmin":self.isAdmin
        }

        return user.append(new_user)


