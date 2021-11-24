// Csapatok update
var update_team = document.querySelectorAll("[id='specific_team_update']");
for (const teamName of update_team) {
    teamName.addEventListener('click', ()=>{
        selected_team_to_update = teamName.getAttribute('data-team')
        document.getElementById('update_team_name').value = selected_team_to_update.split('_').join(' ');
    })
}

var delete_team = document.querySelectorAll("[id='remove_record_team']");
for (const deleteTeamElement of delete_team) {
    deleteTeamElement.addEventListener('click', ()=>{
        selected_team_to_delete = deleteTeamElement.getAttribute('data-team')
        console.log(selected_team_to_delete)
        document.getElementById('team_to_remove').value = selected_team_to_delete.split('_').join(' ');
    })
}

// Játékosok
var update_player = document.querySelectorAll("[id='specific_team_update']");
for (const playerName of update_player) {
    playerName.addEventListener('click', ()=>{
        selected_player_id = playerName.getAttribute('data-id')
        document.getElementById('update_player_id').value = selected_player_id;
        selected_player_name = playerName.getAttribute('data-player-name')
        document.getElementById('update_player_name').value = selected_player_name.split('_').join(' ');
    })
}

var delete_player = document.querySelectorAll("[id='remove_record_player']");
for (const deletePlayerElement of delete_player) {
    deletePlayerElement.addEventListener('click', ()=>{
        selected_player_to_delete = deletePlayerElement.getAttribute('data-player-id')
        console.log(selected_player_to_delete)
        document.getElementById('player_to_delete').value = selected_player_to_delete;
    })
}
