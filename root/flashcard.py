from flask import Flask
from flask import request
from flask import render_template
from flask import session
import mysql.connector
import secrets


app = Flask(__name__)

# Set secret key
# REQUIRED for session to work to track username through website
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)

###################################
### Connection for the database ###
###################################
mydb = mysql.connector.connect(
    host="35.223.161.145",
    user="root",
    password=""
    )

mycursor = mydb.cursor()
mycursor.execute("use flashcards")

########################
### Helper Functions ###
########################
def get_user(username):
    sql = "SELECT * FROM users WHERE username = %s"
    val=(username, )
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult[0]

#function to get user
def login(username, password):
    user=get_user(username)
    if user == None:
        return False
    else:
        if (user[2] == password):
            return True
        else:
            return False

##############
### ROUTES ###
##############

# Navigates to langingPage.html, root of the website
@app.route('/')
def mysite():
    return render_template('landingPage.html')

# Validates the entered username and password
# If valid, sets session variables and goes to user's library page
# TODO: If invalid, returns to login page and display failed message
@app.route('/doLogin')
def dologin():
    username=request.args.get('username', None)
    password=request.args.get('password', None)
    valid = login(username,password)
    if (valid == True):
        session['username'] = username
        return render_template('user-library.html', username=session['username'])
    else:
        return render_template('Signinpage.html', failedLoginMessage="Failed login: please try again with a valid username and password.")

# Navigates to create-new-card.html
@app.route('/createCard')
def goToCreateCard():
    return render_template('create-new-card.html')

# Adds a new card to the database and returns to user library
@app.route('/addNewCard')
def addNewCard():
    # Function will be run when the save button is pressed and form is submitted for
    # create-new-card.html page
    return goToLibrary()

# Navigates to deck.html page
@app.route('/createDeck')
def goToCreateDeck():
    return render_template('deck.html')

# Adds a new deck to the database and returns to user library
@app.route('/addNewDeck')
def addNewDeck():
    # Function will be run when the save button is pressed and form is submitted for
    # deck.html page
    return goToLibrary()

# Returns user to their personal library page
@app.route('/library')
def goToLibrary():
    return render_template('user-library.html', username=session['username'])

# Navigates to Signinpage.html
@app.route('/signIn')
def goToSignIn():
    return render_template('Signinpage.html')

# Navigates to SignUp.html
@app.route('/signUp')
def goToSignUp():
    return render_template('SignUp.html')
