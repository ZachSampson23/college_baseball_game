from models import Season, Result, Dynasty
from stats import TeamStat, BatterStat, PitcherStat
import random

def at_bat(pitcher, batter):
    """Simulates a single at-bat requiring one pitcher object and one batter object"""
    base_walk_proportion = 0.12
    walk_proportion = base_walk_proportion - pitcher.control * 0.00025
    random_walk_prop = random.random()
    if walk_proportion >= random_walk_prop:
        result = Result("Walk")
        return result
    else:
        base_stikeout_prop = 0.21
        strikout_prop = 0.0002 * (pitcher.stuff + pitcher.velocity - batter.contact) + base_stikeout_prop
        random_strikeout_prop = random.random()
        if strikout_prop >= random_strikeout_prop:
            result = Result("Strikeout")
            return result
        else:
            base_hit_prop = 0.315
            hit_prop = 0.001 * (batter.contact - pitcher.stuff) + base_hit_prop
            random_hit_prop = random.random()
            if hit_prop >= random_hit_prop:
                hit_random = random.random()
                hr_base_prop = 0.015
                hr_prop = batter.power * 0.001 + hr_base_prop
                double_base_prop = 0.155
                double_prop = batter.power * 0.0003 + double_base_prop
                double_threshold = double_prop + hr_prop
                triple_base_prop = 0.008
                triple_prop = batter.speed * 0.001 + triple_base_prop
                triple_threshold = double_threshold + triple_prop
                if hr_prop >= hit_random:
                    result = Result("Homerun")
                    return result
                elif double_threshold >= hit_random:
                    result = Result("Double")
                    return result
                elif triple_threshold >= hit_random:
                    result = Result("Triple")
                    return result
                else:
                    result = Result("Single")
                    return result
            else:
                error_base_prop = 0.035
                random_error_prop = random.random()
                if(error_base_prop >= random_error_prop):
                    result = Result("Error")
                    return result
                else:
                    result = Result("Out")
                    return result

def simulate_inning(pitcher, lineup, batter_index):
    outs = 0
    strikeouts = 0
    runs = 0
    hits = 0
    walks = 0
    singles = 0
    doubles = 0
    triples = 0
    home_runs = 0
    errors = 0
    bases = [None, None, None]
    i = batter_index

    while outs < 3:
        result = at_bat(pitcher, lineup[i])
        runs_in_one_play = 0
        if result.result == "Out" or result.result == "Strikeout" :
            if result.result == "Out":
                #print(lineup[i].name + " hits into an out")
                outs+=1
            else:
                strikeouts += 1
                outs+=1
                #print(pitcher.name + " strikes out " + lineup[i].name + "!")
        elif result.result == "Homerun" or result.result == "Triple" or result.result == "Double" or result.result == "Single":
            hits += 1
            if result.result == "Homerun":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                home_runs += 1
                #print(lineup[i].name + " hits it out of the park, HOMERUN!!")
            elif result.result == "Triple":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                triples += 1
                #print(lineup[i].name + " hits it for a triple.")
            elif result.result == "Double":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                doubles += 1
                #print(lineup[i].name + " hits it for a double.")
            elif result.result == "Single":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                singles += 1
                #print(lineup[i].name + " hits it for a single.")
        elif result.result == "Walk":
            bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
            walks += 1
            #print(lineup[i].name + " draws a walk.")
        elif result.result == "Error":
            bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
            errors += 1
            #print(lineup[i].name + " gets on base from an error.")
        lineup[i].stats.record_result(result.result, runs_in_one_play)
        pitcher.stats.record_result(result.result, runs_in_one_play)
        i += 1
        if i >= len(lineup):
            i = 0

    #print("Strikeouts: " + str(strikeouts), "Runs: " + str(runs), "Walks: " + str(walks), "Hits: " + str(hits),
        #"Singles: " + str(singles), "Doubles: " + str(doubles), "Triples: " + str(triples), "Home Runs: " + str(home_runs), "Errors: " + str(errors))
    return {"runs": runs, "strikeouts": strikeouts, "walks": walks, "hits": hits, "singles": singles, "doubles": doubles, 
            "triples": triples, "home_runs": home_runs, "errors": errors, "next_batter_index": i}

