from character import Character

class Shop:
    def __init__(self, items:list):
        self.items = items
    



class Item:
    def __init__(self, name:str, amount, character:Character, price:int):
        self.name = name
        self.amount = amount
        self.character = character
        self.price = price



class HealthPotion(Item):
    def __init__(self, name: str, amount:int, character:Character, price:int):
        super().__init__(name, amount, character, price)
    
    def use(self):
        self.character.race.health += self.amount
        self.character.items.pop(self.name)
        print(f"You drank {self.name} and gained {self.amount} HEALTH")



class StrengthPotion(Item):
    def __init__(self, name: str, amount:float, character:Character, price:int):
        super().__init__(name, amount, character, price)

    def use(self):
        self.character.stat_modifiers['strength'].append(self.amount)
        self.character.items.pop(self.name)
        print(f"You drank {self.name} and gained a STRENGTH modifier of {self.amount}")


class DefensePotion(Item):
    def __init__(self, name: str, amount:float, character:Character, price:int):
        super().__init__(name, amount, character, price)

    def use(self):
        self.character.stat_modifiers['defense'].append(self.amount)
        self.character.items.pop(self.name)
        print(f"You drank {self.name} and gained a DEFENSE modifier of {self.amount}")



class SpeedPotion(Item):
    def __init__(self, name: str, amount:float, character:Character, price:int):
        super().__init__(name, amount, character, price)

    def use(self):
        self.character.stat_modifiers['speed'].append(self.amount)
        self.character.items.pop(self.name)
        print(f"You drank {self.name} and gained a SPEED modifier of {self.amount}")



