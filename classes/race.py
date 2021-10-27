class Race:
    def __init__(self,name,health,strength,defense,speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed

all_races = {
    'human' : Race('human',100,10,10,10)
}