from game.deck import Deck
from game.player import Player
from game.ai_player import AIPlayer
from game.betting import collect_bets, reset_bets
from game.hand_evaluator import evaluate_hand
from game.game_rules import check_winner


class PokerGame:
    def __init__(self):
        # 初始化玩家
        self.players = [Player("玩家")] + [AIPlayer(f"AI 玩家 {i+1}") for i in range(5)]
        self.deck = Deck()  # 初始化扑克牌组
        self.community_cards = []  # 公共牌
        self.pot = 0  # 当前奖池
        self.round = 0  # 游戏当前轮次

    def deal_hands(self):
        """发两张手牌给每个玩家"""
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]
            print(f"{player.name} 的手牌: {player.hand}")

    def deal_community_cards(self, count):
        """发公共牌"""
        for _ in range(count):
            card = self.deck.draw_card()
            self.community_cards.append(card)

    def play_betting_round(self):
        """进行一轮下注"""
        print("\n进行一轮下注...")
        self.pot += collect_bets(self.players)

    def play_game(self):
        """完整游戏流程"""
        print("开始一场新的德州扑克游戏！\n")
        self.round += 1
        self.deck.reset_deck()  # 每轮洗牌
        self.community_cards = []  # 重置公共牌

        # 1. 发手牌
        print("\n发手牌...")
        self.deal_hands()

        # 2. 下注（第1轮）
        self.play_betting_round()

        # 3. 发公共牌（翻牌）
        print("\n翻牌...")
        self.deal_community_cards(3)
        print(f"公共牌: {self.community_cards}")
        self.play_betting_round()

        # 4. 发公共牌（转牌）
        print("\n转牌...")
        self.deal_community_cards(1)
        print(f"公共牌: {self.community_cards}")
        self.play_betting_round()

        # 5. 发公共牌（河牌）
        print("\n河牌...")
        self.deal_community_cards(1)
        print(f"公共牌: {self.community_cards}")
        self.play_betting_round()

        # 6. 决定胜负
        print("\n最终结果...")
        winner = check_winner(self.players, self.community_cards)
        print(f"胜者是: {winner.name}，赢得 {self.pot} 筹码！")
        winner.chips += self.pot

        # 重置玩家下注
        reset_bets(self.players)
