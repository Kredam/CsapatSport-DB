CREATE TABLE Championship(  league VARCHAR(50),
                            season YEAR);

CREATE TABLE Clubs(     name VARCHAR(50) NOT NULL,
                        league VARCHAR(50),
                        season YEAR,
                        abbreviation VARCHAR(3),
                        badge VARCHAR(100),
                        points INT,
                        matches_played INT,
                        W INT,
                        D INT,
                        L INT);

CREATE TABLE Scorers(   team VARCHAR(50) NOT NULL,
                        league VARCHAR(50),
                        name VARCHAR(100),
                        goals INT);

CREATE TABLE Players(   team VARCHAR(50) NOT NULL,
                        name VARCHAR(50),
                        position VARCHAR(30),
                        number INT);

CREATE TABLE Matches(   team VARCHAR(50) NOT NULL,
                        enemy_team VARCHAR(50) NOT NULL,
                        takes_place DATE);

CREATE TABLE Stadiums(  team VARCHAR(50) NOT NULL,
                        name VARCHAR(100));

CREATE TABLE Managers(  name VARCHAR(50),
                        nationality VARCHAR(50),
                        team VARCHAR(50) NOT NULL);

CREATE TABLE Owners (   company VARCHAR(100),
                        boss VARCHAR(50),
                        team VARCHAR(50) NOT NULL);

ALTER TABLE Clubs ADD PRIMARY KEY(name);
ALTER TABLE Stadiums ADD PRIMARY KEY(name);
ALTER TABLE Owners ADD PRIMARY KEY(company);
ALTER TABLE Championship ADD PRIMARY KEY(league, season);
ALTER TABLE Matches ADD id INT PRIMARY KEY AUTO_INCREMENT;
ALTER TABLE Players ADD id INT PRIMARY KEY AUTO_INCREMENT;
ALTER TABLE Scorers ADD id INT PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE Players ADD FOREIGN KEY (team) REFERENCES Clubs(name) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Owners ADD FOREIGN KEY (team) REFERENCES Clubs(name) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Matches ADD FOREIGN KEY (team) REFERENCES Clubs(name) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Stadiums ADD FOREIGN KEY (team) REFERENCES Clubs(name) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Scorers ADD FOREIGN KEY (league) REFERENCES Championship(league) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Scorers ADD FOREIGN KEY (team) REFERENCES Clubs(name) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Clubs ADD FOREIGN KEY(league, season) REFERENCES Championship(league, season) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE Managers ADD FOREIGN KEY(team) REFERENCES Clubs(name) ON UPDATE CASCADE ON DELETE CASCADE;
