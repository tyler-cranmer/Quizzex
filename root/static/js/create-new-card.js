/*
  Runs everytime a user enters text into the first textarea
  Updates the character counter and front-card-example
*/
$('#front-text').on('input', function() {
  var numchars = $('#front-text').val().length;
  $('#front-counter').text(numchars + "/300");
  $('#front-card-example').html("<p class='align-self-center'>" + $('#front-text').val() + "</p>");
});

/*
  Runs everytime a user enters text into the second textarea
  Updates the character counter and back-card-example
*/
$('#back-text').on('input', function() {
  var numchars = $('#back-text').val().length;
  $('#back-counter').text(numchars + "/300");
  $('#back-card-example').html("<p class='align-self-center'>" + $('#back-text').val() + "</p>");
});

/*
  save() is run when the save button is clicked to submit new card information
  sends the following data to flashcard.py flask file:
  - deck-select: name of the deck card will be added to
  - front-text: text for front of card
  - back-text: text for back of card
*/
function save() {
  document.forms[0].submit();
}
