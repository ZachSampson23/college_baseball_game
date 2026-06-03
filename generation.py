import random
from models import Batter, Pitcher, Team
from faker import Faker

fake = Faker()
def batter_generator():
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    name = first_name + " " + last_name
    random_contact = random.randint(50, 99)
    random_power = random.randint(50, 99)
    random_speed = random.randint(50, 99)
    random_fielding = random.randint(50, 99)
    new_batter = Batter(name, random_contact, random_power, random_speed, random_fielding)
    return new_batter

def pitcher_generator():
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    name = first_name + " " + last_name
    random_velocity = random.randint(50, 99)
    random_control = random.randint(50, 99)
    random_stuff = random.randint(50, 99)
    new_pitcher = Pitcher(name, random_velocity, random_control, random_stuff)
    return new_pitcher

def team_generator(team_name):
    lineup = []
    for x in range(9):
        lineup.append(batter_generator())
    pitcher = pitcher_generator()
    new_team = Team(team_name, lineup, pitcher)
    return new_team
