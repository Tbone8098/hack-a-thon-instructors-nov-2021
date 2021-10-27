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

class Character:
    def __init__(self, name:str, race:Race):
        self.name = name
        self.race = race
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

class Game:
    def __init__(self):
        self.running = False
        self.player = None
        self.state = 'play'

    def create_character(self):
        name = input("Choose a name: ")
        print(f'Races: {", ".join(race for race in all_races)}')
        while (race := input("Choose a race: ")) not in all_races:
            print("Please choose a valid race!")
        self.player = Character(name,all_races.get(race))
        return self

    def do_battle(self):
        enemy = Character('enemy',10,10,)
        while enemy.health >= 0 and self.player.health >= 0:
            command, *arguments = input("Choose a command: ").strip().split(' ')
            self.run_command(command,arguments)
        self.state = "shop"


    def shop_for_items(self):
        while self.state == "shop":
            command, *arguments = input("Choose a command: ").strip().split(' ')
            self.run_command(command,arguments)


    def play(self):
        self.running = True
        self.state = "battle"
        while self.running:
            if self.state == 'battle':
                self.do_battle()
            if self.state == 'shop':
                self.shop_for_items()


    def run_command(self, command:str, arguments:list):
        if self.state == "battle":
            pass
            #battle commands
        elif self.state == "shop":
            if command == "leave":
                self.state = "battle"
            #shop commands

if __name__ == "__main__":
    game = Game()
    game.create_character()
    game.play()