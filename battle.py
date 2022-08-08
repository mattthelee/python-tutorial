from battleground import Battleground
from hero.hero import Hero
from hero.villain import Villain
from potion.basepotion import BasePotion
from potion.flight_potion import FlightPotion
from potion.strength_potion import StrengthPotion
import numpy as np


croydon = Battleground("Croydon", "London", "Rainy", 1000000, 5)
print(croydon)

batman = Hero(
    "The Batman", good=True, can_fly=False, strength=200, special_ability=0, alive=True
)

joker = Villain(
    "The Joker",
    good=False,
    can_fly=False,
    strength=10000,
    special_ability=10,
    alive=True,
)

hulk = Hero(
    "The Hulk", good=True, can_fly=False, strength=1000, special_ability=0, alive=True
)

for i in range(150):
    croydon.add_character(batman, 1)
    croydon.add_character(joker, 2)
    croydon.add_character(hulk, 3)

print(croydon)
print(croydon.character_dict_name)

no_of_batmans = np.where(croydon.map == 1)
no_of_jokers = np.where(croydon.map == 2)
no_of_hulks = np.where(croydon.map == 3)

print(f"No of Batmans = {len(no_of_batmans[0])}")
print(f"No of Jokers = {len(no_of_jokers[0])}")
print(f"No of Hulks = {len(no_of_hulks[0])}")


magic_flight_potion = FlightPotion()
magic_strength_potion = StrengthPotion()

batman.fight(joker)

batman.turnevil(hulk)
joker.drink_potion(magic_flight_potion)
batman.drink_potion(magic_strength_potion)
