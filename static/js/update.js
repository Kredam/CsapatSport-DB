var team_names = document.querySelectorAll("[id='specific_team_update']");
for (const teamName of team_names) {
    teamName.addEventListener('click', ()=>{
        selected_team_to_update = teamName.getAttribute('data-teamname')
        document.getElementById('teams_name').value = selected_team_to_update;
    })
}


