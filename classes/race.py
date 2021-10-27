import random
class Race:
    def __init__(self,name,health,strength,defense,speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
    
    def info(self):
        print(f"health: {self.health}")
        print(f"strength: {self.strength}")
        print(f"defense: {self.defense}")
        print(f"speed: {self.speed}")

def random_num(high_num):
    return random.randint(0, high_num)

all_races = {
    'human' : Race('human',100, random_num(30),random_num(30),random_num(30)),
    'dwarf' : Race('dwarf',150,random_num(50),random_num(30),random_num(10)),
    'elf' : Race('elf',300,random_num(40),random_num(40),random_num(50)),
    'halfling' : Race('halfling',150,random_num(20),random_num(50),random_num(40)),
    'orc' : Race('orc',100,random_num(50),random_num(30),random_num(15)),
    # 'tiefling' : Race('tiefling',200,10,10,10),
    'giant' : Race('giant',200,random_num(80),random_num(45),random_num(5)),
    'goblin' : Race('goblin',50,random_num(15),random_num(10),random_num(60)),
    'hobgoblin' : Race('hobgoblin',75,random_num(35),random_num(25),random_num(20)),
}

