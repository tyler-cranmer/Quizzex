Flashcard App
Allie Bernstein, Samuel Terry, Tyler Cranmer, Benjamin Price

Automated Test Cases: Explain how to run the test cases and the expected output. The instructor should be able to clone your repository and replicate your test results. You should have at least three automated tests.

To run the unittests, please make sure to have the mysql.connector python library installed.  Navigate to the outer-most directory of the project and run the unittests.py file using either 'python unittests.py' or 'python3 unittests.py'.

User Acceptance Testing The purpose of these tests is to have a formatted plan that you could provide to users to go through the steps in using your application and report whether it was successful or not.

TEST SUCCESSFUL LOGIN:
  Use case name
      Verify login with valid user name and password
  Description
      Test the login on Signinpage.html
  Pre-conditions
      User has valid user name and password
  Test steps
      1. Navigate Signinpage.html (can click the 'login' button on landingpage.html)
      2. Provide valid user name
      3. Provide valid password
      4. Click 'Sign In' button
  Expected result
      User should be navigated to their library page with their username shown at the top
  Actual result
      User is navigated to library with successful login and with their username at the top
  Status (Pass/Fail)
      Pass
  Notes
      N/A
  Post-conditions
      User is validated with database and successfully signed into their account.
      The account session details are logged in database.

TEST FAILED LOGIN:
  Use case name
      Verify failed login without valid credentials
  Description
      Test the login on Signinpage.html for failed login
  Pre-conditions
    User has invalid username or password
  Test steps
    1. Navigate to Signinpage.html (can click the 'login' button on landingpage.html)
    2. Provide invalid username
    3. Provide invalid password
    4. Click 'Sign In' button
  Expected result
    User should remain on Signinpage with a failed login message displayed
  Actual result
    User remains on the Signinpage with a red failed long message displayed
  Status (Pass/Fail)
    Pass
  Notes
    Works for both invalid username OR password
  Post-conditions
    No session details should be logged.  User may reattempt login as normal.

TEST SUCCESSFUL CREATE DECK:
  Use case name
    Verify that saving a new deck causes no errors
  Description
    Test the save button for a deck when fields are all filled out
  Pre-conditions
    User is logged in with a valid account
  Test steps
    1. Navigate to deck.html (can click on the Create Deck button on user-library.html
    2. Input a text string into the Deck Name field
    3. Input a text string into the Deck Description field
    4. Ensure a category is selected from the drop down options
    5. Click the 'Save' button
  Expected result
    User should be navigated back to their user library page
  Actual result
    User is navigated back to their user library page with no error message shown
  Status (Pass/Fail)
    Pass
  Notes
    Should update test when decks are importing into user-library correctly to ensure that functionality for newly created deck
  Post-conditions
    None at this time.  Later should display the new deck in the deck list on the user-library page

TEST FAILED CREATE DECK:
  Use case name
    Verify failed save deck message is shown
  Description
    Test the save button for a deck when name, description, or category fields are not filled out
  Pre-conditions
    User is logged in with a valid account
  Test steps
    1. Navigate to deck.html (can click on the Create Deck button on user-library.html and do any one or all of steps 2-4
    2. Omit a text string into the Deck Name field
    3. Omit a text string into the Deck Description field
    4. Omit a category from the drop down options
    5. Click the 'Save' button
  Expected result
    User should remain on the deck.html page and see a message to fill out all fields before saving
  Actual result
    User remains on the deck.html page and sees a new message, "Please fill out all fields before saving."
  Status (Pass/Fail)
    Pass
  Notes
    Could possibly implement specific messages for each case of omitted fields
  Post-conditions
    None
