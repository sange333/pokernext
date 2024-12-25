from game.deck import Deck
from game.player import Player
from game.ai_player import AIPlayer
from game.betting import handle_betting_round, reset_bets
from game.hand_evaluator import compare_hands
from game.game_rules import check_winner
from game.game_state import GameState
from game.utils import display_cards


class PokerGame:
    """
    德州扑克游戏主逻辑
    """
    def __init__(self):
        # 初始化玩家：1名人类玩家 + 5名AI玩家
        self.players = [Player("玩家1")] + [AIPlayer(f"AI 玩家 {i+1}") for i in range(5)]
        self.deck = Deck()  # 扑克牌组
        self.state = GameState(self.players)  # 游戏状态管理
        self.dealer_index = 0  # 庄家的索引

    def rotate_dealer(self):
        """
        轮换庄家，每局游戏后将庄家顺时针切换到下一位玩家
        """
        self.dealer_index = (self.dealer_index + 1) % len(self.players)
        print(f"\n本局的庄家是: {self.players[self.dealer_index].name}")

    def setup_blinds(self):
        """
        设置小盲和大盲
        """
        small_blind_index = (self.dealer_index + 1) % len(self.players)
        big_blind_index = (self.dealer_index + 2) % len(self.players)

        small_blind_player = self.players[small_blind_index]
        big_blind_player = self.players[big_blind_index]

        # 小盲下注
        if small_blind_player.bet_chips(1):
            print(f"{small_blind_player.name} 强制下注小盲 (1 筹码)")
        # 大盲下注
        if big_blind_player.bet_chips(2):
            print(f"{big_blind_player.name} 强制下注大盲 (2 筹码)")

        # 更新奖池
        self.state.add_to_pot(3)  # 小盲 1 + 大盲 2 = 3 筹码

    def deal_hands(self):
        """
        给每位玩家发两张手牌
        """
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]
            # 只显示人类玩家的手牌
            if not player.is_ai:
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
        print("\n开始新一局德州扑克游戏！")
        self.deck.reset_deck()  # 每局洗牌
        self.state.reset()  # 重置游戏状态
        self.rotate_dealer()  # 设置庄家
        self.setup_blinds()  # 强制小盲和大盲下注

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
