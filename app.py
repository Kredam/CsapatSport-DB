from flask import Flask, redirect, url_for, render_template, request
import os
from db import database
from other import scraper
from db.DAO import ClubsDAO
from db.DAO import PlayersDAO
from db.DAO import MatchesDAO
from db.DAO import StadiumsDAO
from db.DAO import OwnersDAO
from db.DAO import ManagersDAO
from db.DAO import TrainingGroudnsDAO

app = Flask(__name__, template_folder=os.path.abspath('client/templates'))
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./images/upload"
clubsDAO = ClubsDAO.ClubsDAO(database)
playersDAO = PlayersDAO.PlayerDAO(database)
matchesDAO = MatchesDAO.MatchesDAO(database)
stadiumDAO = StadiumsDAO.StadiumsDAO(database)
ownersDAO = OwnersDAO.OwnersDAO(database)
managersDAO = ManagersDAO.ManagersDAO(database)
trainingGroundsDAO = TrainingGroudnsDAO.TrainingGroundsDAO(database)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/teams', methods=['GET', 'POST'])
def teams():
    if request.method == 'POST':
        clubsDAO.listClubs()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            clubsDAO.searchClub(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            clubsDAO.updateClub(request.form.get('teams_name'), request.form.get('abbreviation'),
                                request.form.get('badge'), request.form.get('league_name'),
                                request.form.get('league_season'), request.form.get('wins'),
                                request.form.get('draws'), request.form.get('loss'))
        elif request.form.get('create') is not None:
            clubsDAO.addClub(request.form.get('teams_name'), request.form.get('abbreviation'),
                             request.form.get('badge'), request.form.get('league_name'),
                             request.form.get('league_season'), request.form.get('wins'),
                             request.form.get('draws'), request.form.get('loss'))
        elif request.form.get('remove_record') is not None:
            clubsDAO.removeClub(request.form.get('record_key'))
    else:
        clubsDAO.listClubs()
    return render_template("csapatok.html", teams=database.cursor)


@app.route('/players', methods=['GET', 'POST'])
def players():
    if request.method == "POST":
        playersDAO.listPlayers()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            playersDAO.searchPlayer(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            playersDAO.updatePlayer(id=request.form.get('player_id'),
                                    team=request.form.get('teams_name'),
                                    position=request.form.get('pitch_position'),
                                    shirt_number=request.form.get('shirt_number'))
        elif request.form.get('remove_record') is not None:
            playersDAO.removePlayer(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            playersDAO.createPlayer(team=request.form.get('teams_name'),
                                    name=request.form.get('player_name'),
                                    position=request.form.get('pitch_position'),
                                    shirt_number=request.form.get('shirt_number'))
    else:
        playersDAO.listPlayers()
    return render_template("jatekosok.html", players=database.cursor)


@app.route('/matches', methods=['GET', 'POST'])
def matches():
    if request.method == "POST":
        matchesDAO.listMatches()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            matchesDAO.searchMatch(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            matchesDAO.updateMatch(request.form.get('match_id'), request.form.get('teams_name'),
                                   request.form.get('enemy_team'), request.form.get('takes_place'))
        elif request.form.get('remove_record') is not None:
            matchesDAO.removeMatch(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            print(request.form)
            matchesDAO.createMatch(request.form.get('teams_name'),
                                   request.form.get('enemy_team'),
                                   request.form.get('takes_place'))
    else:
        matchesDAO.listMatches()
    return render_template("meccsek.html", matches=database.cursor)


@app.route('/stadiums', methods=['GET', 'POST'])
def stadiums():
    if request.method == "POST":
        stadiumDAO.listStadium()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            stadiumDAO.searchStadium(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            stadiumDAO.updateStadium(request.form.get('teams'),
                                     request.form.get('stadium'),
                                     request.form.get('city'))
        elif request.form.get('remove_record') is not None:
            stadiumDAO.removeStadium(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            stadiumDAO.createStadium(request.form.get('teams'),
                                     request.form.get('stadium'),
                                     request.form.get('city'))
    else:
        stadiumDAO.listStadium()
    return render_template("stadionok.html", stadiums=database.cursor)


@app.route('/training_grounds', methods=['GET', 'POST'])
def scorers():
    if request.method == "POST":
        trainingGroundsDAO.listTrainingGrounds()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            trainingGroundsDAO.searchTrainingGround(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            trainingGroundsDAO.updateTrainingGround(name=request.form.get('training_ground'),
                                                    team=request.form.get('teams'),
                                                    city=request.form.get('city'))
        elif request.form.get('remove_record') is not None:
            trainingGroundsDAO.removeTrainingGround(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            trainingGroundsDAO.createTrainingGround(name=request.form.get('training_ground'),
                                                    team=request.form.get('teams'),
                                                    city=request.form.get('city'))
    else:
        trainingGroundsDAO.listTrainingGrounds()
    return render_template("training_grounds.html", grounds=database.cursor)


@app.route('/managers', methods=['GET', 'POST'])
def manager():
    if request.method == "POST":
        managersDAO.listManagers()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            managersDAO.searchManager(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            managersDAO.updateManager(  manager_id=request.form.get('managers_id'),
                                        team=request.form.get('teams_name'),
                                        nationality=request.form.get('nationality'),
                                        name=request.form.get('name'))
        elif request.form.get('remove_record') is not None:
            managersDAO.removeManager(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            managersDAO.createManager(team=request.form.get('teams_name'),
                                      nationality=request.form.get('nationality'),
                                      name=request.form.get('name'))
    else:
        managersDAO.listManagers()
    return render_template("managers.html", managers=database.cursor)


@app.route('/owners', methods=['GET', 'POST'])
def owners():
    if request.method == "POST":
        ownersDAO.listOwners()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            ownersDAO.searchOwner(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            ownersDAO.updateOwner(request.form.get('owner_id'),
                                  request.form.get('company'),
                                  request.form.get('teams_name'),
                                  request.form.get('owner_name'))
        elif request.form.get('remove_record') is not None:
            ownersDAO.removeOwner(request.form.get('record_key'))
        elif request.form.get('add') is not None:
            ownersDAO.createOwner(request.form.get('company'),
                                  request.form.get('teams_name'),
                                  request.form.get('owner_name'))
    else:
        ownersDAO.listOwners()
    return render_template("owners.html", owners=database.cursor)


@app.route('/stat')
def statistics():
    return render_template("statistics.html", teams=clubsDAO.scorersByTeam(),
                           sumPlayersTeam=playersDAO.sumPlayersByTeam())


if __name__ == '__main__':
    print(os.getcwd())
    database.create_database()
    database.drop_tables()
    database.create_tables()
    database.triggers()
    # scraper.scraper()
    database.fill_up_tables("insert_championships.sql")
    database.fill_up_tables("insert_teams.sql")
    database.fill_up_tables("insert_player.sql")
    database.fill_up_tables("insert_match.sql")
    database.fill_up_tables("insert_stadiums.sql")
    database.fill_up_tables("insert_manager.sql")
    database.fill_up_tables("insert_owners.sql")
    database.fill_up_tables("insert_training_grounds.sql")
    app.run()
