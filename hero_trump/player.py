
import random

class Player:
    def __init__(self, username):
        self.username = username
        self.record = {'wins': 0, 'losses': 0, 'draws': 0}
        self.current_cards = []
        self.last_five_games = []
        self.elo = self.calc_elo()
    
    def get_display_record(self):
        print(f"{self.username}'s current record is {self.record['wins']}-{self.record['losses']}-{self.record['draws']}")


    def calc_elo(self, k_factor=32, initial_rating=1200):
        wins = self.record['wins']
        losses = self.record['losses']
        draws = self.record['draws']
        rating = initial_rating

        if wins + losses + draws == 0:
            return rating
        expected_score = (wins + 0.5 * draws) / (wins + losses + draws)
        rating += k_factor * (wins - expected_score * (wins + losses + draws))
        return int(rating)

    def get_elo(self):
        elo_rating = self.calc_elo()
        print(f"Players Elo rating: {elo_rating}")


        


class MatchPlayers:

    def __init__(self, record, last_five_games):
        self.record = record
        self.last_five_games = last_five_games


    def match_players(self, player_list_elo1, player_list_elo2, last_five_games):
        if last_five_games.count('win') <= 3:
            player_list_elo1.append(self)
        else:
            player_list_elo2.append(self)

    def find_opposition(self, player_list):
        players_for_game = random.sample(player_list, 2)
        return players_for_game

