from race import Race
from attack_skill import AttackSkill
import random

class Character:
    def __init__(self, name:str, race:Race, gold:int=0):
        self.name = name
        self.race = race
        self.gold = gold
        self.damage_taken = 0
        self.attack_skills = [AttackSkill('melee')]
        self.items = {}

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
        hit = random.randint(0,20)
        chance_to_hit = (self.race.strength * other.race.defense) / 100
        print(f"hit roll: {hit} || chance to hit: {chance_to_hit}")

    def block(self, other):
        pass

