// function to flip the card
function flip() {
    $('.card').toggleClass('flipped');
};


//function to check if back of the card being displayed is present in html
//Used to fix z-indexing problem when iterating through 
//the deck while back of card is showing..
function flip_back() {
    var cardFlipped = document.getElementsByClassName('card flipped');
    if (cardFlipped.length > 0) {
        console.log('Back of card is showing'); 
        flip();
    } else {
        console.log('Front of card is showing');
    };
};


//Flip through deck of cards
$(document).ready(function() {
    $.ajax({ //used to convert python tuple into JS array
        url: '/shuffleCard?deckID='+document.getElementById("deckID").value,
        success: function(data) {
            console.log('retrieved python list');
            temp = JSON.parse(data);

            console.log("New Array: ", temp)

            //If there are no cards in deck, display deck is empty
            if (temp == null){
                var deckArray = [['Deck is empty', 'Deck is empy']];
            }else{
                var deckArray = temp;
            }

            //Setting initial values for deck
            var index = 0;
            $(document).ready(function() {
                $("#card_info").text(deckArray[index][0]);
                $("#backcard_info").text(deckArray[index][1]);
                $("#fade").fadeIn(1000);
            });

            //Iterate to next card in deck
            $("#next_button").click(function() {
                flip_back();
                setTimeout(function() {
                    index++;
                    if (index > deckArray.length - 1) {
                        $("p").fadeOut(function() {
                            $("#card_info").text('End of the deck');
                            $("#backcard_info").text('End of the deck');
                            $("p").fadeIn();
                            index = deckArray.length - 1;
                        });
                    } else {
                        $("p").fadeOut(function() {
                            $("#card_info").text(deckArray[index][0]);
                            $("#backcard_info").text(deckArray[index][1]);
                            $("p").fadeIn();
                        });
                    }
                }, 250);
            });

            //Iterate to previous card in deck.
            $("#back_button").click(function() {
                flip_back();
                setTimeout(function() {
                    index--;
                    if (index < 0) {
                        index = 0;
                    } else {
                        $("p").fadeOut(function() {
                            $("#card_info").text(deckArray[index][0]);
                            $("#backcard_info").text(deckArray[index][1]);
                            $("p").fadeIn();
                        });
                    }
                }, 250);
            });


        }
    });

});



         
