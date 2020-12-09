
// function to flip the card
function flip() {
    $('.card').toggleClass('flipped');
};



//function to check if back of the card being displayed is present in html
//Used to fix z-indexing problem when iterating through 
//the deck while back of card is showing. 
function flip_back(){
    var cardFlipped = document.getElementsByClassName('card flipped');
    if(cardFlipped.length > 0){
        console.log('Back of card is showing');
        flip();
        setTimeout(function(){ 
            index ++;
            if (index > deckArray.length - 1 ) {
                $("p").fadeOut(function() {
                    $("#card_info").text('End of the deck');
                    $("#backcard_info").text('End of the deck');
                    $("p").fadeIn();
                    index = deckArray.length - 1;
                });
            }else{
                $("p").fadeOut(function() {
                    $("#card_info").text(deckArray[index][0]);
                    $("#backcard_info").text(deckArray[index][1]);
                    $("p").fadeIn();
                });
            }}, 225);
    }else{
        console.log('Front of card is showing');
    };
};


//Flip through deck of cards
$(document).ready(function() {
    
    //Array to store the deck cards
    var deckArray = [
        ["Danny Davis Snowboard", "Deep Thinker"],
        ["Mark Mcmorris Snowboard", "The Process"],
        ["K2 Snowboard", "Darkside"],
        ["Ride Snowboard", "Alter-Ego"],
        ["GNU", "Gorp"], ["LibTech", "Orca"]
    ];
    
    var index = 0;
    
    //Setting initial values for deck
    $(document).ready(function() {
        $("#card_info").text(deckArray[index][0]);
        $("#backcard_info").text(deckArray[index][1]);
        $("#fade").fadeIn(1000);
    });
    
    //Iterate through the array
    $("#next_button").click(function() {
        flip_back();
        setTimeout(function(){ 
            index ++;
            if (index > deckArray.length - 1 ) {
                $("p").fadeOut(function() {
                    $("#card_info").text('End of the deck');
                    $("#backcard_info").text('End of the deck');
                    $("p").fadeIn();
                    index = deckArray.length - 1;
                });
            }else{
                $("p").fadeOut(function() {
                    $("#card_info").text(deckArray[index][0]);
                    $("#backcard_info").text(deckArray[index][1]);
                    $("p").fadeIn();
                });
            }}, 250);
    });


  $("#back_button").click(function() {
    flip_back();
    setTimeout(function(){ 
        index--;
        if (index < 0){
            index = 0;
        } else { 
            $("p").fadeOut(function() {
            $("#card_info").text(deckArray[index][0]);
            $("#backcard_info").text(deckArray[index][1]);
            $("p").fadeIn();
            });
            }}, 250);
});
});