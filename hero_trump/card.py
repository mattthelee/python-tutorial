import csv

class Card:
    def __init__(
        self,
        name=str,
        number=int,
        category=str,
        strength=int,
        intelligence=int,
        defense=int,
        power=int,
        magic=int,
        tools=int,
        present=False
    ):

        self.name = name
        self.number = number
        self.category = category
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense
        self.power = power
        self.magic = magic
        self.tools = tools
        self.present = present


    def assign_card(self):
        with open('Cards.txt') as f:
            lines = f.readlines()
            num = self.number
            splitlines  = lines[num].split(',')
            self.name = splitlines[0]
            self.number = splitlines[1]
            self.category = splitlines[2]
            self.strength = splitlines[3]
            self.intelligence = splitlines[4]
            self.defense = splitlines[5]
            self.power = splitlines[6]
            self.magic = splitlines[7]
            self.tools = splitlines[8]
            self.present=True,
    
    def card_info(self):
        print(self.name, "is a", self.category, "and their stats are:""\n"
              "Strength:", self.strength,"\n"
              "Intelligence:", self.intelligence,"\n"
              "Defense:", self.defense,"\n"
              "Magic:", self.magic,"\n"
              "Power:", self.power,"\n"
              "Tools:", self.tools,
              )

c1 = Card("null", 0, "null", 0, 0, 0, 0, 0, 0, False)
c2 = Card("null", 1, "null", 0, 0, 0, 0, 0, 0, False)
c3 = Card("null", 2, "null", 0, 0, 0, 0, 0, 0, False)
c4 = Card("null", 3, "null", 0, 0, 0, 0, 0, 0, False)
c5 = Card("null", 4, "null", 0, 0, 0, 0, 0, 0, False)
c6 = Card("null", 5, "null", 0, 0, 0, 0, 0, 0, False)
c7 = Card("null", 6, "null", 0, 0, 0, 0, 0, 0, False)
c8 = Card("null", 7, "null", 0, 0, 0, 0, 0, 0, False)
c9 = Card("null", 8, "null", 0, 0, 0, 0, 0, 0, False)
c10 = Card("null", 9, "null", 0, 0, 0, 0, 0, 0, False)

c1.assign_card()
c2.assign_card()
c3.assign_card()
c4.assign_card()
c5.assign_card()
c6.assign_card()
c7.assign_card()
c8.assign_card()
c9.assign_card()
c10.assign_card()

c4.card_info()

