$('#description').on('input', function() {
  var numchars = $('#description').val().length;
  $('#desc-counter').text(numchars + "/300");
});

function save() {
  var name = document.forms[0].elements[0].value;
  var description = document.forms[0].elements[1].value;
  var category = document.forms[0].elements[2].value;
  // Value of checkbox is only sent when form is submitted.  This variable only says 'on' either way
  var isPublic = document.forms[0].elements[3].value;

  alert("Name: " + name + "\nDescription: " + description + "\nCategory: " + category + "\nIs it public?: " + isPublic);
  return document.forms[0].submit();
}

function back() {
  var res = confirm("Your new deck has not been saved.  Are you sure you would like to go back?");
  if (res) {
    window.location.href = '/library';
  }
}
