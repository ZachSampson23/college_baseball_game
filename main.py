"""Zach Sampson"""
import random
from models import*
from simulation import*
from leaderboard import*


unc_batter1 = Batter("")



teams = [team1, team2, team3]
test_season = simulate_season(teams)
print_standings(test_season)
batter_leaderboard_non_derived_stats(test_season, "home_runs", "Home Run Leaderboard")
batter_leaderboard_derived_stats(test_season, "ops", "OPS Leaderboard")
pitcher_leaderboard_non_derived_stats(test_season, "strikeouts", "Strikeout Leaderboard")
pitcher_leaderboard_derived_stats(test_season, "era", "ERA Leaders")