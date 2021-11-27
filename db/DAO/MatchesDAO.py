class MatchesDAO:
    def __init__(self, database):
        self.database = database

    def listMatches(self):
        self.database.cursor.execute("SELECT team, id, badge AS team_badge, enemy_team, (SELECT badge FROM Clubs WHERE Clubs.name = Matches.enemy_team) AS enemy_team_badge, takes_place FROM Matches INNER JOIN Clubs on Clubs.name = Matches.team")

    def removeMatch(self, key):
        self.database.cursor.execute(f"DELETE FROM Matches WHERE id = '{key}'")
        self.database.db.commit()
        self.listMatches()

    def createMatch(self, team, enemy_team, takes_place):
        self.database.cursor.execute(f"INSERT INTO Matches(team, enemy_team, takes_place) VALUES ('{team}', '{enemy_team}', {takes_place})")
        self.database.db.commit()
        self.listMatches()

    def updateMatch(self, match_id, team, enemy_team, takes_place):
        self.database.cursor.execute(f"UPDATE Matches SET team = '{team}', enemy_team = '{enemy_team}',  takes_place='{takes_place}' WHERE id = {match_id}")
        self.database.db.commit()
        self.listMatches()

    def searchMatch(self, key):
        self.database.cursor.execute(f"SELECT team, id, badge AS team_badge, enemy_team, (SELECT badge FROM Clubs WHERE Clubs.name = Matches.enemy_team) AS enemy_team_badge, takes_place FROM Matches INNER JOIN Clubs on Clubs.name = Matches.team WHERE team = '{key}'")
