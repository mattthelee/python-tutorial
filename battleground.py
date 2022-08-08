import numpy as np
import random
from superhero import Hero
from hero.villain import Villain
from potion.flightpotion import FlightPotion
from potion.strengthpotion import StrengthPotion


class Battleground:
    def __init__(
        self, name: str, location: str, weather: str, population: int, size: int
    ):

        self.name = name
        self.location = location
        self.weather = weather
        self.population = population
        self.size = size
        self.map = self.map_gen(size)
        self.character_dict = {}
        self.character_dict_name = {}
        self.fight_group_population = 0

    def map_gen(self, size):
        return np.zeros([size, size])

    def __str__(self):
        return str(self.map)

    def add_character(self, character: Hero, fight_group_no: int = None):
        if not fight_group_no:
            self.fight_group_population += 1
            self.character_dict[self.fight_group_population] = character
            self.character_dict_name[self.fight_group_population] = character.name
        else:
            self.character_dict[fight_group_no] = character
            self.character_dict_name[fight_group_no] = character.name

        rand_col = random.randint(0, self.size - 1)
        rand_row = random.randint(0, self.size - 1)
        if self.map[rand_col, rand_row] == 0.0:
            self.map[rand_col, rand_row] = (
                fight_group_no if fight_group_no else self.fight_group_population
            )
            # check_if_present = np.where(self.map == self.fight_group_population)
        else:
            self.character_dict[self.map[rand_col, rand_row]].fight(character)
            print(self.character_dict[self.map[rand_col, rand_row]].alive)
            if not self.character_dict[self.map[rand_col, rand_row]].alive:
                self.map[rand_col, rand_row] = (
                    fight_group_no if fight_group_no else self.fight_group_population
                )


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
