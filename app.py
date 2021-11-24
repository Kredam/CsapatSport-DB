from flask import Flask, redirect, url_for, render_template, request
import os
from db import database
from other import scraper


app = Flask(__name__, template_folder=os.path.abspath('client/templates'))
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/teams', methods=['GET', 'POST'])
def teams():
    if request.method == 'POST':
        update_button = request.form.get('update')
        list_button = request.form.get('list')
        add_button = request.form.get('create')
        remove_button = request.form.get('remove_button')
        search_add_field = request.form.get('search_add_field')
        club = request.form.get('teams_name')
        league_name = request.form.get('league_name')
        league_season = request.form.get('league_season')
        badge = request.form.get('badge')
        abbr = request.form.get('abbreviation')
        wins = request.form.get('wins')
        draws = request.form.get('draws')
        loss = request.form.get('loss')
        if list_button is not None and search_add_field.strip() != "":
            print(request.form)
            database.cursor.execute(f"SELECT * FROM Clubs WHERE name = '{search_add_field}'")
        elif update_button is not None:
            database.cursor.execute(f"UPDATE Clubs SET abbreviation = '{abbr}', badge = '{badge}', league = '{league_name}', season = '{league_season}' , W = {wins}, D = {draws}, L={loss} WHERE name = '{club}'")
            database.db.commit()
            database.cursor.execute("SELECT * FROM Clubs  ORDER BY points DESC ")
        elif add_button is not None:
            database.cursor.execute(f"INSERT INTO Clubs (name, league, season, abbreviation, badge, W, D, L) VALUES ('{club}','{league_name}', {league_season},'{abbr}','{badge}', {wins}, {draws}, {loss})")
            database.db.commit()
            database.cursor.execute("SELECT * FROM Clubs  ORDER BY points DESC ")
        elif remove_button is not None:
            team_to_delete = request.form.get('team_delete')
            database.cursor.execute(f"DELETE FROM Clubs WHERE name LIKE '{team_to_delete}'")
            database.db.commit()
            database.cursor.execute("SELECT * FROM Clubs  ORDER BY points DESC ")
        else:
            database.cursor.execute(("SELECT * FROM Clubs ORDER BY points DESC "))
    else:
        database.cursor.execute("SELECT * FROM Clubs  ORDER BY points DESC ")
    return render_template("csapatok.html", teams=database.cursor)


@app.route('/players', methods=['GET', 'POST'])
def players():
    if request.method == "POST":
        search_add_field = request.form.get('search_add_field')
        list_button = request.form.get('list')
        update_button = request.form.get('update')
        add_button = request.form.get('create')
        remove_button = request.form.get('remove_button')
        player_id = request.form.get('player_id')
        team = request.form.get('teams_name')
        name = request.form.get('player_name')
        position = request.form.get('pitch_position')
        shirt_number = request.form.get('shirt_number')
        if list_button is not None and search_add_field.strip() != "":
            database.cursor.execute(f"SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team  FROM Players INNER JOIN Clubs on Clubs.name = Players.team WHERE team = '{search_add_field}' OR Players.name = '{search_add_field}' OR position = '{search_add_field}'")
        elif update_button is not None:
            database.cursor.execute(f"UPDATE Players SET team = '{team}', position = '{position}', number = {shirt_number} WHERE id = {player_id}")
            database.db.commit()
            database.cursor.execute("SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team FROM Players INNER JOIN Clubs ON Clubs.name = Players.team")
        elif remove_button is not None:
            player_to_delete = request.form.get('player_delete')
            print(player_to_delete)
            database.cursor.execute(f"DELETE FROM Players WHERE id = '{player_to_delete}'")
            database.db.commit()
            database.cursor.execute("SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team FROM Players INNER JOIN Clubs ON Clubs.name = Players.team")
        elif add_button is not None:
            print(f"INSERT INTO Players(team, name, position, number) VALUES (team = '{team}', name = '{name}', position = '{position}', number = '{shirt_number}')")
            database.cursor.execute(f"INSERT INTO Players(team, name, position, number) VALUES ('{team}','{name}','{position}',{shirt_number})")
            database.db.commit()
            database.cursor.execute("SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team FROM Players INNER JOIN Clubs ON Clubs.name = Players.team")
        else:
            database.cursor.execute("SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team FROM Players INNER JOIN Clubs ON Clubs.name = Players.team")
    else:
        database.cursor.execute("SELECT badge, Players.name, Players.id AS id, Players.position, Players.number, team FROM Players INNER JOIN Clubs ON Clubs.name = Players.team")
    return render_template("jatekosok.html", players=database.cursor)


@app.route('/matches', methods=['GET', 'POST'])
def matches():
    if request.method == "POST":
        search_add_field = request.form.get('search_add_field')
        list_button = request.form.get('list')
        update_button = request.form.get('update')
        add_button = request.form.get('add')
        remove_button = request.form.get('remove_button')
        if request.form.get('search_options') == "Players":
            if list_button is not None and search_add_field.strip() != "":
                database.cursor.execute(f"SELECT badge, Players.name, Players.position, Players.number, team  FROM Players INNER JOIN Clubs on Clubs.name = Players.team WHERE team = '{search_add_field}'")
            elif update_button is not None:
                pass
            elif remove_button is not None:
                pass
            elif add_button is not None and search_add_field.strip() != "":
                pass
            else:
                database.cursor.execute("SELECT badge, Players.name, Players.position, Players.number, team FROM Players INNER JOIN Clubs ON Clubs.name = Players.team")
    else:
        database.cursor.execute("SELECT team, badge AS team_badge, enemy_team, (SELECT badge FROM Clubs WHERE Clubs.name = Matches.enemy_team) AS enemy_team_badge, takes_place FROM Matches INNER JOIN Clubs on Clubs.name = Matches.team")
    return render_template("meccsek.html", matches=database.cursor)


