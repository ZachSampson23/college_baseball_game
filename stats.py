class BatterStat:
    def __init__(self):
        self.games = 0
        self.at_bats = 0
        self.hits = 0
        self.singles = 0
        self.doubles = 0
        self.triples = 0
        self.home_runs = 0
        self.walks = 0
        self.strikeouts = 0
        self.runs = 0
        self.rbi = 0
    
    def record_result(self, result, runs):
        if result == "Error":
            self.at_bats += 1
        elif result == "Walk":
            self.walks += 1
            self.rbi += runs
        else:
            self.at_bats += 1
        if result in ["Single", "Double", "Triple", "Homerun"]:
            self.hits += 1
            if result == "Single":
                self.singles += 1
            elif result == "Double":
                self.doubles += 1
            elif result == "Triple":
                self.triples += 1
            elif result == "Homerun":
                self.home_runs += 1
            self.rbi += runs
        elif result == "Strikeout":
            self.strikeouts += 1
        elif result == "Out":
            pass
    
    def get_stats(self):
        total_bases = self.singles + 2*self.doubles + 3*self.triples + 4*self.home_runs
        if self.at_bats == 0:
            average = 0
            slugging = 0
        else:
            average = self.hits / self.at_bats
            slugging =  total_bases / self.at_bats
        if self.walks + self.at_bats == 0:
            on_base_percentage = 0
        else:
            on_base_percentage = (self.walks + self.hits) / (self.walks + self.at_bats)
        on_base_plus_slugging = on_base_percentage + slugging
        return {"obp": on_base_percentage, "avg": average, "tb": total_bases, "slg": slugging, "ops": on_base_plus_slugging}
    
class PitcherStat:
    def __init__(self):
        self.games = 0
        self.outs_recorded = 0
        self.hits_allowed = 0
        self.runs_allowed = 0
        self.earned_runs = 0
        self.walks_allowed = 0
        self.strikeouts = 0
        self.home_runs_allowed = 0
    
    def record_result(self, result, runs):
        if result == "Out":
            self.outs_recorded += 1
        if result == "Strikeout":
            self.outs_recorded += 1
            self.strikeouts += 1
        elif result in ["Single", "Double", "Triple", "Homerun"]:
            self.hits_allowed += 1
            self.earned_runs += runs
            self.runs_allowed += runs
            if result == "Homerun":
                self.home_runs_allowed += 1
        elif result == "Walk":
            self.walks_allowed += 1
            self.earned_runs += runs
            self.runs_allowed += runs
        elif result == "Error":
            self.runs_allowed += runs
    
    def get_stats(self):
        innings_pitched = int(self.outs_recorded / 3) + 0.1 * (self.outs_recorded % 3) 
        innings_for_stats = self.outs_recorded / 3 
        if innings_for_stats == 0: 
            era = 0 
            whip = 0 
            k_per_nine = 0 
            bb_per_nine = 0 
        else: 
            era = self.earned_runs / (innings_for_stats / 9) 
            whip = (self.hits_allowed + self.walks_allowed) / innings_for_stats 
            k_per_nine = self.strikeouts / innings_for_stats * 9 
            bb_per_nine = self.walks_allowed / innings_for_stats * 9 
            return {"ip": innings_pitched, "era": era, "whip": whip, "K/9": k_per_nine, "BB/9": bb_per_nine}
