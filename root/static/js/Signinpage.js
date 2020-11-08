/*
  signIn will submit the form to the flask file with username and password variables
  TO DO: return a statement to the user if the credentials are not in the database!!!!
*/
function signIn() {
  //var username = document.forms[0].elements[0].value;
  //var password = document.forms[0].elements[1].value;
  //alert("This will submit the login for user: " + username + " with password: " + password + ".");
  $("#loginForm").submit();
}
