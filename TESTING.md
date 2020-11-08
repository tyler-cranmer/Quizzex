Flashcard App
Allie Bernstein, Samuel Terry, Tyler Cranmer, Benjamin Price

Automated Test Cases: Explain how to run the test cases and the expected output. The instructor should be able to clone your repository and replicate your test results. You should have at least three automated tests.

EXPLANATION HERE (and can remove directions above)

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
  Use case Name
    Verify failed login without valid credentials
  Description
    Test the login on Signinpage.html for failed login
Pre-conditions
  User has invalid username or password
Test steps
  1. Navigate Signinpage.html (can click the 'login' button on landingpage.html)
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
