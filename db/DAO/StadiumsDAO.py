class StadiumsDAO:
    def __init__(self, database):
        self.database = database

    def listStadium(self):
        self.database.cursor.execute(
            f"SELECT badge, Stadiums.team, Stadiums.name AS name, city FROM Stadiums INNER JOIN Clubs ON Clubs.name = Stadiums.team")

    def searchStadium(self, key):
        self.database.cursor.execute(
            f"SELECT badge, Stadiums.team, Stadiums.name AS name, city FROM Stadiums INNER JOIN Clubs ON Clubs.name = Stadiums.team WHERE Stadiums.name = '{key}'")

    def createStadium(self, team, name, city):
        self.database.cursor.execute(f"INSERT INTO Stadiums(team, name, city) VALUES ('{team}', '{name}', '{city}')")
        self.database.db.commit()
        self.listStadium()

    def removeStadium(self, key):
        self.database.cursor.execute(f"DELETE FROM Stadiums WHERE name = '{key}'")
        self.database.db.commit()
        self.listStadium()

    def updateStadium(self, team, name, city):
        self.database.cursor.execute(f"UPDATE Stadiums SET team = '{team}', city = '{city}' WHERE name = '{name}'")
        self.database.db.commit()
        self.listStadium()
