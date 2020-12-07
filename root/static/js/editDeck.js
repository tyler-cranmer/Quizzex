$(document).ready(function() {

  // Fade in effect for each row
  $(".cardForm").each(function(index) {
    $(this).delay(300*index).fadeIn("slow");
  });

  // Enable tooltips for bootstrap on html page
  $('[data-toggle="tooltip"]').tooltip();

});
