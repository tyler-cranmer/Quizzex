$(document).ready(function() {
  $(".deckForm").each(function(index) {
    $(this).delay(300*index).fadeIn("slow");
  });

  $(".delete_button").click(function() {
    if(confirm("This will delete the deck and all associated cards.  Are you sure?")) {
      $(this).parent("form").submit();
    }
  });

  // Enable tooltips for bootstrap on html page
  $('[data-toggle="tooltip"]').tooltip();

});
