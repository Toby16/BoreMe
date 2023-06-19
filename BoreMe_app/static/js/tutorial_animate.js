/* for paragraph with id '#tutorial_intro_text' */
const tut_intro_text = "In this tutorial, we'll guide you through the basics of playing BoreMe, a thrilling game of strategy and teamwork.";
const tut_intro_paragraph = document.getElementById("tutorial_intro_text");
let tut_intro_counter = 0;

function tut_intro_typeWriter() {
    if (tut_intro_counter < tut_intro_text.length) {
        tut_intro_paragraph.textContent += tut_intro_text.charAt(tut_intro_counter)
        tut_intro_counter++;
        setTimeout(tut_intro_typeWriter, 30); // Adjust typing speed by changing the timeout value (in milliseconds)
    }
};


//------------------------------------------------------------------------------------------------
/* for paragraph with id '#game_objective_text' */
const game_objective_text = "The goal of BoreMe is to compete against other teams and be the first to reach the randomly generated target number. You'll need to collaborate with your team members and strategize your moves wisely.";
const game_objective_paragraph = document.getElementById("game_objective_text");
let game_objective_counter = 0;

function game_objective_typeWriter() {
    if (game_objective_counter < game_objective_text.length) {
      game_objective_paragraph.textContent += game_objective_text.charAt(game_objective_counter);
      game_objective_counter++;
      setTimeout(game_objective_typeWriter, 30); // Adjust typing speed by changing the timeout value (in milliseconds)
    }
};
  

//-----------------------------------------------------------------------
/* for list with id '#game_rules_list' */
const game_rules_text = [
    "The game session can have a maximum of 4 teams, with each team consisting of a maximum of four players.",
    "The computer generates a random target number within a certain range at the beginning of each game session, depending on the level of difficulty.",
    "Each team takes turns, and any player in each team can freely choose any random number from the specified range.",
    "The game continues with the next team taking their turn until a team guesses the correct number.",
    "After each guess, the computer provides clues to help teams refine their guesses.",
    "If a team correctly guesses the target number, they earn 1 point for that round and proceed to the next round.",
    "The game continues with new target numbers generated for each round.",
    "After 10 rounds, the team with the most points wins the game."
];
const game_rules_list = document.getElementById("game_rules_list");
let game_rules_counter = 0;
let currentLetterIndex = 0;

function game_rules_typeWriter() {
    if (game_rules_counter < game_rules_text.length) {
        const listItem = document.createElement("li");
        game_rules_list.appendChild(listItem);
        
        const typeWriterInterval = setInterval(() => {
            if (currentLetterIndex < game_rules_text[game_rules_counter].length) {
                listItem.textContent += game_rules_text[game_rules_counter][currentLetterIndex];
                currentLetterIndex++;
            } else {
                clearInterval(typeWriterInterval);
                game_rules_counter++;
                currentLetterIndex = 0;
                setTimeout(game_rules_typeWriter, 100); // Adjust typing speed by changing the timeout value (in milliseconds)
            }
        }, 7);
    }
};




//-------------------------------------------------------------------------
 /* for paragraph with id '#team_communication_text' */
const team_communication_text = "To enhance your teamwork, utilize the built-in chat feature to communicate with your team members. Discuss strategies, share insights from clues, and coordinate your guessing efforts.";
const team_communication_paragraph = document.getElementById("team_communication_text");
let team_communication_counter = 0;

function team_communication_typeWriter() {
    if (team_communication_counter < team_communication_text.length) {
        team_communication_paragraph.textContent += team_communication_text.charAt(team_communication_counter);
        team_communication_counter++;
        setTimeout(team_communication_typeWriter, 30);
    }
}



//------------------------------------------------------------------------
/* for paragraph with id '#team_chat_text' */
const team_chat_text = " Use the team chat to communicate exclusively with your team members. Share your guesses, discuss possible strategies, and collaborate effectively.";
const team_chat_paragraph = document.getElementById("team_chat_text");
let team_chat_counter = 0;
 
function team_chat_typeWriter() {
    if (team_chat_counter < team_chat_text.length) {
        team_chat_paragraph.textContent += team_chat_text.charAt(team_chat_counter);
        team_chat_counter++;
        setTimeout(team_chat_typeWriter, 30);
    }
}



//------------------------------------------------------------------------
/* for paragraph with id '#general_chat_text' */
const general_chat_text = " Engage in the general chat section to communicate with all players in the game, including opponents. Share your excitement, challenge your opponents, and enjoy a friendly competition";
const general_chat_paragraph = document.getElementById("general_chat_text");
let general_chat_counter = 0;
 
function general_chat_typeWriter() {
    if (general_chat_counter < general_chat_text.length) {
        general_chat_paragraph.textContent += general_chat_text.charAt(general_chat_counter);
        general_chat_counter++;
        setTimeout(general_chat_typeWriter, 30);
    }
}




//--------------------------------------------------------------------
/* for list with id '#getting_started_list' */
const getting_started_text = [
    "Create an account or log in to access your existing account.",
    "Join or create a team with your friends or other players.",
    "Wait for your team's turn to make a guess.",
    "Analyze the clues provided by the computer and discuss possible numbers with your team.",
    "Select a number within the specified range as your team's guess.",
    "Submit your guess and eagerly await the next round of clues.",
    "If your team correctly guesses the target number, celebrate and earn 1 point for that round.",
    "Continue the guessing and clue analysis process for 10 rounds.",
    "At the end of 10 rounds, the team with the highest number of points wins the game.",
    "Celebrate your victory and enjoy the thrill of teamwork in BoreMe!"
]
const getting_started_list = document.getElementById("getting_started_list");
let getting_started_counter = 0;
let getting_started_LetterIndex = 0;

function getting_started_typeWriter() {
    if (getting_started_counter < getting_started_text.length) {
        const getting_started_listItem = document.createElement("li");
        getting_started_list.appendChild(getting_started_listItem);
        
        const getting_started_typeWriterInterval = setInterval(() => {
            if (getting_started_LetterIndex < getting_started_text[getting_started_counter].length) {
                getting_started_listItem.textContent += getting_started_text[getting_started_counter][getting_started_LetterIndex];
                getting_started_LetterIndex++;
            } else {
                clearInterval(getting_started_typeWriterInterval);
                getting_started_counter++;
                getting_started_LetterIndex = 0;
                setTimeout(getting_started_typeWriter, 100); // Adjust typing speed by changing the timeout value (in milliseconds)
            }
        }, 8);
    }
};


//----------------------------------------------------------------
/* for paragraph with id '#ending_text' */
const ending_text = " Remember, effective communication, strategic thinking, and accurate guessing are crucial to winning the BoreMe Game. Good luck, and have fun!";
const ending_paragraph = document.getElementById("ending_text");
let ending_counter = 0;
 
function ending_typeWriter() {
    if (ending_counter < ending_text.length) {
        ending_paragraph.textContent += ending_text.charAt(ending_counter);
        ending_counter++;
        setTimeout(ending_typeWriter, 30);
    }
}
 



//--------------------------------
/* calling all necessary functions */
tut_intro_typeWriter();
game_objective_typeWriter();
game_rules_typeWriter();
team_communication_typeWriter();
team_chat_typeWriter();
general_chat_typeWriter();
getting_started_typeWriter();
setTimeout(ending_typeWriter, 7000);

/* for button 'Back' with id '#back_button' on tutorial page to direct back to "welcome.html" */
document.getElementById("back_button").addEventListener("click", function(){
    window.location.href = "/";
});