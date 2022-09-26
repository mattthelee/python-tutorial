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
        self.map_id = None

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
