from basepotion import BasePotion


class FlightPotion(BasePotion):
    def __init__(self, **kwargs):
        gives_flight = True
        super().__init__(gives_flight=gives_flight, **kwargs)

    def __str__(self):
        return "A flight potion"
