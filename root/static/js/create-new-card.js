/*
  Runs everytime a user enters text into the first textarea
  Updates the character counter and front-card-example
*/
$('#front-text').on('input', function() {
  var numchars = $('#front-text').val().length;
  $('#front-counter').text(numchars + "/300");
  $('#front-card-example').html("<p>" + $('#front-text').val() + "</p>");
});

/*
  Runs everytime a user enters text into the second textarea
  Updates the character counter and back-card-example
*/
$('#back-text').on('input', function() {
  var numchars = $('#back-text').val().length;
  $('#back-counter').text(numchars + "/300");
  $('#back-card-example').html("<p>" + $('#back-text').val() + "</p>");
});

/*
  save() is run when the save button is clicked to submit new card information
  sends the following data to flashcard.py flask file:
  - deck-select: name of the deck card will be added to
  - front-text: text for front of card
  - back-text: text for back of card
*/
function save() {
  var front = document.forms[0].elements[1].value;
  var back = document.forms[0].elements[2].value;
  alert("Front: " + front + "\nBack: " + back);
}

/*
  back() displays warning message and navigates back to the user library if user accepts
*/
function back() {
  var res = confirm("Your new flashcard has not been saved.  Are you sure you would like to go back?");
  if (res) {
    window.location.href = '/library';
  }
}
