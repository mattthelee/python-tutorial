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

    def add_character(
        self, character: Hero, y_pos, x_pos
    ):  # can then run from battle.py, hero uses hero name from battle.py and then you can input own coors in the same section on battle.py (hulk, 2,1 etc)
        self.fight_group_population += 1  # make the population per char 1
        self.character_dict[self.fight_group_population] = character
        character.map_id = self.fight_group_population
        self.map[
            y_pos, x_pos
        ] = (
            self.fight_group_population
        )  # takes the coords from char and takes population

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

    def move_character_down(self, character_name, character_dict_name):

        max_y = self.map.shape[0] - 1
        min_y = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x
        new_y = y + 1
        if new_y <= max_y and new_y >= min_y:
            character_on_pos = self.map[new_y, new_x] != 0
            if character_on_pos:
                self.character_dict
                moving_character = character_on_pos
                destination_character = character_on_pos[character_dict_name]

                moving_character.fight(destination_character)

                print(self.character_dict[character_name])
                new_destination_name = self.map[new_y, new_x]
                print(self.character_dict[new_destination_name])
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

    def move_character_up(self, character_name):
        max_y = self.map.shape[0] - 1
        min_y = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x
        new_y = y - 1
        if new_y <= max_y and new_y >= min_y:
            character_on_pos = self.map[new_y, new_x] != 0
            if character_on_pos:
                print(self.character_dict[character_name])
                new_destination_name = self.map[new_y, new_x]
                print(self.character_dict[new_destination_name])
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

    def move_character_left(self, character_name):
        max_x = self.map.shape[1] - 1
        min_x = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x - 1
        new_y = y
        if new_x <= max_x and new_x >= min_x:
            character_on_pos = self.map[new_y, new_x] != 0
            if character_on_pos:
                print(self.character_dict[character_name])
                new_destination_name = self.map[new_y, new_x]
                print(self.character_dict[new_destination_name])
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0

        else:
            print(f"The map is too small to move", character_name)

    def move_character_right(self, character_name):
        max_x = self.map.shape[1] - 1
        min_x = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x + 1
        new_y = y
        if new_x <= max_x and new_x >= min_x:
            character_on_pos = self.map[new_y, new_x] != 0
            if character_on_pos:
                print(self.character_dict[character_name])
                new_destination_name = self.map[new_y, new_x]
                print(self.character_dict[new_destination_name])
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

    def move_character_up_2(self, character_name):
        max_y = self.map.shape[0] - 1
        min_y = 0
        y, x = self.find_first_instance_of_character(character_name)
        new_x = x
        new_y = y - 1
        if new_y <= max_y and new_y >= min_y:
            character_on_pos = self.map[new_y, new_x] != 0
            if character_on_pos:
                print(self.character_dict[character_name])
                new_destination_name = self.map[new_y, new_x]
                print(self.character_dict[new_destination_name])
            self.map[new_y, new_x] = character_name
            self.map[y, x] = 0
        else:
            print(f"The map is too small to move", character_name)

#my 7 substeps:
#Which character is currently moving (store for later)
#What is their current position?
#Where is the character moving?
#What id is at the destination position?
#Check if that id is non-zero: if it's zero we just move there
#What character is at the destination (need to use our self.character_dict to map between id and chracter)
#Start fight between moving character and destination character




    def move_character_up(self, character_id):
        y, x = self.find_first_instance_of_character(character_id)
        new_x = x
        new_y = y - 1
        destination_id = self.map[new_y, new_x]
        check_id_is_nonzero = destination_id != 0
        if check_id_is_nonzero:
            # Do the fight
            moving_character = self.character_dict[character_id]
            destination_character = self.character_dict[destination_id]
            winner_of_fight = moving_character.fight(destination_character)
            # Move winner into the new position
            # get the winning character (already done)
            # get new position (already have)
            # get winning character's id
            winner_id = winner_of_fight.map_id
            
            # assign winning id to new position
            self.map[new_y, new_x] = winner_id



            # Loser character removed from map

        else:
            # Just move there
            print("moved")

