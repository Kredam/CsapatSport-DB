class TrainingGroundsDAO:
    def __init__(self, database):
        self.database = database
# mysql.connector.errors.IntegrityError
    def listTrainingGrounds(self):
        self.database.cursor.execute(
            f"SELECT badge, TrainingGrounds.team, TrainingGrounds.name AS name, city FROM TrainingGrounds INNER JOIN Clubs ON Clubs.name = TrainingGrounds.team")

    def searchTrainingGround(self, key):
        self.database.cursor.execute(
            f"SELECT badge, TrainingGrounds.team, TrainingGrounds.name AS name, city FROM TrainingGrounds INNER JOIN Clubs ON Clubs.name = TrainingGrounds.team WHERE TrainingGrounds.name = '{key}'")

    def createTrainingGround(self, team, name, city):
        self.database.cursor.execute(f"INSERT INTO TrainingGrounds(team, name, city) VALUES ('{team}', '{name}', '{city}')")
        self.database.db.commit()
        self.listTrainingGrounds()

    def removeTrainingGround(self, key):
        self.database.cursor.execute(f"DELETE FROM TrainingGrounds WHERE name = '{key}'")
        self.database.db.commit()
        self.listTrainingGrounds()

    def updateTrainingGround(self, team, name, city):
        print(team,name,city)
        self.database.cursor.execute(f"UPDATE TrainingGrounds SET team = '{team}', city = '{city}' WHERE name = '{name}'")
        self.database.db.commit()
        self.listTrainingGrounds()

