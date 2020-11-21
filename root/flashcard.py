from flask import Flask
from flask import request
from flask import render_template
from flask import session
import mysql.connector
import secrets
from helper_functions import *

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
    password="Allie2207"
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
# If invalid, returns to login page and display failed message
@app.route('/doLogin')
def dologin():
    username=request.args.get('username', None)
    password=request.args.get('password', None)
    valid = login(username,password)
    if (valid == True):
        session['username'] = username
        return goToLibrary()
    else:
        return render_template('Signinpage.html', failedLoginMessage="Failed login: please try again with a valid username and password.")

# Validates the entered username and password
# If valid, sets session variables and goes to user's library page
# If invalid, returns to signup page and displays error message
@app.route('/doSignup')
def doSignup():
    username = request.args.get('username', None)
    password1 = request.args.get('password1', None)
    password2 = request.args.get('password2', None)
    email = request.args.get('email', None)

    status = add_user(username, password1, password2, email)

    # Check status message
    # If valid, update the username session property and perform goToLibrary
    if status == "Success!":
        session['username'] = username
        return goToLibrary()

    # If invalid, render the 'SignUp' template (again) and pass the error message as a keyword argument
    else:
        return render_template('SignUp.html', signupFailureError=status)

# Navigates to create-new-card.html
@app.route('/createCard')
def goToCreateCard():
    return render_template('create-new-card.html')

# Adds a new card to the database and returns to user library
@app.route('/addNewCard')
def addNewCard():
    # Function will be run when the save button is pressed and form is submitted for
    # create-new-card.html page
    deck = request.args.get('deck-select', None)
    front = request.args.get('front-text', None)
    back = request.args.get('back-text', None)
    if(deck and front and back):
        # NEED TO ADD CODE TO SUBMIT CARD TO DATABASE HERE!
        return goToLibrary()
    else:
        return render_template('create-new-card.html', failedSaveMessage="Please fill out all fields before saving.")

# Navigates to deck.html page
@app.route('/createDeck')
def goToCreateDeck():
    return render_template('deck.html')

# Adds a new deck to the database and returns to user library
@app.route('/addNewDeck')
def addNewDeck():
    # Function will be run when the save button is pressed and form is submitted for
    # deck.html page
    name=request.args.get('deck-name', None)
    description=request.args.get('description', None)
    category=request.args.get('category-select', None)
    isPublic=request.args.get('public-checkbox', None)
    if(isPublic and name and description and category):
        # NEED TO ADD CODE TO SUBMIT DECK TO DATABASE HERE!
        # THIS IS FOR PUBLIC DECKS ONLY!!!
        username = session['username']
        add_deck(username,1, name, category)
        return goToLibrary()
    elif(name and description and category):
        # NEED TO ADD CODE TO SUBMIT DECK TO DATABASE HERE!
        # THIS IS FOR PRIVATE DECKS ONLY!!!
        username = session['username']
        add_deck(username,0, name, category)
        return goToLibrary()
    else:
        return render_template('deck.html', failedSaveMessage="Please fill out all fields before saving.")

# Returns user to their personal library page
@app.route('/library')
def goToLibrary():
    user = session['username']
    user_decks = get_decks(user)
    return render_template('user-library.html', username=user, decks = user_decks)

# Navigates to Signinpage.html
@app.route('/signIn')
def goToSignIn():
    return render_template('Signinpage.html')

# Navigates to SignUp.html
@app.route('/signUp')
def goToSignUp():
    return render_template('SignUp.html')
