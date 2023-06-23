/* for button 'Tutorial' with id '#tutorial_button' on welcome page to direct to "tutorial.html" */
document.getElementById("tutorialButton").addEventListener("click", function(){
    window.location.href = "/tutorial";
});

document.getElementById("loginButton").addEventListener("click", function() {
    window.location.href = "/login";
});