$(document).ready(function() {
  $(".deckForm").each(function(index) {
    $(this).delay(300*index).fadeIn("slow");
  });
});
