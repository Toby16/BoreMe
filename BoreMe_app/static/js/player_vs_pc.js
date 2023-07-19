$(document).ready(function () {
  $('#game_status_value').click(function () {

    // Update the game status to "Generating random number..."
    $('#game_status_value').text('Generating random number...');

    // Make an AJAX request to generate the random number after a delay
    setTimeout(function () {
      $.ajax({
        type: 'POST',
        url: '/start/game/vs_pc',
        success: function (response) {
          // Update the game status with the generated random number
          console.log("target number ->", response.target_number) /* will remove later - for testing */
          $('#game_status_value').text('Random number generated');
        },
        error: function (error) { 
          console.log('AJAX request error:', error);
        }
      });
    }, 4000); // Delay of 4 seconds (4000 milliseconds)
  });
});


$(document).ready(function () {
  $('#player_vs_pc_form').submit(function (e) {
    e.preventDefault(); // Prevent default form submission behavior

    // Create an object with the user input
    var formData = {
      user_input: $('#user_input').val()
    };

    $('#player_status_value').text("checking...");

    // Make an AJAX request to process the form data
    setTimeout(function () {
      $.ajax({
        type: 'POST',
        url: '/start/game/vs_pc/player',
        data: JSON.stringify(formData), // Convert the object to JSON
        contentType: 'application/json', // Set the content type to JSON
        success: function (response) {
          // Update the player status with the response
          //console.log("player status:", response.player_status); /* for testing */
          $('#player_status_value').text(response.player_status);
          $("#player_score_value").text(response.player_score);
          $("#pc_score_value").text(response.pc_score);
          $("#game_status_value").text(response.game_status);
          console.log("player guess:", formData.user_input)
          //console.log("player_score:", response.player_score) // for testing
          //console.log("pc_score:", response.pc_score) // for testing

          // If player's guess is incorrect, make a request for the PC's guess
          if (response.player_status !== "Correct") {
            // Update the game status to "PC guessing..."
            $('#pc_status_value').text('PC guessing...');

            // Make an AJAX request to get the PC's guess
            setTimeout(function(){
              $.ajax({
                type: "POST",
                url: "/start/game/vs_pc/pc",
                success: function (pcResponse) {
                  // Update the game status with the PC's guess
                  console.log("PC guess:", pcResponse.pc_input) /* for testing */
                  //$('#game_status_value').text('PC guess: ' + pcResponse.pc_guess);
                  $('#pc_status_value').text(pcResponse.pc_status);
                  $('#pc_score_value').text(pcResponse.pc_score);
                  $("#game_status_value").text(pcResponse.game_status);
                },
                error: function (error) {
                  console.log('AJAX request error:', error);
                }
              })
            }, 2000);
          }
        },
        error: function (error) {
          console.log('AJAX request error:', error);
        }
      });
    }, 2000);
  });
});

/*
$(document).ready(function () {
  $('#player_vs_pc_form').submit(function (e) {
    e.preventDefault(); // Prevent default form submission behavior

    // Create an object with the user input
    var formData = {
      user_input: $('#user_input').val()
    };

    // Make an AJAX request to process the form data
    $.ajax({
      type: 'POST',
      url: '/start/game/vs_player_play',
      data: JSON.stringify(formData), // Convert the object to JSON
      contentType: 'application/json', // Set the content type to JSON
      success: function (response) {
        // Update the player status with the response
        console.log("player status:", response.player_status); //for testing
        $('#player_status_value').text(response.player_status);
        $("#player_score_value").text(response.player_score)
        $("#pc_score_value").text(response.pc_score)
        console.log("player_score:", response.player_score) // for testing
        console.log("pc_score:", response.pc_score) // for testing
      },
      error: function (error) {
        console.log('AJAX request error:', error);
      }
    });
  });
});
*/