def advance_runners(result, bases, batter, runs):
    first_base = bases[0]
    second_base = bases[1]
    third_base = bases[2]
    additional_runs = 0
    if result == "Error":
        base_error_speed_prop = 0.4
        error_speed_prop = 0.001 * batter.speed + base_error_speed_prop
        random_error_speed = random.random()
        if third_base:
            additional_runs += 1
            third_base.stats.runs += 1
            third_base = None
        if second_base:
            if error_speed_prop > random_error_speed:
                additional_runs += 1
                second_base.stats.runs += 1
                second_base = None
            else:
                third_base = second_base
                second_base = None
        if first_base:
            if error_speed_prop > random_error_speed:
                third_base = first_base
                first_base = None
            else:
                second_base = first_base
                first_base = None
        first_base = batter
    elif result == "Single":
        base_single_speed_prop = 0.71
        single_speed_prop = 0.0013 * batter.speed + base_single_speed_prop
        random_single_speed_prop = random.random()
        if third_base:
            additional_runs += 1
            third_base.stats.runs += 1
            third_base = None
        if second_base:
            if single_speed_prop > random_single_speed_prop:
                additional_runs += 1
                second_base.stats.runs += 1
                second_base = None
            else:
                third_base = second_base
                second_base = None
        if first_base:
            if single_speed_prop > random_single_speed_prop:
                third_base = first_base
                first_base = None
            else: 
                second_base = first_base
                first_base = None
        first_base = batter
    elif result == "Double":
        double_speed_base_prop = 0.76
        double_speed_prop = 0.0015 * batter.speed + double_speed_base_prop
        random_double_speed_prop = random.random()
        if third_base:
            additional_runs += 1
            third_base.stats.runs += 1
            third_base = None
        if second_base:
            additional_runs += 1
            second_base.stats.runs += 1
            second_base = None
        if first_base:
            if double_speed_prop > random_double_speed_prop:
                additional_runs += 1
                first_base.stats.runs += 1
                first_base = None
            else: 
                third_base = first_base
                first_base = None
        second_base = batter
    elif result == "Triple":
        if third_base:
            additional_runs += 1
            third_base.stats.runs += 1
            third_base = None
        if second_base:
            additional_runs += 1
            second_base.stats.runs += 1
            second_base = None
        if first_base:
            additional_runs += 1
            first_base.stats.runs += 1
            first_base = None
        third_base = batter
    elif result == "Homerun":
        if third_base:
            additional_runs += 1
            third_base.stats.runs += 1
            third_base = None
        if second_base:
            additional_runs += 1
            second_base.stats.runs += 1
            second_base = None
        if first_base:
            additional_runs += 1
            first_base.stats.runs += 1
            first_base = None
        additional_runs += 1
        batter.stats.runs += 1
    elif result == "Walk":
        if first_base and second_base and third_base:
            third_base.stats.runs += 1
            third_base = None
            additional_runs += 1
        if first_base and second_base:
            third_base = second_base
            second_base = None
        if first_base:
            second_base = first_base
            first_base = None
        first_base = batter
    new_bases = [first_base, second_base, third_base]
    runs += additional_runs
    return new_bases, runs, additional_runs

