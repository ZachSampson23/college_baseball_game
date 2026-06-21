"""Zach Sampson"""
import random
from models import*
from simulation import*
from leaderboard import*
from generation import*

pitcher = pitcher_generator()
print("Name: " + pitcher.name + " Potential: " + str(pitcher.potential) + " Development: " + pitcher.development_type)
print("Year 1: " + str(pitcher.get_overall()))
progress_pitcher(pitcher)
print("Year 2: " + str(pitcher.get_overall()))
progress_pitcher(pitcher)
print("Year 3: " + str(pitcher.get_overall()))
progress_pitcher(pitcher)
print("Year 4: " + str(pitcher.get_overall()))