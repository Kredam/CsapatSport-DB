from flask import Flask, redirect, url_for, render_template, request
import os
from db import database
from other import scraper


app = Flask(__name__, template_folder=os.path.abspath('client/templates'))
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/teams', methods=['GET','POST'])
def teams():
    if request.method == 'POST':
        list_button = request.form.get('list')
        add_button = request.form.get('add')
        remove_button = request.form.get('remove')
        club = request.form.get('team')
        abbr = request.form.get('abbreviation')
        badge = request.form.get('badge')
        stadium = request.form.get('stadium')
        wins = request.form.get('wins')
        draws = request.form.get('draws')
        loss = request.form.get('loss')
        points = wins*3 + draws
        matches_played = wins+draws+loss
        if list_button:
            database.cursor.execute(f"SELECT * FROM csapatok WHERE name LIKE '{club}' OR "
                                    f"abbreviation LIKE '{abbr}' OR "
                                    f"stadium LIKE '{stadium}'")
        if add_button:
            if club.strip() != "":
                database.cursor.execute(f"INSERT INTO csapatok (name, abbreviation, stadium, badge, points, matches_played, W, D, L) VALUES"
                                        f"('{club}', '{abbr}', '{stadium}', '{badge}', {points}, {matches_played}, {wins}, {draws}, {loss})")
                database.db.commit()
        if remove_button:
            database.cursor.execute(f"DELETE * FROM csapatok WHERE name LIKE '{club}' OR abbreviation LIKE '{abbr}'")
    else:
        database.cursor.execute("SELECT * FROM csapatok  ORDER BY points DESC ")
        database.db.commit()
    return render_template("csapatok.html", teams=database.cursor)

@app.route('/players')
def players():
    database.cursor.execute("SELECT * FROM jatekosok INNER JOIN csapatok on csapatok.name = jatekosok.club")
    return render_template("jatekosok.html", players=database.cursor)

@app.route('/matches')
def matches():
    database.cursor.execute("SELECT * FROM meccsek")
    return render_template("meccsek.html", matches=database.cursor)

@app.route('/stadiums')
def stadiums():
    database.cursor.execute("SELECT * FROM stadion")
    return render_template("stadionok.html", stadiums=database.cursor)



if __name__ == '__main__':
    database.create_database()
    database.drop_tables()
    database.create_tables()
    scraper.scraper()
    database.fill_up_tables("insert_teams.sql")
    database.fill_up_tables("insert_player.sql")
    database.fill_up_tables("insert_match.sql")
    database.fill_up_tables("insert_stadiums.sql")
    app.run()

