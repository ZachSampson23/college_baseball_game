"""Zach Sampson"""
import random
from models import*
from simulation import*
from leaderboard import*
from generation import*

team = team_generator("North Carolina Tar Heels")
team2 = team_generator("Duke Blue Devils")
team3 = team_generator("Virginia Cavaliers")
team4 = team_generator("NC State Wolfpack")
team5 = team_generator("Georgia Tech Yellow Jackets")
team6 = team_generator("Wake Forest Demon Deacons")
team7 = team_generator("Louisville Cardinals")
team8 = team_generator("Miami Hurricanes")
teams = [team, team2, team3, team4, team5, team6, team7, team8]

for x in range(5):
    print("BEFORE OFFSEASON")
    print("Lineup size:", len(team.lineup))
    print("Bench size:", len(team.bench))

    # Force a few players to graduate so we know the test is meaningful
    team.lineup[0].year = "Senior"
    team.lineup[1].year = "Senior"
    team.bench[0].year = "Senior"

    advance_team_offseason(team)

    print("\nAFTER OFFSEASON")
    print("Lineup size:", len(team.lineup))
    print("Bench size:", len(team.bench))

    print("\nLINEUP")
    for player in team.lineup:
        print(player.name, player.position, player.second_pos, player.year, player.get_overall())

    print("\nBENCH")
    for player in team.bench:
        print(player.name, player.position, player.second_pos, player.year, player.get_overall())

    # Basic checks
    if len(team.lineup) != 9:
        print("FAILED: lineup does not have 9 players")
    elif any(player.year == "Graduated" for player in team.lineup):
        print("FAILED: graduated player still in lineup")
    elif any(player.year == "Graduated" for player in team.bench):
        print("FAILED: graduated player still on bench")
    else:
        print("PASSED: offseason function works")