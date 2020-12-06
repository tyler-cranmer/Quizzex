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
# SECRET_KEY must be a constant value. When using a random value, gunicorn re-returns
# the code at random points with things called 'workers' that essentially makes it look
# like the user is logged out and breaks things
app.config["SECRET_KEY"] = '6548973215454889'

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
        add_card(get_deckID(deck), front, back)
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
        # THIS IS FOR PUBLIC DECKS ONLY!!!
        username = session['username']
        add_deck(username,1, name, category)
        return goToLibrary()
    elif(name and description and category):
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
                '<div class="deckForm">' +
                '<form method="POST" action="/study" class="">' +
                '<input name="deckname" type="hidden" value="' + deck[0] + '"/>' +
                '<input name="study" class="deck" type="submit" value="' + deck[0] + '"/>' +
                '</form>' +
                '<form method="POST" action="/editDeck" class="button_form">' +
                '<input name="deckname" type="hidden" value="' + deck[0] + '" class="hidden"/>' +
                '<input name="edit" class="deck_button_img" type="image" src="static/img/editIcon.jpg" alt="Edit"/>' +
                '</form>' +
                '<form method="POST" action="/deleteDeck" class="button_form delete_form">' +
                '<input name="deckname" type="hidden" value="' + deck[0]+ '" class="hidden"/>' +
                '<img name="delete" class="deck_button_img" src="static/img/trashcan.png" alt="Delete">' +
                '</form><br>' +
                '</div>')
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
            return deleteDeck(deckname)
        elif(request.form.get('study', None)):
            return goToStudy(deckname)
        elif(request.form.get('edit.x', None)):
            return goToEditDeck(deckname)
        else:
            return "Error: Neither edit, delete, nor study was selected for " + deckname + " deck."
    else:
        return "Post request was not performed or another error occurred."

@app.route('/study', methods=['GET', 'POST'])
def goToStudy():
    # retrive deckname from the form
    deck = request.form.get('deckname', None)
    if(request.method == 'POST'):
        return render_template('study_card.html', deckname=deck)

# Deletes the selected deck from the user's library & the deck table
#as well as the cards associated from that deck
@app.route('/deleteDeck')
def deleteDeck(deck):
    user = session['username']
    remove_deck(user, deck)
    return goToLibrary()

# Signs user out and returns them to the landing page
@app.route('/doLogout')
def signOut():
    session['username'] = None
    return mysite()

# Navigates user to the edit deck page for the selected deck
@app.route('/editDeck', methods=['GET', 'POST'])
def goToEditDeck():
    # retrieve the current user's username
    user = session['username']
    # retrieve deckname from form request
    if(request.method == 'POST'):
        deckname = request.form.get('deckname', None)
    # retrieve a list of decks from database in the form [("deckName1",),("deckName2",),...]
    deck_cards = get_cards(get_deckID(deckname))
    card_html = None
    card_count = 0
    # For each deck, increment count and create an html form with delete and open buttons
    if(deck_cards):
        card_html = ""
        for card in deck_cards:
            card_html = (card_html +
                '<div class="cardForm">' +
                '<h2>' + card[0] + '</h2>' +
                '<p>' + card[1] + '</p>' +
                # Edit has been removed.  Maybe will be added back in at a later date
                #'<form method="POST" action="" class="button_form">' +
                #'<input name="cardFront" type="hidden" value="' + card[0] + '" class="hidden"/>' +
                #'<input name="edit" class="deck_button_img" type="image" src="static/img/editIcon.jpg" alt="Edit"/>' +
                #'</form>' +
                '<form method="POST" action="" class="button_form delete_form">' +
                '<input name="cardFront" type="hidden" value="' + card[0]+ '" class="hidden"/>' +
                '<img name="delete" class="deck_button_img" src="static/img/trashcan.png" alt="Delete">' +
                '</form><br>' +
                '</div>')
            card_count = card_count + 1
    return render_template('editDeck.html', username=user, deckname=deckname, cards=card_html, numcards=card_count)
