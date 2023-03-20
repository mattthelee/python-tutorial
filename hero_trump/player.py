
import random
import csv
import re


class Player:
    def __init__(self, username):
        self.username = username
        self.record = {'wins': 0, 'losses': 0, 'draws': 0}
        self.last_five_games = []
        self.elo = self.calc_elo()
    
    def get_display_record(self):
        print(f"{self.username}'s current record is {self.record['wins']}-{self.record['losses']}-{self.record['draws']}")


    def create_player(username, wins=0, losses=0, draws=0):
    # Open the CSV file in append mode
        with open('players.csv', 'a', newline='') as csvfile:
        # Create a CSV writer object
            writer = csv.writer(csvfile, delimiter=',')
        # Write the new player's data to the file
            writer.writerow([username, f'Wins: {wins}, Losses: {losses}, Draws: {draws}'])
        



class PlayerDatabase2:
    def __init__(self):
        self.data = {}
        self.load_dbase()
 
    def load_dbase(self):
        with open('players.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                username = row[0]
                record_str = row[1]
                record_parts = [part.strip() for part in record_str.split(",")] 
                wins = record_parts[0].split(":")[1].strip()
                losses = record_parts[1].split(":")[1].strip()
                draws = record_parts[2].split(":")[1].strip()
                record = f"Wins: {wins}, Losses: {losses}, Draws: {draws}"
                self.data[username] = record
            
    def print_all(self):
        for username, record in self.data.items():
                print(f'{username}: {record}')

    def indiv_rec(self, username):
        if username in self.data:
            record = self.data[username]
            print(f"{username}: {record}")

        else:
            print(f"No record found for user {username}")

                           

    def get_elo(self, username, initial_rating=1200, k_factor=32):
        rating = initial_rating
        username = username  # Replace with the actual player's username
        record = self.data.get(username)
        if username in self.data:
            wins = int(record.split(",")[0].split(":")[1])
            losses = int(record.split(",")[1].split(":")[1])
            draws = int(record.split(",")[2].split(":")[1])
            for i in range(wins):
                rating += k_factor * (1 - 1 / (1 + 10 ** ((1200 - rating) / 400)))
            for i in range(losses):
                rating += k_factor * (0 - 1 / (1 + 10 ** ((1200 - rating) / 400)))
            for i in range(draws):
                rating += k_factor * (0.5 - 1 / (1 + 10 ** ((1200 - rating) / 400)))
            return rating

        else:
            return



            
    def print_elo(self, username):
        rating = self.get_elo(username)  # calculate Elo rating
        if username in self.data:
            print(f"{username}'s ELO is: {rating}")
            return rating
        
        else:
            print(f"No record found for user {username}")





class MatchMaking:
    def __init__(self, player_db):
        self.player_db = player_db
        player_db = PlayerDatabase2()

    def find_opponent(self, player_name):
        player_elo = self.player_db.get_elo(player_name)

        # Find the opponent with the closest ELO to the player
        closest_elo_diff = float('inf')
        closest_opponent = None
        for opponent_name, _ in self.player_db.data.items():
            if opponent_name == player_name:
                continue
            opponent_elo = self.player_db.get_elo(opponent_name)
            elo_diff = abs(player_elo - opponent_elo)
            if elo_diff < closest_elo_diff:
                closest_elo_diff = elo_diff
                closest_opponent = opponent_name

        return closest_opponent














pd = PlayerDatabase2()


mm = MatchMaking(pd)

Player.create_player("Jamie")
pd.print_elo("Liam")
pd.print_elo("Alice")
pd.print_elo("Ringo")
pd.print_all()