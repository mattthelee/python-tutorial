from hero.hero import Hero


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
