import mysql.connector
from tabulate import tabulate

#to run this code you may need to install using the following: 
# pip install mysql-connector-python
# pip install tabulate


def connect_db():
     mydb = mysql.connector.connect(
      host="35.223.161.145",
      user="root",
      password=""
      )
     return mydb
mydb= connect_db()
mycursor = mydb.cursor(buffered=True)
mycursor.execute("use flashcards")


#functions to CREATE entries

#function to call to add a new user to the user table when they create account
def add_user(new_username, new_password, new_email):
    id = mycursor.lastrowid
    sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    val = (new_username, new_password, new_email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

#function to call when user creates a new deck to add into database (will use a session variable to pass in username)
def add_deck(username, public, deckname, category):
    id = mycursor.lastrowid
    sql = "INSERT INTO users (deckname,public, category, username) VALUES (%s, %s, %s, %s)"
    val = (deckname, public, category, username)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

#function to create new card
def add_card(deckID, cardFront, cardBack):
    id = mycursor.lastrowid
    sql = "INSERT INTO users (deckID, cardFront, cardBack) VALUES (%s, %s, %s)"
    val = (deckID,cardFront, cardBack)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")





#functions to READ/retrieve data from database

#function to get user info from database
def get_user(username):
    sql = "SELECT * FROM users WHERE username = %s"
    val=(username, )
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult[0]








