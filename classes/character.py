class Character:
    def __init__(self, name:str, race:Race, gold:int=0):
        self.name = name
        self.race = race
        self.gold = gold
        self.damage_taken = 0

    @property
    def base_stats(self):
        return {
            "strength" : self.race.strength,
            "defense" : self.race.defense,
            "speed" : self.race.speed
        }
    
    @property
    def stat_modifiers(self):
        return {
            'strength' : [],
            'defense' : [],
            'speed' : []
        }

    def calculate_stat(self, stat):
        modifiers = self.stat_modifiers.get(stat)
        stat_total = self.base_stats.get(stat)
        for modifier in modifiers:
            stat_total *= modifier
        return stat_total

    @property
    def current_health(self):
        return self.health - self.damage_taken

    def attack(self, other):
        pass

    def block(self, other):
        pass