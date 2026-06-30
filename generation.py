import random
from models import Batter, Pitcher, Team
from faker import Faker

fake = Faker()
def batter_generator(position, second_pos):
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
            development_type = "gem"
        elif gem_prop <= five_star_bust_prop:
            potential = random.randint(72, 84)
            development_type = "bust"
        else:
            potential = random.randint(90, 99)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= four_star_bust_prop:
            potential = random.randint(68, 78)
            development_type = "bust"
        else:
            potential = random.randint(80, 92)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= three_star_bust_prop:
            potential = random.randint(62, 72)
            development_type = "bust"
        else:
            potential = random.randint(70, 84)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= two_star_bust_prop:
            potential = random.randint(55, 65)
            development_type = "bust"
        else:
            potential = random.randint(60, 76)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= one_star_bust_prop:
            potential = random.randint(45, 65)
            development_type = "bust"
        else:
            potential = random.randint(50, 68)
            development_type = "normal"
    
    
    new_batter = Batter(name, contact, power, speed, fielding, stars, potential, development_type, "Freshman", position, second_pos)
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
            development_type = "gem"
        elif gem_prop <= five_star_bust_prop:
            potential = random.randint(72, 84)
            development_type = "bust"
        else:
            potential = random.randint(90, 99)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= four_star_bust_prop:
            potential = random.randint(68, 78)
            development_type = "bust"
        else:
            potential = random.randint(80, 92)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= three_star_bust_prop:
            potential = random.randint(62, 72)
            development_type = "bust"
        else:
            potential = random.randint(70, 84)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= two_star_bust_prop:
            potential = random.randint(55, 65)
            development_type = "bust"
        else:
            potential = random.randint(60, 76)
            development_type = "normal"
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
            development_type = "gem"
        elif gem_prop <= one_star_bust_prop:
            potential = random.randint(45, 65)
            development_type = "bust"
        else:
            potential = random.randint(50, 68)
            development_type = "normal"


    new_pitcher = Pitcher(name, velocity, control, stuff, stars, potential, development_type, "Freshman")
    return new_pitcher

def walk_on_generator(position):
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    name = first_name + " " + last_name
    if position == "Pitcher":
        velocity = random.randint(40, 53)
        control = random.randint(40, 53)
        stuff = random.randint(40, 53)
        one_star_gem_prop = 0.01
        one_star_bust_prop = one_star_gem_prop + 0.01
        gem_prop = random.random()
        if gem_prop <= one_star_gem_prop:
            potential = random.randint(80, 90)
            development_type = "gem"
        elif gem_prop <= one_star_bust_prop:
            potential = random.randint(45, 65)
            development_type = "bust"
        else:
            potential = random.randint(50, 68)
            development_type = "normal"
        return Pitcher(name, velocity, control, stuff, 1, potential, development_type, "Freshman")
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
            development_type = "gem"
        elif gem_prop <= one_star_bust_prop:
            potential = random.randint(45, 65)
            development_type = "bust"
        else:
            potential = random.randint(50, 68)
            development_type = "normal"
        second_pos = second_pos_gen(position)
        return Batter(name, contact, power, speed, fielding, stars, potential, development_type, "Freshman", position, second_pos)

def team_generator(team_name):
    lineup = []
    bench = []
    lineup.append(batter_generator("1B", second_pos_gen("1B")))
    lineup.append(batter_generator("2B", second_pos_gen("2B")))
    lineup.append(batter_generator("SS", second_pos_gen("SS")))
    lineup.append(batter_generator("3B", second_pos_gen("3B")))
    lineup.append(batter_generator("C", second_pos_gen("C")))
    lineup.append(batter_generator("RF", second_pos_gen("RF")))
    lineup.append(batter_generator("CF", second_pos_gen("CF")))
    lineup.append(batter_generator("LF", second_pos_gen("LF")))
    dh_pos = position_generator()
    lineup.append(batter_generator(dh_pos, second_pos_gen(dh_pos)))

    for x in range(5):
        first_position = position_generator()
        bench.append(batter_generator(first_position, second_pos_gen(first_position)))

    pitcher = pitcher_generator()
    new_team = Team(team_name, lineup, pitcher, bench)
    return new_team

def position_generator():
    positions = ["1B", "2B", "3B", "SS", "C", "LF", "CF", "RF"]
    return random.choice(positions)

def second_pos_gen(first_position):
    if first_position == "C":
        choices = [None, "1B"]
        return random.choice(choices)
    elif first_position == "1B":
        choices = ["3B", "LF"]
        return random.choice(choices)
    elif first_position == "2B":
        choices = ["SS", "3B", "CF"]
        return random.choice(choices)
    elif first_position == "SS":
        choices = ["2B", "3B"]
        return random.choice(choices)
    elif first_position == "3B":
        choices = ["1B", "SS"]
        return random.choice(choices)
    elif first_position == "LF":
        choices = ["RF", "CF", "1B"]
        return random.choice(choices)
    elif first_position == "CF":
        choices = ["RF", "LF"]
        return random.choice(choices)
    elif first_position == "RF":
        choices = ["CF", "LF", "1B"]
        return random.choice(choices)

def create_recruiting_class():
    recruiting_class = []
    for x in range(10):
        first_position = position_generator()
        batter = batter_generator(first_position, second_pos_gen(first_position))
        recruiting_class.append(batter)
    return recruiting_class
