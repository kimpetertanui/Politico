from app.database_config import create_tables
# users = []
from app.database_config import db_connection



class user:
    def __init__(self, id,firstname,lastname,othernames,email,phonenumber,passporturl,password,isadmin):
            self.id=id
            self.firstname=firstname
            self.lastname=lastname
            self.othernames=othernames
            self.email=email
            self.phonenumber=phonenumber
            self.passportUrl=passporturl
            self.password=password
            self.isadmin=isadmin

class db:
    def __init__(self):
        self.db = db_connection()

    def createuser(self):
        new_user={
            "id":self.id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "othernames":self.othernames,
            "email":self.email,
            "phonenumber":self.phonenumber,
            "passporturl":self.passporturl,
             "password":self.password,
            "isAdmin":self.isadmin
        }

    def getAllUsers(self):
        create_tables()
        curr = self.db.cursor()
        curr.execute("""SELECT id,firstname,lastname,othernames,email,phonenumber,passporturl,password,isadmin FROM users""")
        data = curr.fetchall()
        print (data)
        response = []

        for item in data:
            # id, firstname, lastname, othernames, email, phonenumber, passporturl,password, isadmin = data
            user = dict(
                id=item[0],
                firstname=item[1],
                lastname=item[2],
                othername=item[3],
                email=item[4],
                phonenumber=item[5],
                passporturl=item[6],
                password=item[7],
                isadmin=item[8]
            )
            response.append(user)
            return response




