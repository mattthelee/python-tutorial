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


croydon.add_character(hulk, 1, 2)
croydon.add_character(joker, 3, 4)
croydon.add_character(batman, 4, 4)


print(croydon.map)
croydon.move_character_up(1)
croydon.move_character_left(2)
croydon.move_character_down(3)
croydon.move_character_right(3)

print("------------------------")
print(croydon.map)
