class ManagersDAO:
    def __init__(self, database):
        self.database = database

    def searchManager(self, key):
        self.database.cursor.execute(
            f"SELECT team, name, nationality id, (SELECT badge FROM Clubs WHERE Clubs.name = team) AS badge FROM Managers WHERE Managers.team = '{key}'")

    def listManagers(self):
        self.database.cursor.execute(
            "SELECT team, name, nationality, id,(SELECT badge FROM Clubs WHERE Clubs.name = team) AS badge FROM Managers")

    def removeManager(self, key):
        self.database.cursor.execute(f"DELETE FROM Managers WHERE id = {key}")
        self.database.db.commit()
        self.listManagers()

    def createManager(self, team, nationality, name):
        self.database.cursor.execute(f"INSERT INTO Managers(name, nationality, team) VALUES ('{name}', '{nationality}', '{team}')")
        self.database.db.commit()
        self.listManagers()

    def updateManager(self, manager_id, team, nationality, name):
        self.database.cursor.execute(f"UPDATE Managers SET team='{team}', nationality='{nationality}', name='{name}' WHERE id = {manager_id}")
        self.database.db.commit()
        self.listManagers()

