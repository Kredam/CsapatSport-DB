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
        add_button = request.form.get('add')
        remove_button = request.form.get('remove_button')
        club = request.form.get('team')
        if list_button is not None and club.strip() != "":
            database.cursor.execute(f"SELECT * FROM csapatok WHERE name LIKE '{club}'")
        elif update_button is not None:
            print(request.form)
            update_club = request.form.get('teams_name')
            badge = request.form.get('badge')
            wins = request.form.get('wins')
            draws = request.form.get('draws')
            loss = request.form.get('loss')
            abbr = request.form.get('abbreviation')
            database.cursor.execute(f"UPDATE csapatok SET abbreviation = '{abbr}', badge = '{badge}', W = {wins}, D = {draws}, L={loss} WHERE name = '{update_club}'")
            database.db.commit()
            database.cursor.execute("SELECT * FROM csapatok  ORDER BY points DESC ")
        elif add_button is not None and club.strip() != "":
            database.cursor.execute(f"INSERT INTO csapatok (name) VALUES ('{club}')")
            database.db.commit()
            database.cursor.execute("SELECT * FROM csapatok  ORDER BY points DESC ")
        elif remove_button is not None:
            team_to_delete = request.form.get('team_delete')
            database.cursor.execute(f"DELETE FROM csapatok WHERE name LIKE '{team_to_delete}'")
            database.db.commit()
            database.cursor.execute("SELECT * FROM csapatok  ORDER BY points DESC ")
        else:
            database.cursor.execute(("SELECT * FROM csapatok ORDER BY points DESC "))
    else:
        database.cursor.execute("SELECT * FROM csapatok  ORDER BY points DESC ")
    return render_template("csapatok.html", teams=database.cursor)


@app.route('/players', methods=['GET', 'POST'])
def players():
    if request.method == "POST":
        team = request.form.get('team')
        list = request.form.get('list')
        if list is not None and team.strip() != "":
            database.cursor.execute(f"SELECT * FROM jatekosok INNER JOIN csapatok on csapatok.name = jatekosok.club WHERE club = '{team}'")
        elif list is not None and team.strip() == "":
            database.cursor.execute(f"SELECT * FROM jatekosok")
    else:
        database.cursor.execute("SELECT * FROM jatekosok INNER JOIN csapatok on csapatok.name = jatekosok.club")
    return render_template("jatekosok.html", players=database.cursor)


@app.route('/matches')
def matches():
    database.cursor.execute("SELECT * FROM meccsek INNER JOIN csapatok on csapatok.name = meccsek.team")
    return render_template("meccsek.html", matches=database.cursor)


@app.route('/stadiums')
def stadiums():
    database.cursor.execute("SELECT * FROM stadion INNER JOIN csapatok ON csapatok.name = stadion.team")
    return render_template("stadionok.html", stadiums=database.cursor)


if __name__ == '__main__':
    database.create_database()
    database.drop_tables()
    database.create_tables()
    database.triggers()
    # scraper.scraper()
    database.fill_up_tables("insert_teams.sql")
    database.fill_up_tables("insert_player.sql")
    database.fill_up_tables("insert_match.sql")
    database.fill_up_tables("insert_stadiums.sql")
    app.run()

