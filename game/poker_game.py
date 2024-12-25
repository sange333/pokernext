from deck import Deck
from player import Player
from ai_player import AIPlayer
from betting import collect_bets, reset_bets
from game_rules import check_winner

class PokerGame:
    def __init__(self):
        self.players = [Player(f"玩家{i+1}") for i in range(1)] + [AIPlayer(f"AI{i+1}") for i in range(5)]
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0

    def deal_cards(self):
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]

    def play_round(self):
        self.deal_cards()
        self.community_cards = [self.deck.draw_card(), self.deck.draw_card(), self.deck.draw_card()]
        self.pot = collect_bets(self.players)
        winner = check_winner(self.players, self.community_cards)
        print(f"本轮获胜者是 {winner.name}")
        reset_bets(self.players)
