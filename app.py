import mysql.connector.errors
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
app.secret_key = "abc"
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
    error = None
    championships = clubsDAO.getAllLeagues()
    if request.method == 'POST':
        clubsDAO.listClubs()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            clubsDAO.searchClub(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            try:
                clubsDAO.updateClub(request.form.get('teams_name'), request.form.get('abbreviation'),
                                    request.form.get('badge'), request.form.get('league_name'),
                                    request.form.get('league_season'), request.form.get('wins'),
                                    request.form.get('draws'), request.form.get('loss'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('create') is not None:
            try:
                clubsDAO.addClub(request.form.get('teams_name'), request.form.get('abbreviation'),
                                 request.form.get('badge'), request.form.get('league_name'),
                                 request.form.get('league_season'), request.form.get('wins'),
                                 request.form.get('draws'), request.form.get('loss'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('remove_record') is not None:
            clubsDAO.removeClub(request.form.get('record_key'))
    else:
        clubsDAO.listClubs()
    return render_template("csapatok.html", teams=database.cursor, championships=championships, error=error)


@app.route('/players', methods=['GET', 'POST'])
def players():
    error = None
    if request.method == "POST":
        playersDAO.listPlayers()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            playersDAO.searchPlayer(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            try:
                playersDAO.updatePlayer(id=request.form.get('player_id'),
                                        team=request.form.get('teams_name'),
                                        position=request.form.get('pitch_position'),
                                        shirt_number=request.form.get('shirt_number'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('remove_record') is not None:
            playersDAO.removePlayer(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            try:
                playersDAO.createPlayer(team=request.form.get('teams_name'),
                                        name=request.form.get('player_name'),
                                        position=request.form.get('pitch_position'),
                                        shirt_number=request.form.get('shirt_number'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
    else:
        playersDAO.listPlayers()
    return render_template("jatekosok.html", players=database.cursor, error=error)


@app.route('/matches', methods=['GET', 'POST'])
def matches():
    error=None
    if request.method == "POST":
        matchesDAO.listMatches()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            matchesDAO.searchMatch(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            try:
                matchesDAO.updateMatch(request.form.get('match_id'), request.form.get('teams_name'),
                                       request.form.get('enemy_team'), request.form.get('takes_place'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('remove_record') is not None:
            matchesDAO.removeMatch(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            try:
                matchesDAO.createMatch(request.form.get('teams_name'),
                                       request.form.get('enemy_team'),
                                       request.form.get('takes_place'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
    else:
        matchesDAO.listMatches()
    return render_template("meccsek.html", matches=database.cursor, error=error)


@app.route('/stadiums', methods=['GET', 'POST'])
def stadiums():
    error = None
    if request.method == "POST":
        stadiumDAO.listStadium()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            stadiumDAO.searchStadium(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            try:
                stadiumDAO.updateStadium(request.form.get('teams'),
                                         request.form.get('stadium'),
                                         request.form.get('city'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('remove_record') is not None:
            stadiumDAO.removeStadium(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            try:
                stadiumDAO.createStadium(request.form.get('teams'),
                                         request.form.get('stadium'),
                                         request.form.get('city'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
    else:
        stadiumDAO.listStadium()
    return render_template("stadionok.html", stadiums=database.cursor, error=error)


@app.route('/training_grounds', methods=['GET', 'POST'])
def training_grounds():
    error = None
    if request.method == "POST":
        trainingGroundsDAO.listTrainingGrounds()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            trainingGroundsDAO.searchTrainingGround(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            try:
                trainingGroundsDAO.updateTrainingGround(name=request.form.get('training_ground'),
                                                        team=request.form.get('teams'),
                                                        city=request.form.get('city'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('remove_record') is not None:
            trainingGroundsDAO.removeTrainingGround(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            try:
                trainingGroundsDAO.createTrainingGround(name=request.form.get('training_ground'),
                                                        team=request.form.get('teams'),
                                                        city=request.form.get('city'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
    else:
        trainingGroundsDAO.listTrainingGrounds()
    return render_template("training_grounds.html", grounds=database.cursor, error=error)


@app.route('/managers', methods=['GET', 'POST'])
def manager():
    error = None
    if request.method == "POST":
        managersDAO.listManagers()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            managersDAO.searchManager(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            try:
                managersDAO.updateManager(manager_id=request.form.get('managers_id'),
                                          team=request.form.get('teams_name'),
                                          nationality=request.form.get('nationality'),
                                          name=request.form.get('name'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('remove_record') is not None:
            managersDAO.removeManager(request.form.get('record_key'))
        elif request.form.get('create') is not None:
            try:
                managersDAO.createManager(team=request.form.get('teams_name'),
                                          nationality=request.form.get('nationality'),
                                          name=request.form.get('name'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
    else:
        managersDAO.listManagers()
    return render_template("managers.html", managers=database.cursor, error=error)


@app.route('/owners', methods=['GET', 'POST'])
def owners():
    error = None
    if request.method == "POST":
        ownersDAO.listOwners()
        if request.form.get('list') is not None and request.form.get('search_word').strip() != "":
            ownersDAO.searchOwner(request.form.get('search_word'))
        elif request.form.get('update') is not None:
            try:
                ownersDAO.updateOwner(owner_id=request.form.get('owner_id'),
                                      company=request.form.get('company'),
                                      team=request.form.get('teams_name'),
                                      name=request.form.get('owner_name'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
        elif request.form.get('remove_record') is not None:
            ownersDAO.removeOwner(request.form.get('record_key'))
        elif request.form.get('add') is not None:
            try:
                ownersDAO.createOwner(company=request.form.get('company'),
                                      team=request.form.get('teams_name'),
                                      name=request.form.get('owner_name'))
            except mysql.connector.errors.IntegrityError:
                error = "Integrity Error occured(duplicate primary key or not existing foreign key"
    else:
        ownersDAO.listOwners()
    return render_template("owners.html", owners=database.cursor, error=error)


@app.route('/stat')
def statistics():
    return render_template("statistics.html", scorers=playersDAO.topScorers(),
                           sumPlayersTeam=playersDAO.sumPlayersByTeam(),
                           teams=playersDAO.groupScorersByTeam())


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
