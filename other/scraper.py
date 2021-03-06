import cmd
import re
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
import os

import urllib.request

PATH = os.getcwd()+"\\other\\chromedriver.exe"

URL = "https://www.premierleague.com/tables"
premier_league = requests.get(URL)
soup = BeautifulSoup(premier_league.content, "html.parser")
container = soup.find("div", class_="table wrapper col-12")
Clubs = soup.find("nav", class_="clubNavigation").find_all("span", class_="name")
Clubs = [club.get_text().rstrip() for club in Clubs]
jatekos_id = 1


class scraper:
    def __init__(self):
        self.team_website = ""
        self.scrape_clubs_data()

    def scrape_stadium(self):
        wd = webdriver.Chrome(PATH)
        wd.implicitly_wait(20)
        wd.get(self.team_website[:-8] + "stadium")
        stadium_name = wd.find_element_by_css_selector('span.stadium').text.replace('\'', '\'\'')
        wd.quit()

    def scrape_player_goal(self, URL):
        soup = BeautifulSoup(requests.get("https://www.premierleague.com"+URL[:-8]+"stats").content, 'html.parser')
        print("https://www.premierleague.com"+URL[:-8]+"/stats")
        return int(soup.find('span', class_="allStatContainer statgoals").text)
        pass


    def scrape_players_data(self, club):
        player_list = list()
        soup = BeautifulSoup(requests.get(self.team_website).content, 'html.parser')
        club_overview = soup.find("nav", class_="heroPageLinks").find("a", attrs={"href": "squad"})["href"]
        soup = BeautifulSoup(requests.get(self.team_website[:-8] + club_overview).content, 'html.parser')
        player_card_list = soup.find("ul", class_="squadListContainer squadList block-list-4 block-list-3-m block-list-2-s block-list-padding").find_all('li')
        # print(player_card_list)
        players_info = soup.find_all("a", class_="playerOverviewCard active")
        for player_info in players_info:
            goals = 0
            player_name = player_info.find("h4", class_="name").text.replace('\'', '"')
            player_nr = player_info.find("span", class_="number").text
            player_pos = player_info.find("span", class_="position").text
            for labels in player_info.find_all('dl'):
                if labels.findChild('dt').text == "Goals":
                    print(labels)
                    goals = int(labels.findChild('dd').text)
            # print(f"INSERT INTO Players(team, name, position, number, goals) VALUES ({jatekos_id}, '{club}', '{player_name}', '{player_pos}', {int(player_nr)}, {int()});\n")
            if player_name not in player_list and player_nr.isdigit():
                statement = f"INSERT INTO Players(team, name, position, number, goals) VALUES ('{club}', '{player_name}', '{player_pos}', {int(player_nr)}, {int(goals)});\n"
                self.write_to_sql_file("db/sql/insert_player.sql", statement)

    def prev_match(self, match_data, abbr, name):
        for data in match_data:
            if data.find("strong").text == "Recent Result":
                time = data.find("div", class_="label").text
                opponents = data.find_all("span", class_="teamName")
                score = data.find("span", class_="score").text
                for element in opponents:
                    if element.text != abbr:
                        opponent = element.text
                        if opponents[0].text == opponent:
                            return f"{time} \n{opponent} - {name}\n  {score}"
                        else:
                            return f"{time} \n{name} - {opponent}\n  {score}"

    def next_match(self, match_data, abbr, name):
        months = {
            "November": 11,
            "December": 12
        }
        for data in match_data:
            if data.find("strong").text == "Next Fixture":
                time = data.find("time").text + ":00"
                date = data.find("div", class_="label").text
                first_nr = re.search(r'\d', date)
                date = date[first_nr.start():]
                for key, value in months.items():
                    if key in date:
                        date = date[len(date) - 4:] + "-" + str(value) + "-" + date[0]
                team_names = data.find_all("span", class_="teamName")
                datetime = date + " " + time
                for enemy in team_names:
                    if enemy.text != abbr:
                        enemy = enemy.findChild("abbr")
                        statement = f"INSERT INTO Matches(team, enemy_team, takes_place) VALUES ('{name}', '{enemy['title']}', '{datetime}');\n"
                        self.write_to_sql_file("db/sql/insert_match.sql", statement)

    def scrape_clubs_data(self):
        self.clear_file_content("db/sql/insert_match.sql")
        self.clear_file_content("db/sql/insert_player.sql")
        self.clear_file_content("db/sql/insert_teams.sql")
        for club in Clubs:
            if club == "Brighton & Hove Albion":
                club = "Brighton and Hove Albion"
            badge = soup.find("tr", attrs={"data-filtered-table-row-name": club}).find("span", attrs={
                "data-size": 25}).findChild("img")["src"]
            position = soup.find("tr", attrs={"data-filtered-table-row-name": club})['data-position']
            team_stat = soup.find("tr", attrs={"data-filtered-table-row-name": club}).findChildren("td", class_=False)
            abbreviation = soup.find("tr", attrs={"data-filtered-table-row-name": club}).find("span",
                                                                                              class_="short").text
            position = soup.find("tr", attrs={"data-filtered-table-row-name": club}).findChild("span").text
            matches_played = team_stat[0].text
            wins = team_stat[1].text
            draw = team_stat[2].text
            loss = team_stat[3].text
            self.team_website = "https://www.premierleague.com/" + \
                                soup.find("tr", attrs={"data-filtered-table-row-name": club}).find("td",
                                                                                                   class_="team").find(
                                    "a")["href"]
            match_data = soup.find("tr", attrs={
                "data-filtered-table-row-expander": soup.find("tr", attrs={"data-filtered-table-row-name": club})[
                    "data-filtered-table-row"]}).find_all("div", class_="resultWidget")
            points = int(wins)*3+int(draw)
            statement = f"INSERT INTO Clubs(name, league, season, abbreviation, badge, W, D, L) VALUES ('{club}', 'Premier League', 2021, '{abbreviation}', '{badge}', {wins}, {draw}, {loss});\n"
            self.write_to_sql_file("db/sql/insert_teams.sql", statement)
            self.next_match(match_data, abbreviation, club)
            self.scrape_players_data(club)

    def clear_file_content(self, file_name):
        with open(file_name, "r+", encoding='utf-8') as f:
            data = f.read()
            f.seek(0)
            f.truncate()

    def write_to_sql_file(self, file_name, insert_statement):
        # os.chmod(os.getcwd(), 755)
        try:
            file = open(file_name, "a", encoding="utf-8")
            file.write(insert_statement)
        except FileNotFoundError:
            file = open(file_name, "w", encoding="utf-8")
            file.write(insert_statement)
