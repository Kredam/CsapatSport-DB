class ClubsDAO:
    def __init__(self, database):
        self.database = database
        print("SIKERES LÉTREHOZÁS")

    def listClubs(self):
        self.database.cursor.execute("SELECT * FROM Clubs  ORDER BY points DESC ")


    def searchClub(self, key):
        self.database.cursor.execute(f"SELECT * FROM Clubs WHERE name = '{key}'")
        self.listClubs()

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

