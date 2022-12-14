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
