from stats import BatterStat, PitcherStat, TeamStat

class Batter:
    def __init__(self, name, contact, power, speed, fielding):
        self.name = name
        self.contact = contact
        self.power = power
        self.speed = speed
        self.fielding = fielding
        self.stats = BatterStat()
    
class Pitcher:
    def __init__(self, name, velocity, control, stuff):
        self.name = name
        self.velocity = velocity
        self.control = control
        self.stuff = stuff
        self.stats = PitcherStat()

class Result:
    def __init__(self, result):
        self.result = result

class Team:
    def __init__(self, name, lineup, pitcher):
        self.name = name
        self.lineup = lineup
        self.pitcher = pitcher
        self.wins = 0
        self.losses = 0
        self.stats = TeamStat()

class Season:
    def __init__(self, teams):
        self.teams = teams
        self.schedule = self.schedule_creation()
        self.season_games_played = 0
    
    def schedule_creation(self):
        schedule = []
        num_teams = len(self.teams)
        for i in range(num_teams):
            for j in range(num_teams):
                if i <= j:
                    continue
                matchup = [self.teams[i], self.teams[j]]
                for k in range(3):
                    schedule.append(matchup)
        return schedule