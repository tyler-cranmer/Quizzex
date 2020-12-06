$(document).ready(function() {
  $(".deckForm").each(function(index) {
    $(this).delay(300*index).fadeIn("slow");
  });

  $(".delete_button").click(function() {
    if(confirm("This will delete the deck and all associated card.  Are you sure?")) {
      $(this).parent("form").submit();
    }
  });
});
