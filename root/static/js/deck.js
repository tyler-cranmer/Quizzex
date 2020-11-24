
/*
  This function is run everytime a user enters input into the textarea on the page
  Updates the text on beneath the textarea to show the number of characters currently
  in the textarea with a limit of 300
*/
$('#description').on('input', function() {
  var numchars = $('#description').val().length;
  $('#desc-counter').text(numchars + "/300");
});

/*
  save() is run when the save button is clicked to submit new deck information
  sends the following data to flashcard.py flask file:
  - deck-name: name of the Deck
  - description: description of the deck
  - category-select: deck category for folder organization
  - public-checkbox: sets public option for public/private decks
 */
function save() {
    document.forms[0].submit();
}
