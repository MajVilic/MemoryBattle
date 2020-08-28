import json, falcon
from mysql.connector import Error
import mysql.connector


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='membattle',
                                         user='root',
                                         password='')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)



class companies(object):
    def on_get(self, req, resp):
        resp.body = json.dumps('abc1234567')
        resp.status = falcon.HTTP_200

class allresult(object):
    def on_get(self, req, resp):
        connection.commit()   #s komitom pobere vse spremembe/pregleduje spremembe
        cursor.execute("SELECT * FROM game")
        mycursor = cursor.fetchall()
        dump = []
        for result in mycursor:
            poizvedba = "SELECT Username FROM user WHERE UserID={}".format(result[1])
            print(poizvedba)
            cursor.execute(poizvedba)
            user = cursor.fetchall()
            prazen = {}
            prazen['id'] = user
            prazen['score'] = result[2]
            prazen['nof'] = result[4]
            prazen['diff'] = result[3]
            dump.append(prazen)
        print(dump)

        resp.body = json.dumps(dump)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = json.loads(req.stream.read().decode('utf-8'))
        vstavi = "INSERT INTO `game` (`GameID`, `UserID`, `GameScore`,`Difficulty`, `NumberOfPlayers`) VALUES ('',%s,%s,%s,%s);"
        vrednosti = (data["userid"], data["gamescore"], data["diff"], data["nof"])
        cursor.execute(vstavi, vrednosti)
        connection.commit()


class login(object):
    def on_get(self, req, resp):
        cursor.execute("SELECT Username,Password,UserID FROM user")
        mycursor = cursor.fetchall()

        resp.body = json.dumps(mycursor)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = json.loads(req.stream.read().decode('utf-8'))
        vstavi = "INSERT INTO `user` (`Username`, `Password`, `Mail`,`SecretAnswer`, `UserID`) VALUES (%s,%s,%s,%s,'');"
        vrednosti = (data["user"], data["password"], data["email"], data["scrt"])
        cursor.execute(vstavi, vrednosti)
        connection.commit()


class scrt(object):
    def on_get(self, req, resp):
        cursor.execute("SELECT Username,SecretAnswer FROM user")
        mycursor = cursor.fetchall()

        resp.body = json.dumps(mycursor)
        resp.status = falcon.HTTP_200
        print(mycursor)

    def on_post(self, req, resp):
        data = json.loads(req.stream.read().decode('utf-8'))
        vstavi = "UPDATE `user` SET Password=%s WHERE Username=%s"
        vrednosti = (data["password"], data["user"])
        cursor.execute(vstavi, vrednosti)
        connection.commit()


    # def on_get(self, req, resp):