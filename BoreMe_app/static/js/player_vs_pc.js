
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
          console.log("target number:", response.target_number) /* will remove later - for testing */
          $('#game_status_value').text('Random number generated: ' + response.target_number);
        },
        error: function (error) { 
          console.log('AJAX request error:', error);
        }
      });
    }, 4000); // Delay of 4 seconds (4000 milliseconds)
  });
});


/*
$(document).ready(function () {
  $('#player_vs_pc_form').submit(function (e) {
    e.preventDefault(); // Prevent default form submission behavior

    // Make an AJAX request to process the form data
    $.ajax({
      type: 'POST',
      url: '/start/game/vs_pc',
      data: $(this).serialize(), // Serialize the form data
      success: function (response) {
        // Update the player status with the response
        console.log("player status:", response.player_status); // for testing
        $('#player_status_value').text(response.player_status);
      },
      error: function (error) {
        console.log('AJAX request error:', error);
      }
    });
  });
});
*/


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
        console.log("player status:", response.player_status); /* for testing */
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
