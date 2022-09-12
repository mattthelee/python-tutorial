from hero.hero import Hero
from hero.villain import Villain
from battleground import Battleground

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


def populate_map(battleground):
    my_map = battleground.map
    my_map[2, 2] = 4
    my_map[3, 3] = 5
    my_map[1, 1] = 6
    my_map[1, 4] = 7
    my_map[1, 0] = 8
    my_map[0, 4] = 9
    return my_map


print(populate_map(croydon))


croydon.move_character_down(6)
croydon.move_character_up_2(4)
croydon.move_character_up_2(4)
croydon.move_character_up_2(4)
croydon.move_character_up_2(4)
croydon.move_character_up_2(4)
croydon.move_character_up_2(4)
croydon.move_character_left(7)


print("------------------------")
print(croydon.map)
