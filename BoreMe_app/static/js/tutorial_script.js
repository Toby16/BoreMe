/* for button 'Tutorial' with id '#tutorial_button' on welcome page to direct to "tutorial.html" */
document.getElementById("tutorialButton").addEventListener("click", function(){
    window.location.href = "/tutorial";
});

document.getElementById("loginButton").addEventListener("click", function() {
    window.location.href = "/login";
});

/* remove flashed message after 3 seconds */
const flashMessage = document.getElementById("flash_message")

setTimeout(function() {
    flashMessage.style.display = "none";

}, 10000);