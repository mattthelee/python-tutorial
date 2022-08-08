import numpy as np
import random


class Hero:
    def __init__(
        self,
        name,
        good=True,
        can_fly=True,
        strength=50,
        special_ability=10,
        alive=True,
        identity_found=False,
        arrested=False,
    ):

        self.name = name
        self.good = good
        self.can_fly = can_fly
        self.strength = strength
        self.special_ability = special_ability
        self.alive = alive
        self.identity_found = identity_found
        self.arrested = arrested

    def fight(self, target_hero):
        # accepts another animal as an argument X
        # Checks that this animal is a carnivore X

        # increases the weight of this animal X
        if target_hero.good and self.good:
            print(f"{self} didn't fight {target_hero}!")
            return

        elif (not target_hero.can_fly) and self.can_fly:
            print(f"{self} flew away from {target_hero}")
            return

        elif target_hero.special_ability < self.special_ability:
            print(f"{self}'s special ability was too much work for {target_hero}")
            return

        elif target_hero.strength < self.strength:
            target_hero.alive = False
            print(f"{self} has killed {target_hero} ")

        else:
            self.alive = False
            print(f"{self} had a fight with {target_hero} and lost")

    def turnevil(self, target_hero):

        if target_hero.good:
            target_hero.good = False
            print(f"{target_hero} has turned evil due to {self} turning on them!")

    def flymate(self, hero_passenger):
        if self.can_fly and not hero_passenger.can_fly:
            hero_passenger.can_fly = True
            print(f"{self} has flown and carried {hero_passenger} on the way!")

        else:
            return

    def __str__(self):
        return self.name

    def drink_potion(self, potion):
        print(f"{self} drank a {potion} potion!")
        potion.alter(self)


class Villain(Hero):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{args[0]} has been created with args")

    def flyenemy(self, fly_enemy):
        if self.can_fly and not fly_enemy.can_fly:
            self.alive = False
            print(
                f"{self} has flown away and picked up {fly_enemy} on the way and dropped them to their mercy!"
            )

        else:
            print(f"{self} attempted to fly away and then remembered they can't!")


class Citizen(Hero):
    def __init__(
        self,
        name,
        good=True,
        can_fly=True,
        strength=50,
        special_ability=10,
        alive=True,
        identity_found=False,
        arrested=False,
    ):
        super().__init__(
            name,
            good,
            can_fly,
            strength,
            special_ability,
            alive,
            identity_found,
            arrested,
        )

    def witnessed(self, target_hero):
        if self.fight and not target_hero.alive:
            self.arrested = True
            self.identity_found = True
            print(
                f"The police have arrested {self} due to the fight with {target_hero} and his identity has been revealed!"
            )


# A potion for strength
# reusrrection
# flight
# Each potion changes the attribute of the hero that uses it
class BasePotion:
    def __init__(
        self,
        strength_percent=1,
        gives_flight=False,
        gives_special_ability=10,
        resurrects=False,
    ):
        self.gives_flight = gives_flight
        self.strength_percent = strength_percent
        self.gives_special_ability = gives_special_ability
        self.resurrects = resurrects

    def __str__(self):
        return "A mysterious potion"

    def alter(self, target_hero):
        target_hero.can_fly = self.gives_flight or target_hero.can_fly
        target_hero.strength *= self.strength_percent
        target_hero.special_ability = self.gives_special_ability
        target_hero.alive = self.resurrects or target_hero.alive


class FlightPotion(BasePotion):
    def __init__(self, **kwargs):
        gives_flight = True
        super().__init__(gives_flight=gives_flight, **kwargs)

    def __str__(self):
        return "A flight potion"


class StrengthPotion(BasePotion):
    def __init__(self, **kwargs):
        strength_percent = 10
        super().__init__(strength_percent=strength_percent, **kwargs)


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
