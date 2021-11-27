class ClubsDAO:
    def __init__(self, database):
        self.database = database
        print("SIKERES LÉTREHOZÁS")

    def listClubs(self):
        self.database.cursor.execute("SELECT * FROM Clubs  ORDER BY points DESC ")


    def searchClub(self, key):
        self.database.cursor.execute(f"SELECT * FROM Clubs WHERE name = '{key}'")

    def updateClub(self, club, abbr, badge, league, season, wins, draws, loss):
        self.database.cursor.execute(f"UPDATE Clubs SET abbreviation = '{abbr}', badge = '{badge}', league = '{league}', season = '{season}' , W = {wins}, D = {draws}, L={loss} WHERE name = '{club}'")
        self.database.db.commit()
        self.listClubs()

    def addClub(self, club, abbr, badge, league, season, wins, draws, loss):
        self.database.cursor.execute(f"INSERT INTO Clubs (name, league, season, abbreviation, badge, W, D, L) VALUES ('{club}','{league}', {season},'{abbr}','{badge}', {wins}, {draws}, {loss})")
        self.database.db.commit()
        self.listClubs()

    def removeClub(self, key):
        self.database.cursor.execute(f"DELETE FROM Clubs WHERE name = '{key}'")
        self.database.db.commit()
        self.listClubs()

    def scorersByTeam(self):
        self.database.cursor.execute(
            "SELECT (SELECT badge FROM Clubs WHERE Clubs.name = Scorers.team) AS badge, team, Count(team) AS team_apperance, league, SUM(goals) AS all_goals FROM Scorers GROUP BY Scorers.team ORDER BY team_apperance DESC")
        teams_data_dict = {'name': '', 'badge': '', 'league': '', 'all_goals': 0, 'team_apperance': 0}
        teams_list = list()
        for team in self.database.cursor:
            teams_data_dict['name'] = team['team']
            teams_data_dict['badge'] = team['badge']
            teams_data_dict['league'] = team['league']
            teams_data_dict['all_goals'] = team['all_goals']
            teams_data_dict['team_apperance'] = team['team_apperance']
            teams_list.append(teams_data_dict.copy())
        return teams_list
