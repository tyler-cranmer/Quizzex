$('#front-text').on('input', function() {
  var numchars = $('#front-text').val().length;
  $('#front-counter').text(numchars + "/300");
  $('#front-card-example').html("<p>" + $('#front-text').val() + "</p>");
});

$('#back-text').on('input', function() {
  var numchars = $('#back-text').val().length;
  $('#back-counter').text(numchars + "/300");
  $('#back-card-example').html("<p>" + $('#back-text').val() + "</p>");
});
