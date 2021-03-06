// Csapatok update
var update_team = document.querySelectorAll("[id='specific_team_update']");
for (const team of update_team) {
    team.addEventListener('click', ()=>{
        let selected_team_to_update = team.getAttribute('data-team')
        document.getElementById('update_team_name').value = selected_team_to_update.split('_').join(' ');
    })
}

var teams_delete = document.querySelectorAll("[id='remove_record_team']");
for (const team of teams_delete) {
    team.addEventListener('click', ()=>{
        let selected_team_to_delete = team.getAttribute('data-team')
        document.getElementById('record_to_delete').value = selected_team_to_delete.split('_').join(' ');
        document.forms["remove_form"].submit();
    })
}
//---------------------------------------------------------
// Players
var players_update = document.querySelectorAll("[id='specific_team_update']");
for (const player of players_update) {
    player.addEventListener('click', ()=>{
        selected_player_id = player.getAttribute('data-id')
        document.getElementById('update_player_id').value = selected_player_id;
        selected_player_name = player.getAttribute('data-player-name')
        document.getElementById('update_player_name').value = selected_player_name.split('_').join(' ');
    })
}

var players_delete = document.querySelectorAll("[id='remove_record_player']");
for (const player of players_delete) {
    player.addEventListener('click', ()=>{
        selected_player_to_delete = player.getAttribute('data-player-id')
        document.getElementById('record_to_delete').value = selected_player_to_delete;
        document.forms["remove_form"].submit();
    })
}
//---------------------------------------------------------
// Manager
var update_manager = document.querySelectorAll("[id='specific_manager_update']");
for (const manager of update_manager) {
    manager.addEventListener('click', ()=>{
        selected_manager_id = manager.getAttribute('data-id')
        document.getElementById('managers_id').value = selected_manager_id;
    })
}

var managers = document.querySelectorAll("[id='remove_record_manager']");
for (const manager of managers) {
    manager.addEventListener('click', ()=>{
        selected_manager_to_delete = manager.getAttribute('data-id')
        document.getElementById('record_to_delete').value = selected_manager_to_delete;
        console.log(document.getElementById('record_to_delete').value)
        document.forms["remove_form"].submit();
    })
}
//---------------------------------------------------------
// Matches
var update_matches = document.querySelectorAll("[id='specific_match_update']");
for (const manager of update_matches) {
    manager.addEventListener('click', ()=>{
        selected_match_to_update = manager.getAttribute('data-id')
        document.getElementById('match_id').value = selected_match_to_update;
    })
}

var matches = document.querySelectorAll("[id='remove_record_matches']");
for (const match of matches) {
    match.addEventListener('click', ()=>{
        selected_match_to_delete = match.getAttribute('data-id')
        document.getElementById('record_to_delete').value = selected_match_to_delete;
        document.forms["remove_form"].submit();
    })
}
//---------------------------------------------------------
// Stadium
var stadiums_update = document.querySelectorAll("[id='specific_stadium_update']");
for (const stadium of stadiums_update) {
    stadium.addEventListener('click', ()=>{
        selected_stadium_name = stadium.getAttribute('data-stadium-name')
        document.getElementById('update_stadium_name').value = selected_stadium_name.split('_').join(' ');
    })
}

var stadiums = document.querySelectorAll("[id='remove_record_stadium']");
for (const stadium of stadiums) {
    stadium.addEventListener('click', ()=>{
        selected_stadium_to_delete = stadium.getAttribute('data-stadium-name')
        document.getElementById('record_to_delete').value = selected_stadium_to_delete.split('_').join(' ');
        document.forms["remove_form"].submit();
    })
}
//---------------------------------------------------------
// Owner
var update_owner = document.querySelectorAll("[id='specific_owner_update']");
for (const owner of update_owner) {
    owner.addEventListener('click', ()=>{
        selected_owner_id = owner.getAttribute('data-id')
        document.getElementById('owner_id').value = selected_owner_id;
    })
}

var owners = document.querySelectorAll("[id='remove_record_owner']");
for (const owner of owners) {
    owner.addEventListener('click', ()=>{
        selected_owner_to_delete = owner.getAttribute('data-id')
        document.getElementById('record_to_delete').value = selected_owner_to_delete;
        console.log(document.getElementById('record_to_delete').value)
        document.forms["remove_form"].submit();
    })
}//---------------------------------------------------------
// Training Grounds
var update_grounds = document.querySelectorAll("[id='specific_ground_update']");
for (const ground of update_grounds) {
    ground.addEventListener('click', ()=>{
        selected_ground_name = ground.getAttribute('data-ground-name')
        document.getElementById('update_ground').value = selected_ground_name.split('_').join(' ');
    })
}

var grounds = document.querySelectorAll("[id='remove_record_ground']");
for (const ground of grounds) {
    ground.addEventListener('click', ()=>{
        selected_ground_name = ground.getAttribute('data-ground-name')
        document.getElementById('record_to_delete').value = selected_ground_name.split('_').join(' ');
        document.forms["remove_form"].submit();
    })
}

