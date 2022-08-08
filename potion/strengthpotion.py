from potion.basepotion import BasePotion


class StrengthPotion(BasePotion):
    def __init__(self, **kwargs):
        strength_percent = 10
        super().__init__(strength_percent=strength_percent, **kwargs)
