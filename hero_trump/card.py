import random
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import uvicorn
import csv

class Card():
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

    def __str__(self):
        return (self.name)

    def __repr__(self):
        return str(self.name)

    def assign_card(self, row):
        self.name = row[0]
        self.number = row[1]
        self.category = row[2]
        self.strength = row[3]
        self.intelligence = row[4]
        self.defense = row[5]
        self.power = row[6]
        self.magic = row[7]
        self.tools = row[8]
        self.present=True

    def card_info(self):
        print(self.name, "is a", self.category, "and their stats are:""\n"
              "Strength:", self.strength,"\n"
              "Intelligence:", self.intelligence,"\n"
              "Defense:", self.defense,"\n"
              "Magic:", self.magic,"\n"
              "Power:", self.power,"\n"
              "Tools:", self.tools,
              )

class Deck:
    def __init__(
        self,
        cards,
    ):
        self.cards = cards
        self.length = len(cards)

    def read_cards(self):
        with open('Cards.csv', 'r') as file:  
            reader = csv.reader(file)
            for row in reader:
                newcard = Card()
                newcard.assign_card(row)
                cards.append(newcard)

    def add_card(new_card):
        i = new_card
        if i in cards:
            print("This card is already in the deck.")
        else:
            cards.append(new_card)

    def remove_card(card_to_remove):
        i = card_to_remove
        if i in cards:
            cards.remove(card_to_remove)
        else:
            print("This card is already not in the deck.")

    def find_card(card_to_find):
        i = card_to_find
        if i in cards:
            print(card_to_find)
        else:
            print(card_to_find, "cannot be found in the deck.")

    def shuffle_cards():
        random.shuffle(cards)


cards = []

mydeck = Deck(cards)

mydeck.read_cards()

print(cards)

Deck.find_card(cards[2])     #test for finding a card in the deck

Deck.shuffle_cards()    #test for shuffling cards

print(cards[2].category)

Deck.remove_card(cards[5])   #test for removing a card from the deck

print(cards)


def create_app():
    app = FastAPI(
        title="Server",
        description="database for cards",
        version="0.0.1"
    )
    return app

app = create_app()

@app.get("/hello")
async def main():
    return("Welcome!")

@app.get("/card/")
async def show_cards(card: Card):
    return card

@app.post("/cards/")
async def create_card(card: Card):
   Deck.add_card(card)
   return card



# python -m uvicorn card:app --reload     --------------------------- command for running API

