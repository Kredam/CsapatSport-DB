var update_team = document.querySelectorAll("[id='specific_team_update']");
for (const teamName of update_team) {
    teamName.addEventListener('click', ()=>{
        selected_team_to_update = teamName.getAttribute('data-team')
        document.getElementById('teams_name').value = selected_team_to_update.split('_').join(' ');
    })
}

var delete_team = document.querySelectorAll("[id='remove_record']");
for (const deleteTeamElement of delete_team) {
    deleteTeamElement.addEventListener('click', ()=>{
        selected_team_to_delete = deleteTeamElement.getAttribute('data-team')
        document.getElementById('team_to_remove').value = selected_team_to_delete.split('_').join(' ')
    })
}


