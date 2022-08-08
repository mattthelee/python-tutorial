from hero.hero import Hero


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
