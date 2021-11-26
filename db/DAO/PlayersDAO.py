class PlayerDAO:
    def __init__(self, database):
        self.database = database

    def listPlayers(self):
        self.database.cursor.execute("SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team FROM Players INNER JOIN Clubs ON Clubs.name = Players.team")


    def searchPlayer(self, key):
        self.database.cursor.execute(f"SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team  FROM Players INNER JOIN Clubs on Clubs.name = Players.team WHERE Players.name = '{key}'")
        self.database.db.commit()
        self.listPlayers()

    def updatePlayer(self, id, team, position, shirt_number):
        self.database.cursor.execute(f"UPDATE Players SET team = '{team}', position = '{position}', number = {shirt_number} WHERE id = {id}")
        self.database.db.commit()
        self.listPlayers()

    def createPlayer(self, team, name, position, shirt_number ):
        self.database.cursor.execute(f"INSERT INTO Players(team, name, position, number) VALUES ('{team}','{name}','{position}',{shirt_number})")
        self.database.db.commit()
        self.listPlayers()

    def removePlayer(self, key):
        self.database.cursor.execute(f"DELETE FROM Players WHERE id = '{key}'")
        self.database.db.commit()
        self.listPlayers()
