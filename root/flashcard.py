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
@app.route('/goToCreateCard')
def goToCreateCard(failMessage = None):
    user = session['username']
    # retrieve a list of decks from database in the form [("deckName1",),("deckName2",),...]
    user_decks = get_decks(user)
    deck_html = None
    f_message = failMessage
    if(user_decks):
        deck_html = ""
        for deck in user_decks:
            deck_html = (deck_html + '<option value="' + deck[0] + '">' + deck[0] + '</option>')
    return render_template('create-new-card.html', decks=deck_html, failedSaveMessage=f_message)

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
        return goToCreateCard("Please fill out all fields before saving.")

# Navigates to deck.html page
@app.route('/goToCreateDeck')
def goToCreateDeck(failMessage = None):
    user = session['username']
    # retrieve a list of decks from database in the form [("deckName1",),("deckName2",),...]
    user_decks = get_decks(user)
    deck_count = 0
    f_message = failMessage
    if(user_decks):
        for deck in user_decks:
            deck_count = deck_count + 1
    return render_template('deck.html', numdecks=deck_count, failedSaveMessage=f_message)

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
        return goToCreateDeck("Please fill out all fields before saving.")

# Returns user to their personal library page
@app.route('/library')
def goToLibrary():
    user = session['username']
    # retrieve a list of decks from database in the form [("deckName1",),("deckName2",),...]
    user_decks = get_decks(user)
    deck_html = None
    deck_count = 0
    # For each deck, increment count and create an html form with delete and open buttons
    if(user_decks):
        deck_html = ""
        for deck in user_decks:
            deck_html = (deck_html +
                '<form method="POST" action="/doDeckFunction" class="deckForm">' +
                '<input name="deckname" type="hidden" value="' + deck[0] + '"/>' +
                '<input name="study" class="deck" type="submit" value="' + deck[0] + '"/>' +
                '<input name="edit" class="deck_button_img" type="image" src="static/img/editIcon.jpg" alt="Submit">' +
                '<input name="delete" class="deck_button_img" type="image" src="static/img/trashcan.png" alt="Submit">' +
                '</form><br>')
            deck_count = deck_count + 1
    return render_template('user-library.html', username=user, decks = deck_html, numdecks = deck_count)

# Navigates to Signinpage.html
@app.route('/signIn')
def goToSignIn():
    return render_template('Signinpage.html')

# Navigates to SignUp.html
@app.route('/signUp')
def goToSignUp():
    return render_template('SignUp.html')

# Performs either delete or open from a deck form submitted on the user library page
@app.route('/doDeckFunction', methods=['GET', 'POST'])
def doDeckFunction():
    if(request.method == 'POST'):
        deckname = request.form.get('deckname', None)
        if(request.form.get('delete.x', None)):
            return "Delete was selected for " + deckname + " deck."
        elif(request.form.get('study', None)):
            return goToStudy(deckname)
        elif(request.form.get('edit.x', None)):
            return "Edit was selected for " + deckname + " deck."
        else:
            return "Error: Neither edit, delete, nor study was selected for " + deckname + " deck."
    else:
        return "Post request was not performed or another error occurred."

@app.route('/study')
def goToStudy(deck):
    return render_template('study_card.html', deckname=deck)
