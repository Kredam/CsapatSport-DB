class OwnersDAO:
    def __init__(self, database):
        self.database = database

    def listOwners(self):
        self.database.cursor.execute(f"SELECT company, id, name, team, (SELECT badge FROM Clubs WHERE Clubs.name = Owners.team) AS badge FROM Owners")

    def removeOwner(self, key):
        self.database.cursor.execute(f"DELETE FROM Owners WHERE id = {key}")
        self.database.db.commit()
        self.listOwners()

    def updateOwner(self, owner_id, company, name, team):
        self.database.cursor.execute(f"UPDATE Owners SET company = '{company}', name='{name}', team='{team}' WHERE id = {owner_id}")
        self.database.db.commit()
        self.listOwners()

    def searchOwner(self, key):
        self.database.cursor.execute(f"SELECT company, name, id, team, (SELECT badge FROM Clubs WHERE Clubs.name = Owners.team) AS badge FROM Owners WHERE Owners.team = '{key}'")

    def createOwner(self, company, name, team):
        self.database.cursor.execute(f"INSERT INTO Owners(company, name, team) VALUES ('{company}', '{name}', '{team}')")
        self.database.db.commit()
        self.listOwners()
