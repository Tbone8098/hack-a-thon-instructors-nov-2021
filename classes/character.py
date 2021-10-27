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

    def info(self):
        print(f"""{f' {self.name} ':*^80}""")
        print(f"race: {self.race.name}")
        print(f"gold: {self.gold}")
        print(f"damage_taken: {self.damage_taken}")
        for stat, val in self.base_stats.items():
            print(f"{stat}: {val}")
            
        print(f"attack_skills:...")
        for skill in self.attack_skills:
            print("> " + skill.name)

        print(f"items ... ")
        if len(self.items) == 0:
            print("> you have no items")
        else: 
            for item in self.items:
                print(f"> {item.name}")
        return self

    @property
    def base_stats(self):
        return {
            "strength" : self.race.strength,
            "defense" : self.race.defense,
            "speed" : self.race.speed,
            "health": self.race.health
        }
    
    @property
    def stat_modifiers(self):
        return {
            'strength' : [],
            'defense' : [],
            'speed' : []
        }

    @property
    def actions(self):
        return {
            "attack" : self.attack,
            "block" : self.block
        }

    def calculate_stat(self, stat):
        modifiers = self.stat_modifiers.get(stat)
        stat_total = self.base_stats.get(stat)
        for modifier in modifiers:
            stat_total *= modifier
        return stat_total

    @property
    def current_health(self):
        return self.base_stats['health'] - self.damage_taken

    def attack(self, other):
        hit = random.randint(0,20)
        chance_to_hit = (self.race.strength * other.race.defense) / 10
        print(f"hit roll: {hit} || chance to hit: {chance_to_hit}")

    def block(self, other):
        pass

