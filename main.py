"""Zach Sampson"""
import random
from models import*
from simulation import*
from leaderboard import*
from generation import*

batter = batter_generator()
print("Name: " + batter.name + " Potential: " + str(batter.potential) + " Development: " + batter.development_type)
print("Year 1: " + str(batter.get_overall()))
progress_batter(batter)
print("Year 2: " + str(batter.get_overall()))
progress_batter(batter)
print("Year 3: " + str(batter.get_overall()))
progress_batter(batter)
print("Year 4: " + str(batter.get_overall()))