@app.route('/stadiums', methods=['GET', 'POST'])
def stadiums():
    if request.method == "POST":
        search_add_field = request.form.get('search_add_field')
        list = request.form.get('list')
        update_button = request.form.get('update')
        add_button = request.form.get('add')
        remove_button = request.form.get('remove_button')
        if request.form.get('search_options') == "Players":
            if list is not None and search_add_field.strip() != "":
                database.cursor.execute(f"SELECT badge, Players.name, Players.position, Players.number, club  FROM Players INNER JOIN Clubs on Clubs.name = Players.club WHERE club = '{search_add_field}'")
            elif update_button is not None:
                pass
            elif remove_button is not None:
                pass
            elif add_button is not None and search_add_field.strip() != "":
                pass
            else:
                database.cursor.execute("SELECT badge, Players.name, Players.position, Players.number, club FROM Players INNER JOIN Clubs ON Clubs.name = Players.club")
    else:
        database.cursor.execute("SELECT badge, Stadiums.team, Stadiums.name FROM Stadiums INNER JOIN Clubs ON Clubs.name = Stadiums.team")
    return render_template("stadionok.html", stadiums=database.cursor)


@app.route('/scorers', methods=['GET', 'POST'])
def scorers():
    if request.method == "POST":
        search_add_field = request.form.get('search_add_field')
        list_button = request.form.get('list')
        update_button = request.form.get('update')
        add_button = request.form.get('add')
        remove_button = request.form.get('remove_button')
        if list_button is not None and search_add_field.strip() != "":
            database.cursor.execute(f"SELECT badge, league, name, Players.position, Players.number, Scorers.team, goals  FROM Scorers INNER JOIN Players on Players.team = Scorers.team WHERE Scorers.team = '{search_add_field}'")
        elif update_button is not None:
            pass
        elif remove_button is not None:
            pass
        elif add_button is not None and search_add_field.strip() != "":
            pass
        else:
            database.cursor.execute("SELECT badge, Players.name, Players.position, Players.number, Scorers.team, goals, (SELECT badge FROM Clubs WHERE Clubs.name = Players.team) AS badge FROM Scorers INNER JOIN Players ON Players.team = Scorers.team WHERE Players.name = Scorers.name")
    return render_template("scorers.html", scorers=database.cursor)

@app.route('/managers', methods=['GET', 'POST'])
def manager():
    if request.method == "POST":
        print(request.form)
        search_add_field = request.form.get('search_add_field')
        list_button = request.form.get('list')
        update_button = request.form.get('update')
        add_button = request.form.get('add')
        remove_button = request.form.get('remove_button')
        if request.form.get('search_options') == "Managers":
            if list_button is not None and search_add_field.strip() != "":
                database.cursor.execute(
                    f"SELECT (SELECT (badge FROM Clubs WHERE Clubs.name = Owners.team) AS badge, name, nationality, team FROM Managers WHERE team = '{search_add_field}'")
            elif update_button is not None:
                pass
            elif remove_button is not None:
                pass
            elif add_button is not None and search_add_field.strip() != "":
                pass
            else:
                database.cursor.execute(
                    "SELECT name, nationality, team, (SELECT badge FROM Clubs INNER JOIN Clubs ON  ) AS badge FROM Managers")
    else:
        database.cursor.execute("SELECT name, nationality, team, (SELECT badge FROM Clubs WHERE Clubs.name = team) AS badge FROM Managers")
    return render_template("managers.html",  managers=database.cursor)

@app.route('/owners', methods=['GET', 'POST'])
def owners():
    if request.method == "POST":
        search_add_field = request.form.get('search_add_field')
        list_button = request.form.get('list')
        update_button = request.form.get('update')
        add_button = request.form.get('add')
        remove_button = request.form.get('remove_button')
        if list_button is not None and search_add_field.strip() != "":
            database.cursor.execute(
                f"SELECT company, boss, team, (SELECT badge FROM Clubs WHERE Clubs.name = Owners.team) AS badge FROM Owners WHERE Owners.team = '{search_add_field}' OR Owners.name = '{search_add_field}'")
        elif update_button is not None :
            pass
        elif remove_button is not None:
            pass
        elif add_button is not None and search_add_field.strip() != "":
            database.cursor.execute(f"INSERT INTO Owners (company) VALUES ('{search_add_field}')")
        else:
            database.cursor.execute(
                f"SELECT company, boss, team, (SELECT badge FROM Clubs WHERE Clubs.name = Owners.team) AS badge FROM Owners")
    else:
        database.cursor.execute(f"SELECT company, boss, team, (SELECT badge FROM Clubs WHERE Clubs.name = Owners.team) AS badge FROM Owners")
    return render_template("owners.html",  owners=database.cursor)

@app.route('/stat')
def statistics():
    database.cursor.execute("SELECT * FROM Players")
    database.cursor.execute("SELECT * FROM Clubs")
    print(database.cursor)
    return render_template("statistics.html", players=database.cursor)

if __name__ == '__main__':
    database.create_database()
    database.drop_tables()
    database.create_tables()
    database.triggers()
    # scraper.scraper()
    database.fill_up_tables("insert_bajnoksag.sql")
    database.fill_up_tables("insert_teams.sql")
    database.fill_up_tables("insert_player.sql")
    database.fill_up_tables("insert_match.sql")
    database.fill_up_tables("insert_stadiums.sql")
    database.fill_up_tables("insert_scorers.sql")
    database.fill_up_tables("insert_manager.sql")
    database.fill_up_tables("insert_owners.sql")
    app.run()

