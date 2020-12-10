import mysql.connector

#to run this code you may need to install using the following:
# pip install mysql-connector-python
# pip install tabulate


def connect_db():
     mydb = mysql.connector.connect(
      host="35.223.161.145",
      user="root",
      password="Allie2207"
      )
     return mydb
mydb=connect_db()
mycursor = mydb.cursor(buffered=True)
mycursor.execute("use flashcards")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#functions to CREATE entries

#function to call to add a new user to the user table when they create account
def add_user(new_username, new_password, confirm_password, new_email):
    id = mycursor.lastrowid

    #check that the username does not already exist; if not, return an error message
    if(get_user(new_username)!= None):
        return("Sorry, this username is already taken.")

    # Confirm that the two password inputs match; if not, return an error message
    if (new_password != confirm_password):
        return("Passwords don't match, please try again.")

    else:
        sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        val = (new_username, new_password, new_email)
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record inserted.")
        #return mycursor.lastrowid

        # If everything checks out, return a successful status message
        return "Success!"


#function to call when user creates a new deck to add into database (will use a session variable to pass in username)
def add_deck(username, public, deckname, category):
    id = mycursor.lastrowid
    sql = "INSERT INTO decks (deckname,public, category, username) VALUES (%s, %s, %s, %s)"
    val = (deckname, public, category, username)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


#function to create new card
def add_card(deckID, cardFront, cardBack):
    id = mycursor.lastrowid
    sql = "INSERT INTO cards (deckID, cardFront, cardBack) VALUES (%s, %s, %s)"
    val = (deckID,cardFront, cardBack)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#function to get decks for a user from DATABASE
def get_decks(username):
    sql = "SELECT deckname, iddecks FROM decks WHERE username = %s"
    val = (username, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult

#get all public decks
def get_public_decks():
    sql="SELECT deckname, iddecks FROM decks WHERE public = 1"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult


#helper function to get a Deck ID given a deckname
def get_deckID(deckname):
    sql = "SELECT iddecks FROM decks WHERE deckname = %s"
    val=(deckname, )
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult[0][0]
#=======
#function to get user/login
def login(username, password):
    user=get_user(username)
    if user == None:
        return False
    else:
        if (user[2] == password):
            return True
        else:
            return False


#function to get cards from a deck
def get_cards(deckid):
    sql = "SELECT idcards, cardFront, cardBack FROM cards WHERE deckid = %s"
    val = (deckid, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#function to REMOVE/delete an entry from the database


#function to remove a user
def remove_user(username):
    if (get_user(username) == None):
        return("This user does not exist")
    else:
        sql = "delete FROM users WHERE username = %s"
        val=(username, )
        mycursor.execute(sql,val)
        mydb.commit()
        return("User Deleted")

#function to remove a deck and the cards in that deck
def remove_deck(username, deckname):
    val1 = (get_deckID(deckname), )
    sql1 = ("DELETE cards FROM cards WHERE deckID = %s")
    #print(val1)
    mycursor.execute(sql1,val1)
    sql2 = ("DELETE decks FROM decks WHERE username = %s AND deckname = %s")
    val2=(username, deckname)
    mycursor.execute(sql2,val2)
    mydb.commit()
    return("Deck Deleted")


def remove_card(card_id):
    sql=("DELETE cards from cards WHERE idcards = %s")
    val=(card_id, )
    mycursor.execute(sql,val)
    mydb.commit()
    return("Card Deleted")


#----------------------------------------------------------------------
#function to get cards from a deck
def get_cards1(deckid):
    sql = "SELECT cardFront, cardBack FROM cards WHERE deckid = %s"
    val = (deckid, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult