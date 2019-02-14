import psycopg2


url = "dbname='politicoapi' host='localhost' port='5432' user='admin' password='1025'"

def db_connection():
    try:
        con = psycopg2.connect(url)
        print(con)
    except:
        print("con")

db_connection()

def create_tables():
    conn = db_connection()
    curr = conn.cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)
    conn.commit()
##
def tables():
    user = """CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        lastname character varying(50) NOT NULL,
        othernames character varying(50),
        email character varying(50),
        phonenumber character varying(50),
        passportUrl character varying(50) ,
        password character varying(50) NOT NULL,
        isAdmin boolean NOT NULL
    )"""

    party = """CREATE TABLE IF NOT EXISTS party (
            id serial PRIMARY KEY NOT NULL,
            party_name character varying(50) NOT NULL,
            hqAddress character varying(50) NOT NULL,
            logoUrl character varying(50) NOT NULL ,
        )"""

    office= """CREATE TABLE IF NOT EXISTS office (
                id serial PRIMARY KEY NOT NULL,
                office_type character varying(50) NOT NULL,
                office_name character varying(50) NOT NULL,
            )"""

    candidate = """CREATE TABLE IF NOT EXISTS candidate (
                    id serial PRIMARY  KEY NOT NULL,
                    office_id INT  NOT  NULL REFERENCES office(id) ON  DELETE  CASCADE ,
                     party_id INT NOT NULL REFERENCES  party(id) ON  DELETE  CASCADE ,
                     candidate_id INT NOT  NULL REFERENCES  user(id) ON  DELETE  CASCADE ,
                     UNIQUE (office_id,party_id,candidate_id)
                     
                )"""
    vote = """CREATE TABLE IF NOT EXISTS vote (
                        id serial PRIMARY  KEY NOT NULL,
                         createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
                         createdBy int NOT NULL REFERENCES user(id) ON  DELETE CASCADE , 
                         office_id INT  NOT  NULL REFERENCES office(id) ON  DELETE  CASCADE ,
                         candidate_id INT NOT  NULL REFERENCES  user(id) ON  DELETE  CASCADE ,
                         UNIQUE (createdBy,office_id,candidate_id)

                    )"""

    petition= """CREATE TABLE IF NOT EXISTS petition (
                            id serial PRIMARY  KEY NOT NULL,
                             createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
                             createdBy int NOT NULL REFERENCES user(id) ON  DELETE CASCADE , 
                             office_id INT  NOT  NULL REFERENCES office(id) ON  DELETE  CASCADE ,
                              body  character varying(50) NOT NULL,
                             UNIQUE (createdBy,office_id)

                        )"""


    queries = [user,party,office,candidate,vote,petition]
    return queries