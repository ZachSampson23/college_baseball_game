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

test_season = simulate_season(teams)
print_standings(test_season)
batter_leaderboard_derived_stats(test_season, "avg", "Top 10 Avg")