def simulate_game(home, away):
    i = 0 # home batter index
    j = 0 # away batter index
    game_being_played = True # flag that keeps game going
    
    home_lineup = home.lineup
    home_pitcher = home.pitcher
    away_lineup = away.lineup
    away_pitcher = away.pitcher

    for i in range(len(home_lineup)):
        home_lineup[i].stats.games += 1
        away_lineup[i].stats.games += 1
    
    home_pitcher.stats.games += 1
    away_pitcher.stats.games += 1
    
    home_score = 0
    home_strikeouts = 0
    home_walks = 0
    home_hits = 0
    home_singles = 0
    home_doubles = 0
    home_triples = 0
    home_hrs = 0
    home_errors = 0
    
    away_score = 0
    away_strikeouts = 0
    away_walks = 0
    away_hits = 0
    away_singles = 0
    away_doubles = 0
    away_triples = 0
    away_hrs = 0
    away_errors = 0

    innings = 0

    while(game_being_played):
        innings += 1
        away_result = simulate_inning(home_pitcher, away_lineup, j)
        away_score += away_result["runs"]
        away_strikeouts += away_result["strikeouts"]
        away_walks += away_result["walks"]
        away_hits += away_result["hits"]
        away_singles += away_result["singles"]
        away_doubles += away_result["doubles"]
        away_triples += away_result["triples"]
        away_hrs += away_result["home_runs"]
        home_errors += away_result["errors"]
        j = away_result["next_batter_index"]

        if(innings >= 9):
            if(home_score > away_score):
                game_being_played = False
                break

        home_result = simulate_inning(away_pitcher, home_lineup, i)
        home_score += home_result["runs"]
        home_strikeouts += home_result["strikeouts"]
        home_walks += home_result["walks"]
        home_hits += home_result["hits"]
        home_singles += home_result["singles"]
        home_doubles += home_result["doubles"]
        home_triples += home_result["triples"]
        home_hrs += home_result["home_runs"]
        away_errors += home_result["errors"]
        i = home_result["next_batter_index"]

        if innings >= 9:
            if home_score != away_score:
                game_being_played = False
                break
    
    who_won_string = ""
    if home_score > away_score:
        who_won_team = home
        who_lost_team = away
    elif home_score < away_score:
        who_won_team = away
        who_lost_team = home
    who_won_string = who_won_team.name
    #Updating Team Stats:
    home.stats.runs_scored += home_score
    home.stats.runs_allowed += away_score
    home.stats.hits += home_hits
    home.stats.home_runs += home_hrs
    home.stats.errors += home_errors

    away.stats.runs_scored += away_score
    away.stats.runs_allowed += home_score
    away.stats.hits += away_hits
    away.stats.home_runs += away_hrs
    away.stats.errors += away_errors
    #print("The game is over in " + str(innings) + " innings with a score of " + str(home_score) + "-" + str(away_score) + " favoring the " + who_won_string + ".")
    #print("Home Team: Runs: " + str(home_score) + " Hits: " + str(home_hits) + " Errors: " + str(home_errors))
    #print("Away Team: Runs: "+ str(away_score) + " Hits: " + str(away_hits) + " Errors: " + str(away_errors))
    return {"Total Score": home_score + away_score, "Hits": home_hits + away_hits, "HRs": home_hrs + away_hrs, "Errors": home_errors + away_errors, "Winner": who_won_team, "Loser": who_lost_team}

def simulate_season(teams):
    season = Season(teams)
    for i in range(len(season.schedule)):
        game = simulate_game(season.schedule[i][0], season.schedule[i][1])
        winning_team = game["Winner"]
        losing_team = game["Loser"]
        winning_team.wins += 1
        losing_team.losses += 1
        season.season_games_played += 1
    return season

def simulate_series(matchup):
    team0_wins = 0
    team1_wins = 0
    while team0_wins < 2 and team1_wins < 2:
        who_won = simulate_game(matchup[0], matchup[1])["Winner"]
        if who_won.name == matchup[0].name:
            team0_wins += 1
        else:
            team1_wins += 1
    if team0_wins == 2:
        winner = matchup[0]
        loser = matchup[1]
        loser_wins = team1_wins
    elif team1_wins == 2:
        winner = matchup[1]
        loser = matchup[0]
        loser_wins = team0_wins
    winning_string = "The " + winner.name + " defeat the " + loser.name + " " + str(2) + "-" + str(loser_wins)
    return {"winner": winner, "string": winning_string}

def simulate_round(matchups):
    winner_list = []
    string_list = []
    for x in range(len(matchups)):
        series = simulate_series(matchups[x])
        winner = series["winner"]
        winning_string = series["string"]
        winner_list.append(winner)
        string_list.append(winning_string)
    return {"winners": winner_list, "strings": string_list}

def simulate_acc_tournament(season):
    sorted_teams = sorted(season.teams, key=lambda team: team.wins, reverse=True)
    matchup0 = [sorted_teams[0], sorted_teams[3]]
    matchup1 = [sorted_teams[1], sorted_teams[2]]
    semi_matchups = [matchup0, matchup1]
    print("ACC Semifinals Results:")
    round_result = simulate_round(semi_matchups)
    round_strings = round_result["strings"]
    round_winners = round_result["winners"]
    print(round_strings[0])
    print(round_strings[1])
    print("ACC Championship Result:")
    championship_matchup = [round_winners[0], round_winners[1]]
    championship_result = simulate_series(championship_matchup)
    print(championship_result["string"])
    champion = championship_result["winner"]
    return {"champion": champion, "championship_results": championship_result, "semifinal_results": round_result}

