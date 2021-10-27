# from abc import ABC,abstractmethod

# class Item(ABC):
#     all_items = {}
#     def __init__(self):
#         Item.all_items[self.__class__.__name__.lower()] = self.__class__

#     @abstractmethod
#     def use(self):
#         pass

# class Potion(Item):
#     def use(self, character):
#         character.health += 30

# class StoneSkin(Item):
#     def use(self, character):
#         character.stat_modifiers['defense'].append(1.5)

# potion = Potion()
