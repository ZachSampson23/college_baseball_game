"""Zach Sampson"""
import random
from models import*
from simulation import*
from leaderboard import*
from generation import*

team1 = team_generator("North Carolina Tar Heels")
team2 = team_generator("Duke Blue Devils")
team3 = team_generator("Wake Forest Demon Deacons")
team4 = team_generator("Clemson Tigers")
team5 = team_generator("Louisville Cardinals")
team6 = team_generator("Miami Hurricanes")
team7 = team_generator("Virginia Cavaliers")
team8 = team_generator("Virginia Tech Hokies")
teams = [team1, team2, team3, team4, team5, team6, team7, team8]

test_dynasty = Dynasty(teams)
simulate_dynasty_year(test_dynasty)
simulate_dynasty_year(test_dynasty)
simulate_dynasty_year(test_dynasty)
print(test_dynasty.current_year)
print(len(test_dynasty.season_history))
for i in range(len(test_dynasty.champion_history)):
    team = test_dynasty.champion_history[i][0]
    year = test_dynasty.champion_history[i][1]
    print(str(year) + " - " + team.name)