def simulate_dynasty_year(dynasty):
    dynasty_season = simulate_season(dynasty.teams)
    acc_tourney = simulate_acc_tournament(dynasty_season)
    dynasty.season_history.append(dynasty_season)
    champion_history = [acc_tourney["champion"], dynasty.current_year]
    dynasty.champion_history.append(champion_history)
    dynasty.current_year += 1
    reset_stats_after_season(dynasty.teams)

def progress_batter(batter):
    current_ovr = batter.get_overall()
    pot_gap = batter.potential - current_ovr
    if pot_gap >= 25:
        ovr_increase = random.randint(12, 20)
    elif pot_gap >= 15:
        ovr_increase = random.randint(10, 14)
    elif pot_gap >= 8:
        ovr_increase = random.randint(7, 10)
    elif pot_gap >= 1:
        ovr_increase = random.randint(3, 6)
    elif pot_gap <= 0:
        if batter.development_type == "normal":
            ovr_increase += random.randint(0, 4)
        elif batter.development_type == "gem":
            ovr_increase += random.randint(4, 8)
        else:
            ovr_increase -= random.randint(-2, 0)
    
    if batter.development_type == "gem":
        ovr_increase += random.randint(6, 12)
    elif batter.development_type == "bust":
        ovr_increase -= random.randint(2, 5)
    if current_ovr >= 93:
        ovr_increase = random.randint(1, 3)
    
    if ovr_increase < 0:
        for i in range(abs(ovr_increase)):
            attribute_downgrade = random.randint(1, 4)
            if attribute_downgrade == 1:
                batter.contact -= 1
            elif attribute_downgrade == 2:
                batter.power -= 1
            elif attribute_downgrade == 3:
                batter.speed -= 1
            else:
                batter.fielding -= 1
    else:
        for i in range(ovr_increase):
            attribute_upgrade = random.randint(1, 4)
            if attribute_upgrade == 1:
                batter.contact += 1
                if batter.contact > 99:
                    batter.contact = 99
            elif attribute_upgrade == 2:
                batter.power += 1
                if batter.power > 99:
                    batter.power = 99
            elif attribute_upgrade == 3:
                batter.speed += 1
                if batter.speed > 99:
                    batter.speed = 99
            else:
                batter.fielding += 1
                if batter.fielding > 99:
                    batter.fielding = 99

def progress_pitcher(pitcher):
    current_ovr = pitcher.get_overall()
    pot_gap = pitcher.potential - current_ovr
    if pot_gap >= 25:
        ovr_increase = random.randint(10, 16)
    elif pot_gap >= 15:
        ovr_increase = random.randint(6, 10)
    elif pot_gap >= 8:
        ovr_increase = random.randint(4, 8)
    elif pot_gap >= 1:
        ovr_increase = random.randint(3, 6)
    elif pot_gap <= 0:
        if pitcher.development_type == "normal":
            ovr_increase = random.randint(0, 4)
        elif pitcher.development_type == "gem":
            ovr_increase = random.randint(4, 8)
        else:
            ovr_increase = random.randint(-2, 0)
    
    if pitcher.development_type == "gem":
        ovr_increase += random.randint(6, 12)
    elif pitcher.development_type == "bust":
        ovr_increase -= random.randint(1, 4)
    if current_ovr >= 93:
        ovr_increase = random.randint(1, 3)
    
    if ovr_increase < 0:
        for i in range(abs(ovr_increase)):
            attribute_downgrade = random.randint(1, 3)
            if attribute_downgrade == 1:
                pitcher.velocity -= 1
            elif attribute_downgrade == 2:
                pitcher.control -= 1
            else:
                pitcher.stuff -= 1
    else:
        for i in range(ovr_increase):
            attribute_upgrade = random.randint(1, 3)
            if attribute_upgrade == 1:
                pitcher.velocity += 1
                if pitcher.velocity > 99:
                    pitcher.velocity = 99
            elif attribute_upgrade == 2:
                pitcher.control += 1
                if pitcher.control > 99:
                    pitcher.control = 99
            else:
                pitcher.stuff += 1
                if pitcher.stuff > 99:
                    pitcher.stuff = 99


def reset_stats_after_season(teams):
    for i in range(len(teams)):
        teams[i].stats = TeamStat()
        teams[i].wins = 0
        teams[i].losses = 0
        for k in range(len(teams[i].lineup)):
            player = teams[i].lineup[k]
            player.stats = BatterStat()
        teams[i].pitcher.stats = PitcherStat()