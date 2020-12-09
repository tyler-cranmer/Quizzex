$(document).ready(function() {

  // Fade in effect for each row
  $(".cardForm").each(function(index) {
    $(this).delay(300*index).fadeIn("slow");
  });

  $(".delete_button").click(function() {
    if(confirm("This will delete this card from the deck.  Are you sure?")) {
      $(this).closest("form").submit();
    }
  });

  // Enable tooltips for bootstrap on html page
  $('[data-toggle="tooltip"]').tooltip();

});
