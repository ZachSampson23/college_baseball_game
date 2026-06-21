"""Zach Sampson"""
import random
from models import*
from simulation import*
from leaderboard import*
from generation import*

team1 = team_generator("North Carolina Tar Heels")
team2 = team_generator("Duke Blue Devils")
team3 = team_generator("Virginia Cavaliers")
team4 = team_generator("NC State Wolfpack")
team5 = team_generator("Georgia Tech Yellow Jackets")
team6 = team_generator("Wake Forest Demon Deacons")
team7 = team_generator("Louisville Cardinals")
team8 = team_generator("Miami Hurricanes")
teams = [team1, team2, team3, team4, team5, team6, team7, team8]

dynasty = Dynasty(teams)
for x in range(len(teams)):
    print(teams[x].name + " | " + str(teams[x].get_overall()))
simulate_dynasty_year(dynasty)
simulate_dynasty_year(dynasty)
simulate_dynasty_year(dynasty)
simulate_dynasty_year(dynasty)
for x in range(4):
    print(str(dynasty.champion_history[x][1]) + " " + dynasty.champion_history[x][0].name)
for x in range(len(teams)):
    print(teams[x].name + " | " + str(teams[x].get_overall()))