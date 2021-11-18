CREATE TABLE Csapatok(  name VARCHAR(50) NOT NULL,
                        abbreviation VARCHAR(3),
                        stadium VARCHAR(100),
                        badge VARCHAR(100),
                        points INT,
                        matches_played INT,
                        W INT,
                        D INT,
                        L INT);


CREATE TABLE Jatekosok( id INT,
                        club VARCHAR(50) NOT NULL,
                        name VARCHAR(50),
                        position VARCHAR(30),
                        number INT);


CREATE TABLE Meccsek(   team VARCHAR(50) NOT NULL,
                        enemy_team VARCHAR(50) NOT NULL,
                        takes_place DATE);


CREATE TABLE Stadion(   team VARCHAR(50) NOT NULL,
                        name VARCHAR(100));


ALTER TABLE Csapatok ADD PRIMARY KEY(name);
ALTER TABLE Stadion ADD PRIMARY KEY(name);
ALTER TABLE Jatekosok ADD PRIMARY KEY(id);
ALTER TABLE Meccsek ADD PRIMARY KEY(team);

ALTER TABLE Jatekosok ADD FOREIGN KEY (club) REFERENCES Csapatok(name) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Meccsek ADD FOREIGN KEY (team) REFERENCES Csapatok(name) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Stadion ADD FOREIGN KEY (team) REFERENCES Csapatok(name) ON UPDATE CASCADE ON DELETE CASCADE;

