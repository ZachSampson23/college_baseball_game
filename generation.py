import random
from models import Batter, Pitcher, Team
from faker import Faker

fake = Faker()
def batter_generator():
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    name = first_name + " " + last_name
    
    
    five_star_prop = 0.03
    four_star_prop = five_star_prop + 0.12
    three_star_prop = four_star_prop + 0.4
    two_star_prop = three_star_prop + 0.3 
    star_prop = random.random()
    if star_prop <= five_star_prop:
        stars = 5
        contact = random.randint(75, 95)
        power = random.randint(75, 95)
        speed = random.randint(75, 95)
        fielding = random.randint(75, 95)
        five_star_gem_prop = 0.2
        five_star_bust_prop = five_star_gem_prop + 0.1
        gem_prop = random.random()
        if gem_prop <= five_star_gem_prop:
            potential = random.randint(95, 99)
            development = "gem"
        elif gem_prop <= five_star_bust_prop:
            potential = random.randint(72, 84)
            development = "bust"
        else:
            potential = random.randint(90, 99)
            development = "normal"
    elif star_prop <= four_star_prop:
        stars = 4
        contact = random.randint(70, 83)
        power = random.randint(70, 83)
        speed = random.randint(70, 83)
        fielding = random.randint(70, 83)
        four_star_gem_prop = 0.1
        four_star_bust_prop = four_star_gem_prop + 0.08
        gem_prop = random.random()
        if gem_prop <= four_star_gem_prop:
            potential = random.randint(92, 99)
            development = "gem"
        elif gem_prop <= four_star_bust_prop:
            potential = random.randint(68, 78)
            development = "bust"
        else:
            potential = random.randint(80, 92)
            development = "normal"
    elif star_prop <= three_star_prop:
        stars = 3
        contact = random.randint(60, 73)
        power = random.randint(60, 73)
        speed = random.randint(60, 73)
        fielding = random.randint(60, 73)
        three_star_gem_prop = 0.05
        three_star_bust_prop = three_star_gem_prop + 0.05
        gem_prop = random.random()
        if gem_prop <= three_star_gem_prop:
            potential = random.randint(90, 99)
            development = "gem"
        elif gem_prop <= three_star_bust_prop:
            potential = random.randint(62, 72)
            development = "bust"
        else:
            potential = random.randint(70, 84)
            development = "normal"
    elif star_prop <= two_star_prop:
        stars = 2
        contact = random.randint(50, 63)
        power = random.randint(50, 63)
        speed = random.randint(50, 63)
        fielding = random.randint(50, 63)
        two_star_gem_prop = 0.02
        two_star_bust_prop = two_star_gem_prop + 0.03
        gem_prop = random.random()
        if gem_prop <= two_star_gem_prop:
            potential = random.randint(85, 95)
            development = "gem"
        elif gem_prop <= two_star_bust_prop:
            potential = random.randint(55, 65)
            development = "bust"
        else:
            potential = random.randint(60, 76)
            development = "normal"
    else:
        stars = 1
        contact = random.randint(40, 53)
        power = random.randint(40, 53)
        speed = random.randint(40, 53)
        fielding = random.randint(40, 53)
        one_star_gem_prop = 0.01
        one_star_bust_prop = one_star_gem_prop + 0.01
        gem_prop = random.random()
        if gem_prop <= one_star_gem_prop:
            potential = random.randint(80, 90)
            development = "gem"
        elif gem_prop <= one_star_bust_prop:
            potential = random.randint(45, 65)
            development = "bust"
        else:
            potential = random.randint(50, 68)
            development = "normal"
    
    
    new_batter = Batter(name, contact, power, speed, fielding, stars, potential, development, "Freshman")
    return new_batter

def pitcher_generator():
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    name = first_name + " " + last_name


    five_star_prop = 0.03
    four_star_prop = five_star_prop + 0.12
    three_star_prop = four_star_prop + 0.4
    two_star_prop = three_star_prop + 0.3 
    star_prop = random.random()
    if star_prop <= five_star_prop:
        stars = 5
        velocity = random.randint(75, 95)
        control = random.randint(75, 95)
        stuff = random.randint(75, 95)
        five_star_gem_prop = 0.2
        five_star_bust_prop = five_star_gem_prop + 0.1
        gem_prop = random.random()
        if gem_prop <= five_star_gem_prop:
            potential = random.randint(95, 99)
            development = "gem"
        elif gem_prop <= five_star_bust_prop:
            potential = random.randint(72, 84)
            development = "bust"
        else:
            potential = random.randint(90, 99)
            development = "normal"
    elif star_prop <= four_star_prop:
        stars = 4
        velocity = random.randint(70, 83)
        control = random.randint(70, 83)
        stuff = random.randint(70, 83)
        four_star_gem_prop = 0.1
        four_star_bust_prop = four_star_gem_prop + 0.08
        gem_prop = random.random()
        if gem_prop <= four_star_gem_prop:
            potential = random.randint(92, 99)
            development = "gem"
        elif gem_prop <= four_star_bust_prop:
            potential = random.randint(68, 78)
            development = "bust"
        else:
            potential = random.randint(80, 92)
            development = "normal"
    elif star_prop <= three_star_prop:
        stars = 3
        velocity = random.randint(60, 73)
        control = random.randint(60, 73)
        stuff = random.randint(60, 73)
        three_star_gem_prop = 0.05
        three_star_bust_prop = three_star_gem_prop + 0.05
        gem_prop = random.random()
        if gem_prop <= three_star_gem_prop:
            potential = random.randint(90, 99)
            development = "gem"
        elif gem_prop <= three_star_bust_prop:
            potential = random.randint(62, 72)
            development = "bust"
        else:
            potential = random.randint(70, 84)
            development = "normal"
    elif star_prop <= two_star_prop:
        stars = 2
        velocity = random.randint(50, 63)
        control = random.randint(50, 63)
        stuff = random.randint(50, 63)
        two_star_gem_prop = 0.02
        two_star_bust_prop = two_star_gem_prop + 0.03
        gem_prop = random.random()
        if gem_prop <= two_star_gem_prop:
            potential = random.randint(85, 95)
            development = "gem"
        elif gem_prop <= two_star_bust_prop:
            potential = random.randint(55, 65)
            development = "bust"
        else:
            potential = random.randint(60, 76)
            development = "normal"
    else:
        stars = 1
        velocity = random.randint(40, 53)
        control = random.randint(40, 53)
        stuff = random.randint(40, 53)
        one_star_gem_prop = 0.01
        one_star_bust_prop = one_star_gem_prop + 0.01
        gem_prop = random.random()
        if gem_prop <= one_star_gem_prop:
            potential = random.randint(80, 90)
            development = "gem"
        elif gem_prop <= one_star_bust_prop:
            potential = random.randint(45, 65)
            development = "bust"
        else:
            potential = random.randint(50, 68)
            development = "normal"


    new_pitcher = Pitcher(name, velocity, control, stuff, stars, potential, development, "Freshman")
    return new_pitcher

def team_generator(team_name):
    lineup = []
    for x in range(9):
        lineup.append(batter_generator())
    pitcher = pitcher_generator()
    new_team = Team(team_name, lineup, pitcher)
    return new_team
