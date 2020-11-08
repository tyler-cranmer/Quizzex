function signIn() {
  var username = document.forms[0].elements[0].value;
  var password = document.forms[0].elements[1].value;
  alert("This will submit the login for user: " + username + " with password: " + password + ".");
  $("#loginForm").submit();
}
