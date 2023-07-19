// for button 'Player vs Pc' with id '#player_vs_pc' on welcome page to direct to "player_vs_pc.html"
document.getElementById("player_vs_pc").addEventListener("click", function(){
    window.location.href = "/start/game/vs_pc";
});

// for button 'Player vs Player' with id 'player_vs_player' on home page to direct to "player_vs_player.html"
document.getElementById("chat_room").addEventListener("click", function(){
    window.location.href = "/start/game/chat_room";
})

// for button 'Group vs Group' with id '#group_vs_group' on home page to direct to "group_vs_group.html"
document.getElementById("player_vs_player").addEventListener("click", function(){
    window.location.href = "/start/game/player_vs_player";
})
