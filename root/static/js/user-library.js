$(document).ready(function() {
  $(".deckForm").each(function(index) {
    $(this).delay(400*index).fadeIn("slow");
  });
});
