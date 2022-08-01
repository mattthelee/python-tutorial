from hero import Hero
from random import random

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

