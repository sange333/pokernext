from game.deck import Deck
from game.player import Player
from game.ai_player import AIPlayer
from game.betting import handle_betting_round, reset_bets
from game.hand_evaluator import compare_hands
from game.game_rules import check_winner
from game.game_state import GameState


class PokerGame:
    """
    德州扑克游戏主逻辑
    """
    def __init__(self):
        # 初始化玩家：1名人类玩家 + 5名AI玩家
        self.players = [Player("玩家1")] + [AIPlayer(f"AI 玩家 {i+1}") for i in range(5)]
        self.deck = Deck()  # 扑克牌组
        self.state = GameState(self.players)  # 游戏状态管理

    def deal_hands(self):
        """
        给每位玩家发两张手牌
        """
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]
            print(f"{player.name} 的手牌: {player.hand}")

    def deal_community_cards(self, count):
        """
        发放公共牌
        """
        for _ in range(count):
            card = self.deck.draw_card()
            self.state.add_community_card(card)

    def play_betting_round(self):
        """
        进行一轮下注
        """
        pot_addition = handle_betting_round(self.players, self.state.pot)
        self.state.add_to_pot(pot_addition)

    def play_game(self):
        """
        运行完整的游戏流程
        """
        print("开始新一局德州扑克游戏！")
        self.deck.reset_deck()  # 每局洗牌
        self.state.reset()  # 重置游戏状态

        # 1. 发手牌
        print("\n发手牌...")
        self.deal_hands()

        # 2. 第一次下注
        print("\n第一次下注...")
        self.play_betting_round()

        # 3. 发公共牌（翻牌）
        print("\n翻牌阶段...")
        self.deal_community_cards(3)
        self.state.display_state()
        self.play_betting_round()

        # 4. 发公共牌（转牌）
        print("\n转牌阶段...")
        self.deal_community_cards(1)
        self.state.display_state()
        self.play_betting_round()

        # 5. 发公共牌（河牌）
        print("\n河牌阶段...")
        self.deal_community_cards(1)
        self.state.display_state()
        self.play_betting_round()

        # 6. 决定胜负
        print("\n决胜阶段...")
        winner = check_winner(self.players, self.state.community_cards)
        if winner:
            print(f"{winner.name} 赢得本轮胜利，获得 {self.state.pot} 筹码！")
            winner.chips += self.state.pot
        else:
            print("本轮无胜者！")

        # 重置下注
        reset_bets(self.players)

    def play_multiple_games(self, num_games=5):
        """
        连续进行多局游戏
        """
        for i in range(1, num_games + 1):
            print(f"\n=== 第 {i} 局 ===")
            self.play_game()

            # 显示每位玩家的筹码数
            print("\n当前玩家筹码情况：")
            for player in self.players:
                print(f"{player.name}: {player.chips} 筹码")

            # 检查是否有玩家筹码耗尽
            self.players = [player for player in self.players if player.chips > 0]
            if len(self.players) < 2:
                print("游戏结束：不足两名玩家继续游戏！")
                break

        print("\n游戏结束！最终玩家筹码情况：")
        for player in self.players:
            print(f"{player.name}: {player.chips} 筹码")
