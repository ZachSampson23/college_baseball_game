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

player1 = Batter(34, 44, 5, 24, 22, 4, 55, "normal", "Freshman")
player2 = Batter(34, 44, 5, 24, 22, 4, 55, "normal", "Sophomore")
player3 = Batter(34, 44, 5, 24, 22, 4, 55, "normal", "Junior")
player4 = Batter(34, 44, 5, 24, 22, 4, 55, "normal", "Senior")

print("Player1: " + player1.year)
print("Player2: " + player2.year)
print("Player3: " + player3.year)
print("Player4: " + player4.year)

advance_player_year(player1)
advance_player_year(player2)
advance_player_year(player3)
advance_player_year(player4)

print("Player1: " + player1.year)
print("Player2: " + player2.year)
print("Player3: " + player3.year)
print("Player4: " + player4.year)