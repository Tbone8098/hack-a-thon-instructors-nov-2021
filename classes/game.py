from character import Character
from race import all_races
import random

class Game:
    def __init__(self):
        self.running = False
        self.player = None
        self.enemy = None
        self.state = 'play'

    def create_character(self):
        name = input("Choose a name: ")
        print(f'Races: {", ".join(race for race in all_races)}')
        while (race := input("Choose a race: ")) not in all_races:
            print("Please choose a valid race!")
        self.player = Character(name,all_races.get(race))
        return self

    def do_battle(self):
        self.enemy = Character('enemy',all_races['human'],100)
        while self.enemy.current_health >= 0 and self.player.current_health >= 0:
            command, *arguments = input("Choose a command: ").strip().split(' ')
            enemy_choice = random.choice(['attack','block'])
            if self.player.base_stats['speed'] >= self.enemy.base_stats['speed']:
                self.run_command(command,arguments)
                self.enemy.actions[enemy_choice](self.player)
            else:
                self.enemy.actions[enemy_choice](self.player)
                self.run_command(command,arguments)
        self.state = "shop"

    def shop_for_items(self):
        print("Welcome to the shop!")
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
            if command == "attack":
                self.player.attack(self.enemy)
            elif command == "block":
                self.player.block(self.enemy)
            elif command == "use":
                item_name = arguments[0]
                if item_name in self.player.items:
                    item = self.player.items[item_name]
                    item.use()
                    # self.player.items.pop(arguments[0])
                else:
                    print("Invalid item!")
            elif command == "flee":
                if random.randint(0,1):
                    self.state == "shop"
                    print("Successfully escaped! Returning to shop")
                else:
                    print("Failed to flee!")
        elif self.state == "shop":
            if command == "leave":
                self.state = "battle"
            
            #shop commands