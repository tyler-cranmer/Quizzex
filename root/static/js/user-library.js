$(document).ready(function() {
  $(".deck").each(function(index) {
    $(this).delay(400*index).fadeIn("slow");
  });
});
