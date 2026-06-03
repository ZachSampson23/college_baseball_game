from models import Season

def stat_line(batter):
    derived_stats = batter.stats.get_stats()
    obp = derived_stats["obp"]
    avg = derived_stats["avg"]
    slg = derived_stats["slg"]
    ops = derived_stats["ops"]
    blockA = batter.name + " | " + str(batter.stats.games) + " G | " + str(batter.stats.at_bats) + " AB | " + str(batter.stats.hits) + " H | " + \
          str(batter.stats.home_runs) + " HR | " + str(batter.stats.rbi) + " RBI | "
    blockB = f"{avg:.3f}".lstrip("0") + "/" + f"{obp:.3f}".lstrip("0") + "/" + f"{slg:.3f}".lstrip("0") + " | " + \
          f"{ops:.3f}".lstrip("0") + " OPS"
    print(blockA + blockB)

def print_standings(season):
    sorted_teams = sorted(season.teams, key=lambda team: team.wins, reverse=True)
    #takes the teams and sorts the objects by their wins in descending order
    print("Standings")
    for x in range(len(sorted_teams)):
        win_percentage = f"{sorted_teams[x].wins / (sorted_teams[x].wins + sorted_teams[x].losses):.3f}".lstrip("0")
        run_differential = sorted_teams[x].stats.get_stats()["run_diff"]
        if run_differential > 0:
            run_differential = "+" + str(run_differential)
        print(str(x + 1) + ". " + sorted_teams[x].name + " | " + str(sorted_teams[x].wins) + "-" + 
              str(sorted_teams[x].losses) + " | " + str(win_percentage) + " | " + str(run_differential))

def batter_leaderboard_derived_stats(season, stat, title):
    """Takes the season, what stat to sort by and the title of the leaderboard. This will print the top 10 in the stat that is chosen"""
    every_player_list = []
    for x in season.teams:
        for y in range(len(x.lineup)):
            every_player_list.append(x.lineup[y])
    sorted_players = sorted(every_player_list, key=lambda batter: batter.stats.get_stats()[stat], reverse=True)
    print(title)
    for i in range(10):
        print(str(i + 1) + ". " + sorted_players[i].name + "   " + f"{sorted_players[i].stats.get_stats()[stat]:.3f}".lstrip("0"))

def batter_leaderboard_non_derived_stats(season, stat, title):
    """Takes the season, what stat to sort by and the title of the leaderboard. Creates a learderboard for the chosen stat"""
    every_player_list = []
    for x in season.teams:
        for y in range(len(x.lineup)):
            every_player_list.append(x.lineup[y])
    sorted_players = sorted(every_player_list, key=lambda batter: getattr(batter.stats, stat), reverse=True)
    print(title)
    for i in range(10):
        print(str(i + 1) + ". " + sorted_players[i].name + "   " + str(getattr(sorted_players[i].stats, stat)))

def pitcher_leaderboard_non_derived_stats(season, stat, title):
    every_pitcher_list = []
    for x in season.teams:
        every_pitcher_list.append(x.pitcher)
    if stat in ["strikeouts", "outs_recorded"]:
        sorted_players = sorted(every_pitcher_list, key=lambda pitcher: getattr(pitcher.stats, stat), reverse=True)
    else:
        sorted_players = sorted(every_pitcher_list, key=lambda pitcher: getattr(pitcher.stats, stat), reverse=False)
    print(title)
    for i in range(3):
        print(str(i + 1) + ". " + sorted_players[i].name + "   " + str(getattr(sorted_players[i].stats, stat)))

def pitcher_leaderboard_derived_stats(season, stat, title):
    every_pitcher_list = []
    for x in season.teams:
        every_pitcher_list.append(x.pitcher)
    if stat == "K/9":
        sorted_players = sorted(every_pitcher_list, key=lambda pitcher: pitcher.stats.get_stats()[stat], reverse=True)
    else:
        sorted_players = sorted(every_pitcher_list, key=lambda pitcher: pitcher.stats.get_stats()[stat], reverse=False)
    print(title)
    for i in range(3):
        print(str(i + 1) + ". " + sorted_players[i].name + "   " + f"{sorted_players[i].stats.get_stats()[stat]:.2f}")

def team_leaderboards(derived_stat, stat, title, season):
    if derived_stat:
        sorted_teams = sorted(season.teams, key=lambda team: team.stats.get_stats()[stat], reverse=True)
    else:
        if stat in ["runs_allowed", "errors"]:
            sorted_teams = sorted(season.teams, key=lambda team: getattr(team.stats, stat), reverse=False)
        else:
            sorted_teams = sorted(season.teams, key=lambda team: getattr(team.stats, stat), reverse=True)
    print(title)
    for i in range(len(season.teams)):
        if stat == "run_diff":
            if sorted_teams[i].stats.get_stats()[stat] > 0:
                run_diff = sorted_teams[i].stats.get_stats()[stat]
                print(str(i + 1) + ". " + sorted_teams[i].name + "   +" + str(run_diff))
            else:
                print(str(i + 1) + ". " + sorted_teams[i].name + "   " + str(sorted_teams[i].stats.get_stats()[stat]))
        elif derived_stat:
            print(str(i + 1) + ". " + sorted_teams[i].name + "   " + str(sorted_teams[i].stats.get_stats()[stat]))
        else:
            print(str(i + 1) + ". " + sorted_teams[i].name + "   " + str(getattr(sorted_teams[i].stats, stat)))