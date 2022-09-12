from multiprocessing.sharedctypes import Value
import random
from re import X
import numpy as np
from hero.hero import Hero


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

    def move_character(self):
        return

    def find_first_instance_of_character(self, character_name):
        # given a character name, find the x and y coords on the map
        y, x = np.argwhere(self.map == character_name)[0]
        return y, x

    def switch_character(self, character_one, character_two):
        # Take two characters, find them and switch their positions on the map
        character_one_x, character_one_y = np.argwhere(self.map == character_one)[0]
        character_two_x, character_two_y = np.argwhere(self.map == character_two)[0]
        self.map[character_one_x, character_one_y] = character_two
        self.map[character_two_x, character_two_y] = character_one
        return character_one, character_two

    def add_boundaries(self):
        # Add a wall around the outer
        return

    def amount_of_heroes(self):

        amount = self.map
        return np.unique(amount)

    def check_for_character(self, character_name):
        num = character_name
        arr = self.map

        return num in arr

    def top_row(self):

        row = self.map[0]
        return row

    def char_top_row(self, character_name):
        num = character_name
        row = self.map[0]

        return num in row

    def small_value(self):
        small_value = np.min(self.map)
        return small_value

    def axis_find(self, x, y):
        return self.map[y, x]

    def move_character_down(self, character_name):

        max_y = self.map.shape[0]
        min_y = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x
        new_y = y + 1
        if new_y <= max_y and new_y >= min_y:
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

    def move_character_up(self, character_name):
        max_y = self.map.shape[0]
        min_y = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x
        new_y = y - 1
        if new_y <= max_y and new_y >= min_y:
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

    def move_character_left(self, character_name):
        max_x = self.map.shape[1]
        min_x = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x - 1
        new_y = y
        if new_x <= max_x and new_x >= min_x:
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

    def move_character_right(self, character_name):
        max_x = self.map.shape[1]
        min_x = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x + 1
        new_y = y
        if new_x <= max_x and new_x >= min_x:
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

    def move_character_up_2(self, character_name):
        max_y = self.map.shape[0]
        min_y = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x
        new_y = y - 1
        if new_y <= max_y and new_y >= min_y:
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

        # if new_y < array[1]:
        #  self.map[new_y, new_x] = character_name
        #  self.map[coords] = 0

    #  else:
    #  print(f"The map is too small to move", character_name)
