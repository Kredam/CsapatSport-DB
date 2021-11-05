CREATE TABLE Csapatok(  name VARCHAR(50) UNIQUE PRIMARY KEY NOT NULL,
                        abbreviation VARCHAR(3),
                        stadium VARCHAR(60),
                        badge VARCHAR(100),
                        points INT,
                        position INT,
                        matches_played INT,
                        W INT,
                        D INT,
                        L INT);


CREATE TABLE Jatekosok( id INT PRIMARY KEY,
                        club VARCHAR(50),
                        name VARCHAR(50),
                        position VARCHAR(30),
                        number INT,
                        FOREIGN KEY (club) REFERENCES Csapatok(name)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE);


CREATE TABLE Meccsek(   team VARCHAR(50) NOT NULL,
                        PRIMARY KEY(team),
                        enemy_team VARCHAR(50) NOT NULL,
                        takes_place DATETIME,
                        FOREIGN KEY (team) REFERENCES Csapatok(name)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE);


CREATE TABLE Stadion(   team VARCHAR(50),
                        name VARCHAR(100) PRIMARY KEY,
                        FOREIGN KEY (team) REFERENCES Csapatok(name)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE);
